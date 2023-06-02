from odoo import models, fields, api  # type:ignore


class Customer(models.Model):
    _inherit = 'res.partner'

       