# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, exceptions

class ShopTypeModel(models.Model):
    _name = "shop.type.managerment"
    _description = "Shop Type Managerment"

    name = fields.Char("Shop type", required=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], string='Status', default='active')

    
    

    

    