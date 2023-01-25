# -*- coding: utf-8 -*-
# from odoo import http


# class Test0(http.Controller):
#     @http.route('/test0/test0', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test0/test0/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test0.listing', {
#             'root': '/test0/test0',
#             'objects': http.request.env['test0.test0'].search([]),
#         })

#     @http.route('/test0/test0/objects/<model("test0.test0"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test0.object', {
#             'object': obj
#         })
