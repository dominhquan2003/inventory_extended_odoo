from odoo import models, fields, api  # type:ignore
from odoo.exceptions import ValidationError  # type:ignore


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    # order_id = fields.Many2one('sale.order', string='Sale Order', related='order_id', readonly=True)
    partner_id_test = fields.Many2one(
        "res.partner",
        related='order_id.partner_id',
    )
    virtual_available = fields.Float(related="product_template_id.virtual_available")
    qty_available = fields.Float(related="product_template_id.qty_available")

    