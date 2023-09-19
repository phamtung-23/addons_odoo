# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, exceptions

class RegionsModel(models.Model):
    _name = "regions.managerment"
    _description = "Regions Managerment"

    name = fields.Char("Region name", required=True)
    code = fields.Char("Region code", required=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], string='Status', default='active')

    parent_regions_id = fields.Many2one('parent.regions.managerment', string='Parent Regions', required=True)
    

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.code + ' - ' + record.name))
        return result
    

    

    