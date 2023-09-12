# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
import requests
import os

class RelatedLogo(models.Model):
    _inherit = 'res.company'

    def related_company_logo(self):
        """Sets company logo"""
        first_company = self.search([], limit=1)
        if first_company:
            module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            logo_path = os.path.join(module_path, 'static', 'src', 'img', 'SIRS_logo_color.png')
            favicon_path = os.path.join(module_path, 'static', 'src', 'img', 'favicon.png')
            
            first_company.write({
                'logo': self.convert_image_to_base64(logo_path),
                'favicon': self.convert_image_to_base64(favicon_path)
            })

    def convert_image_to_base64(self, image_path):
        """Utility to convert image to base64"""
        if os.path.isfile(image_path):
            with open(image_path, 'rb') as image_file:
                return base64.b64encode(image_file.read())
        return False


    
   