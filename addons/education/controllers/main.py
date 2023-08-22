from odoo import http
from odoo.http import request
import json


class Main(http.Controller):
   @http.route('/course', type='http', auth="public", website=True)
   def course(self):
      return request.render('education.course_template', {
            'courses': request.env['education'].search([]),
         })

   @http.route('/course/<model("education"):course>', type='http', auth="user", website=True)
   def course_detail(self, course):
      return request.render( 'education.course_detail', {'courses': course,})

