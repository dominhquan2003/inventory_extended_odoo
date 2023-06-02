from odoo import models, fields, api #type:ignore


class Product(models.Model):
    _inherit = "product.template"

    customer_id = fields.Many2many(
        "res.partner", 
        string="Customer"
    )
    
