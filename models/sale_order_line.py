from odoo import models, fields, api  # type:ignore


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_template_id = fields.Many2one(
        domain=[]
        # domain=[('sale_ok', '=', True), ('customer_id','=', order_id.partner_id)]
    )
