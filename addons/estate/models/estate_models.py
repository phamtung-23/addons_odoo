# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, exceptions
from datetime import timedelta
from odoo.tools.float_utils import float_compare, float_is_zero



class EstateModel(models.Model):
    _name = "estate.model"
    _description = "estate table data"
    _order = "id desc"

    name = fields.Char("Name model", required=True)
    description = fields.Text("Description model")
    postcode = fields.Char("Postcode model", groups="estate.group_estate_model_user")
    date_availability = fields.Date("Date availability", copy=False, default=fields.Date.today())
    expected_price = fields.Float("Expected price", required=True)
    selling_price = fields.Float("Selling price ", readonly=True, copy=False)
    bedrooms = fields.Integer("Bedrooms", default=2)
    living_area = fields.Integer("Living area")
    facades = fields.Integer("Facades")
    garades = fields.Boolean("Garages")
    garden_area = fields.Integer("Garden area")
    garden_orientation = fields.Selection([
        ("north", "North"), 
        ("south", "South"), 
        ("east", "East"), 
        ("west", "West")
    ])
    active = fields.Boolean('Active', default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('canceled', 'Canceled')
    ], string='State', required=True, default='new', copy=False) 

    property_type_id = fields.Many2one("estate.property.type", string="Property Type")

    buyer_id = fields.Many2one('res.partner', string='buyer', index=True, tracking=True, copy=False)
    salesperson_id = fields.Many2one('res.users', string='Salesperson', index=True, tracking=True, default=lambda self: self.env.user)

    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offer")

    total_erea = fields.Integer("Total area", compute="_get_total_area")

    offer_id = fields.Many2one('estate.property.offer', string='Offers')
    best_price = fields.Float(string='Best Offer Price', compute='_compute_best_price', store=True)

    _sql_constraints = [
        ('check_price_positive', 'CHECK(expected_price > 0 AND selling_price >= 0)',
         'The property expected price and selling price must be strictly positive!')
    ]

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price'), default=0.0)
    @api.depends("living_area", "garden_area")
    def _get_total_area(self):
        for record in self:
            record.total_erea = record.living_area + record.garden_area

    @api.onchange('garades')
    def _onchange_garades(self):
        if self.garades:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False

    def sold_action(self):
        if self.state == 'canceled':
            raise exceptions.UserError('You can not sold canceled property')
        else:
            self.write({'state': 'sold'})

    def cancel_action(self):
        self.write({'state': 'canceled'})


    @api.constrains('selling_price', 'expected_price')
    def check_price(self):
        for record in self:
            if (not float_is_zero(record.expected_price, precision_digits=2) and not float_is_zero(record.selling_price, precision_digits=2)):
                if record.selling_price < (record.expected_price * 0.9):
                    raise exceptions.ValidationError('The selling price cannot be lower than 90% of the expected price')



