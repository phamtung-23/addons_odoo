# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, exceptions

class CityModel(models.Model):
    _name = "city.managerment"
    _description = "City Managerment"

    name = fields.Char("City name", required=True)
    code = fields.Char("City code", required=True)
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ], string='Status', default='active')

    

    regions_id = fields.Many2one('regions.managerment', string='Regions', required=True)
    parent_regions = fields.Char(related='regions_id.parent_regions_id.name', string='Parent Regions', readonly=True)


    

    

    