from odoo import models, fields, api #type:ignore


class Customer(models.Model):
    _name = 'newsale.customer'
    _description = 'customer of sale'

    name = fields.Char()
    
