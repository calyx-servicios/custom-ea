# Copyright 2021 Calyx S.A.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, api, fields


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    @api.multi
    def _current_company_adaly(self):
        """
        This function check if the company of the current user
        is "Adaly SA"
        I have to use the id number because the company was create
        by interface.
        18 is the company id number of Adaly in production.
        """
        for rec in self:
            if self.env.user.company_id.id == 18:
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

    qr_image = fields.Binary("QR Image", attachment=True)
