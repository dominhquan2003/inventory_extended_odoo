from odoo import models, fields, api  # type:ignore


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    partner_id_test = fields.Many2one(
        "res.partner",
        related='order_id.partner_id',
    )
