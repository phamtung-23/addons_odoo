# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, exceptions
from datetime import timedelta
from odoo.tools.float_utils import float_compare, float_is_zero

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Type'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    offer_count = fields.Integer(string='Offers count', compute='_compute_offer_count')

    offer_ids = fields.One2many('estate.property.offer', 'property_type_id', string='Properties')

    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")
    
    _sql_constraints = [
        ('unique_estate_property_type_name', 'unique(name)', 'Property type name must be unique')
    ]

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)