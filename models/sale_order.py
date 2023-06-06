from odoo import models, fields, api  # type:ignore


class quotation(models.Model):
    _inherit = 'sale.order'

       