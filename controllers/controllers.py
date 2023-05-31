# -*- coding: utf-8 -*-
# from odoo import http


# class SaleCustomized(http.Controller):
#     @http.route('/sale_customized/sale_customized', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_customized/sale_customized/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_customized.listing', {
#             'root': '/sale_customized/sale_customized',
#             'objects': http.request.env['sale_customized.sale_customized'].search([]),
#         })

#     @http.route('/sale_customized/sale_customized/objects/<model("sale_customized.sale_customized"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_customized.object', {
#             'object': obj
#         })
