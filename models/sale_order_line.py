from odoo import models, fields, api  # type:ignore
from odoo.exceptions import ValidationError  # type:ignore
import logging


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
  

    partner_id_test = fields.Many2one(
        "res.partner",
        related='order_id.partner_id',
    )
    virtual_available = fields.Float(
        related="product_template_id.virtual_available"
    )
    qty_available = fields.Float(
        related="product_template_id.qty_available"
    )
     # kiểm tra xem user hiện tại có ở trong group 'sales_team.group_sale_manager' không
    sale_group = fields.Boolean(
        compute="_compute_sale_group",
    )

    def _compute_sale_group(self):
        is_admin = self.env.user in self.env.ref('sales_team.group_sale_manager').users
        # context = dict(self.env.context)
        # context.update({'is_admin': 0})
        # self.env.context = context
        logging.error(f"AAAAAAAAAAAAAA{self.env.context}")
        for rc in self:
            rc.sale_group = is_admin
            

    def name_get(self):
        result = []
        for so_line in self:
            name = so_line.product_id.name
            result.append((so_line.id, name))
        return result
    