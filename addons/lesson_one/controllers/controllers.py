from odoo import http
from odoo.http import request
import json


class ProductController(http.Controller):
    # product 
    @http.route('/products', auth='public', website=True)
    def product(self, **kw):
        products = http.request.env['my.module.product'].search([])
        return http.request.render('lesson_one.product_template', {'products': products})

    @http.route('/products/<model("my.module.product"):product>', auth='public', website=True)
    def product_detail(self, product, **kw):
        return http.request.render('lesson_one.product_detail_template', {'product': product})

   

