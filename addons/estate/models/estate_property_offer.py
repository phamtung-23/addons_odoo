# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, exceptions
from datetime import timedelta
from odoo.tools.float_utils import float_compare, float_is_zero

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Real Estate Property offer'
    _order = 'price asc'

    price = fields.Float(string='Price', required=True)
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ], copy=False)

    partner_id = fields.Many2one('res.partner', string='Buyer', required=True)
    property_id = fields.Many2one('estate.model', string='Property')
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')

    validity = fields.Integer(string='Validity', default=7)
    date_deadline = fields.Date(string='Deadline', compute='_compute_date_deadline', inverse='_inverse_date_deadline')

    _sql_constraints = [
        ('offer_price_positive_check', 'CHECK(price > 0)', 'Offer price must be strictly positive')
    ]
    @api.depends('validity')
    def _compute_date_deadline(self):
        for offer in self:
            if offer.create_date:
                offer.date_deadline = offer.create_date + timedelta(days=offer.validity)
            else:
                current_date = fields.Date.today()
                offer.date_deadline = current_date + timedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            if offer.date_deadline:
                offer.validity = offer.date_deadline.day - offer.create_date.day

    def button_confirm(self):
        self.write({'status': 'accepted'})
        if self.status == 'accepted':
            self.property_id.selling_price = self.price
            self.property_id.buyer_id = self.partner_id

    def button_cancel(self):
        self.write({'status': 'refused'})

            