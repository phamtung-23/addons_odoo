from odoo import http
from odoo.http import request
import json


class Main(http.Controller):
   @http.route('/course', type='http', auth='public', website=True)
   def test(self):
      return request.render('education.course_template', {
            'courses': request.env['education'].search([]),
         })

   @http.route('/course/<model("education"):course>', type='http', auth="public", website=True, csrf=False)
   def course_detail(self, course):
      return request.render( 'education.courses_detail', {'courses': course,})


   

