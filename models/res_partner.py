from odoo import models, fields, api  # type:ignore
from odoo.exceptions import ValidationError  # type:ignore


class Partner(models.Model):
    _inherit = "res.partner"

    country_id = fields.Many2one(
        default=241
    )
    tax_number = fields.Char()
