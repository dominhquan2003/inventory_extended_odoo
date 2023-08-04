from odoo import models, fields, api  # type:ignore
from odoo.exceptions import ValidationError  # type:ignore


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
  

    virtual_available = fields.Float(
        related="product_template_id.virtual_available"
    )
    qty_available = fields.Float(
        related="product_template_id.qty_available"
    )

    def name_get(self):
        result = []
        for so_line in self:
            name = so_line.product_id.name
            result.append((so_line.id, name))
        return result