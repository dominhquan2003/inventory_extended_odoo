from odoo import models, fields, api #type:ignore


class Product(models.Model):
    _inherit = "product.template"

    customer_id = fields.Many2one(
        "res.partner", 
        string="Customer"
    )
    detailed_type = fields.Selection(
        default='product',
    )
    
