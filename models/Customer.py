from odoo import models, fields, api  # type:ignore


class Customer(models.Model):
    _inherit = 'res.partner'
    country_id = fields.Many2one(default = 241) 