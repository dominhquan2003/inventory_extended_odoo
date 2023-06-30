from odoo import models, fields, api  # type:ignore


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    partner_id_test = fields.Many2one(
        "res.partner",
        related='order_id.partner_id',
    )
    virtual_available = fields.Float(compute='_compute_virtual_available',store=True)
    qty_available = fields.Float(compute='_compute_qty_available',store=True)

    @api.depends('product_id.product_tmpl_id.qty_available')
    def _compute_qty_available(self):
        for line in self:
            line.qty_available = line.product_id.product_tmpl_id.qty_available

    @api.depends('product_id.product_tmpl_id.virtual_available')
    def _compute_virtual_available(self):
        for line in self:
            line.virtual_available = line.product_id.product_tmpl_id.virtual_available

    



