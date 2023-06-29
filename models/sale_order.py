from odoo import models, fields, api  # type:ignore


class SaleOrder(models.Model):
    _inherit = 'sale.order'


