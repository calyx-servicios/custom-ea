# Copyright 2021 Calyx S.A.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def print_account_adaly_voucher(self):
        return self.env.ref(
            "account_invoice_adaly_report.action_custom_invoice_report"
        ).report_action(self)
