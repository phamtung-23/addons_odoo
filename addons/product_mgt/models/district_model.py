# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, exceptions

class DistrictModel(models.Model):
    _name = "district.managerment"
    _description = "District Managerment"

    name = fields.Char("District name", required=True)
    code = fields.Char("District code", required=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], string='Status', default='active')

    city_id = fields.Many2one('city.managerment', string='City', required=True)
    region = fields.Char(related='city_id.regions_id.name', string='Regions', readonly=True)
    parent_regions = fields.Char(related='city_id.parent_regions', string='Parent Regions', readonly=True)
    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.code + ' - ' + record.name))
        return result

    

    

    