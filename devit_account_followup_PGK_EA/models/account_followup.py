from functools import reduce
from lxml import etree

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools.misc import formatLang


class FollowupLine(models.Model):
    @api.model
    def _get_default_template(self):
        try:
            return self.env['ir.model.data'].get_object_reference(
                'devit_account_followup_PGK_EA', 'modifiable_payment_follow_up_template_pgk')[
                1]
        except ValueError:
            return False

    _inherit = 'devit_account_followup.followup.line'

class ResPartner(models.Model):
    @api.multi
    def do_partner_mail(self):
        # import wdb
        # wdb.set_trace()
        ctx = self.env.context.copy()
        ctx['followup'] = True
        # partner_ids are res.partner ids
        # If not defined by latest follow-up level,
        # it will be the default template if it can find it
        template = 'devit_account_followup_PGK_EA.modifiable_payment_follow_up_template_pgk'
        unknown_mails = 0
        for partner in self:
            partners_to_email = [child for child in partner.child_ids if
                                 child.type == 'invoice' and child.email]
            if not partners_to_email and partner.email:
                partners_to_email = [partner]
            if partners_to_email:
                level = partner.latest_followup_level_id_without_lit
                for partner_to_email in partners_to_email:
                    if level and level.send_email and \
                            level.email_template_id and \
                            level.email_template_id.id:
                        level.email_template_id.with_context(ctx).send_mail(
                            partner_to_email.id)
                    else:
                        mail_template_id = self.env.ref(template)
                        mail_template_id.with_context(ctx).send_mail(
                            partner_to_email.id)
                if partner not in partners_to_email:
                    partner.message_post(body=_(
                        'Overdue email sent to %s' % ', '.join(
                            ['%s <%s>' % (partner.name, partner.email) for
                             partner in partners_to_email])))
            else:
                unknown_mails = unknown_mails + 1
                action_text = _("Email not sent because of email address "
                                "of partner not filled in")
                if partner.payment_next_action_date:
                    payment_action_date = min(
                        fields.Date.today(),
                        partner.payment_next_action_date)
                else:
                    payment_action_date = fields.Date.today()
                if partner.payment_next_action:
                    payment_next_action = \
                        partner.payment_next_action + " \n " + action_text
                else:
                    payment_next_action = action_text
                partner.with_context(ctx).write(
                    {'payment_next_action_date': payment_action_date,
                     'payment_next_action': payment_next_action})
        return unknown_mails

    _inherit = "res.partner"
