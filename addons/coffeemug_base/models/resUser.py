from odoo import models, fields, api
import base64
import os

class ResUsers(models.Model):
    _inherit = 'res.users'

    def update_odoo_bot_details(self):
        """Sets icon, name, email for Odoo Bot user"""
        odoo_bot = self.env.ref('base.user_root')
        module_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logo_path = os.path.join(module_path, 'static', 'src', 'img', 'SIRS_logo_color.png')
        if odoo_bot:
            odoo_bot.name = "SIRS System"
            odoo_bot.image_1920 = self.convert_image_to_base64(logo_path)
            odoo_bot.email = "sirssytem@example.com"

    def convert_image_to_base64(self, image_path):
        """Utility to convert image to base64"""
        if os.path.isfile(image_path):
            with open(image_path, 'rb') as image_file:
                return base64.b64encode(image_file.read())
        return False
