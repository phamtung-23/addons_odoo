# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models

class Category(models.Model):
    _name = "my.module.category"
    _description = "this is category model in my module!"

    name = fields.Char(string="Name category")
    description = fields.Text(string="Description category")

    product_ids = fields.One2many('my.module.product', 'category_id', string="Products")