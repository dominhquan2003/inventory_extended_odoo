from odoo import models, fields, api  # type:ignore
from odoo.exceptions import ValidationError  # type:ignore


class ResCurrencyRate(models.Model):
    _inherit = "res.currency.rate"

    currency_id = fields.Many2one(
        default=lambda self: (
            self.env.ref('base.VND').id
        )
    )