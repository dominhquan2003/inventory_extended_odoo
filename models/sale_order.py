from odoo import models, fields, api, _  # type:ignore


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    name = fields.Char(
        default=lambda self: _('Đơn hàng mới'))
