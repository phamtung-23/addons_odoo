# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class Product(models.Model):
    _name = "my.module.product"
    _description = "this is product models in my module!"

    name = fields.Char(string="Name product")
    description = fields.Text(string="Description product")

    category_id = fields.Many2one("my.module.category", string="Category")

    _sql_constraints = [
        ('check_unique_product_name', 'unique(name)', 'Product name must be unique!')
    ]