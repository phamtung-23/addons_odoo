from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    notification_type = fields.Selection(
        selection=[
            ('option1', 'Option 1 - New Name'),
        ],
        string='Notification Type',
    )