from xml.dom import ValidationErr
from odoo import models, fields, api  # type:ignore


class Product(models.Model):
    _inherit = "product.template"

    customer_id = fields.Many2one(
        "res.partner",
        required=True,
        domain=[('customer_rank', '>', 0),('is_company', '=', True)]
    )
    detailed_type = fields.Selection(
        default='product',
    )
    # làm field total và kí hiệu tiền tệ
    total = fields.Float('Tổng', compute='_compute_total', store=True)
    currency_id = fields.Many2one(
        'res.currency',
        default=lambda self: self.env.company.currency_id.id)
    
    _sql_constraints = [
        ('unique_name', 'UNIQUE (name)', 'Trùng tên mã hàng.')
    ]
    
    @api.depends('qty_available', 'list_price')
    def _compute_total(self):
        for product in self:
            product.total = product.qty_available * product.list_price

    def _compute_quantities(self):
        super()._compute_quantities()  # Call the original compute method

        for record in self:
            if record.virtual_available > 0:
                record.virtual_available = 0