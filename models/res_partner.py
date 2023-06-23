from odoo import models, fields, api  # type:ignore
from odoo.exceptions import ValidationError  # type:ignore


class Partner(models.Model):
    _inherit = "res.partner"

    country_id = fields.Many2one(
        default=241
    )

    @api.constrains('phone')
    def get_phone_type(self):
        if not 10 < len(self.phone.strip()) < 17:
            raise ValidationError("Invalid phone number!")
