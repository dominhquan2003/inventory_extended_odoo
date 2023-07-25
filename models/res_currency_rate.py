from odoo import models, fields, api  # type:ignore
from odoo.exceptions import ValidationError  # type:ignore


class ResCurrencyRate(models.Model):
    _inherit = "res.currency.rate"
    _order = "write_date desc"

    currency_id = fields.Many2one(
        default=lambda self: (
            self.env.ref('base.VND').id
        )
    )

    _sql_constraints = [
        ('unique_name_per_day', 'Check(1=1)', 'Only one currency rate per day allowed!'),
        ('currency_rate_check', 'CHECK (rate>0)', 'The currency rate must be strictly positive.'),
    ]

    def _onchange_rate_warning(self):
        return True