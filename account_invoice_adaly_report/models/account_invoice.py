# Copyright 2021 Calyx S.A.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, api, fields
import logging

_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def _current_company_adaly(self):
        for rec in self:
            _logger.info("here")
            _logger.info("USER: %s" % self.env.user.company_id.id)
            if self.env.user.company_id.id == 18:
                _logger.info("entro")
                flag = True
            else:
                flag = False

            rec.keep_company_adaly = flag

    @api.multi
    def print_account_adaly_voucher(self):
        return self.env.ref(
            "account_invoice_adaly_report.action_custom_invoice_report"
        ).report_action(self)

    keep_company_adaly = fields.Boolean(
        string="Adaly", compute="_current_company_adaly"
    )
