from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    associate_id = fields.Many2one(
        string = 'Associate',
        related = 'partner_id.user_id'
    )