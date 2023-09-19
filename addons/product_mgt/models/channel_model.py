# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, exceptions

class ChannelModel(models.Model):
    _name = "channel.managerment"
    _description = "Channel Managerment"

    name = fields.Char("Channel name", required=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], string='Status', default='active')

    
    

    

    