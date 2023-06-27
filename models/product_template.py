from odoo import models, fields, api #type:ignore


class Product(models.Model):
    _inherit = "product.template"

    customer_id = fields.Many2one(
        "res.partner", 
        required=True,
        domain = [('customer_rank','>', 0)]
    )
    detailed_type = fields.Selection(
        default='product',
    )
    total = fields.Float('Total', compute='_compute_total', store=True)

    @api.depends('qty_available', 'list_price')
    def _compute_total(self):
        for product in self:
            product.total = product.qty_available * product.list_price
    
