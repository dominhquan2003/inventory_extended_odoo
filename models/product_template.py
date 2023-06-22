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
    
