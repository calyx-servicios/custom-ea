from odoo import models, api, fields, _

class AccountPaymentGroup(models.Model):
    _inherit = "account.payment.group"

    matched_move_line_ids_qty = fields.Integer('Matched Move Lines Qty', default=0)


    @api.multi
    def _compute_matched_move_line_ids(self):
        super(AccountPaymentGroup, self)._compute_matched_move_line_ids()
        for rec in self:
            qty = len(rec.matched_move_line_ids)
            rec.write({'matched_move_line_ids_qty': qty})

