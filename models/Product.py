from odoo import models, fields, api #type:ignore


class Product(models.Model):
    _name = 'newsale.product'
    _description = 'Product of sale'

    name = fields.Char()
    
