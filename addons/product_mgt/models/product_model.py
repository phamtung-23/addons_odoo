# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, exceptions

class ProductModel(models.Model):
    _name = "product.managerment"
    _description = "Product Managerment"

    name = fields.Char("Product name", required=True)
    description = fields.Text("Product Description")
    image = fields.Binary("Product Image")
    active = fields.Boolean('Active', default=True)
    price = fields.Float("Sale price")
    

    

    