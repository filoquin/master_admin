# -*- coding: utf-8 -*-
from openerp import http

# class MasterAdmin(http.Controller):
#     @http.route('/master_admin/master_admin/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/master_admin/master_admin/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('master_admin.listing', {
#             'root': '/master_admin/master_admin',
#             'objects': http.request.env['master_admin.master_admin'].search([]),
#         })

#     @http.route('/master_admin/master_admin/objects/<model("master_admin.master_admin"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('master_admin.object', {
#             'object': obj
#         })