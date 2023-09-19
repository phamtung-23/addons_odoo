# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, exceptions

class ParentRegionsModel(models.Model):
    _name = "parent.regions.managerment"
    _description = "Parent Regions Managerment"

    name = fields.Char("Parent Region name", required=True)
    code = fields.Char("Parent Region code", required=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], string='Status', default='active')

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.code + ' - ' + record.name))
        return result
    
    

    

    