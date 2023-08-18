# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class Product(models.Model):
    _name = "my.module.product"
    _description = "this is product models in my module!"

    name = fields.Char(string="Name product")
    size = fields.Selection([
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
    ])
    material = fields.Selection([
        ('cotton', 'Cotton'),
        ('polyester', 'Polyester'),
        ('wool', 'Wool'),
    ])
    price = fields.Float(string="Price")
    image_url = fields.Char(string="Image url")
    description = fields.Text(string="Description product")

    category_id = fields.Many2one("my.module.category", string="Category")

    image_html = fields.Html(string="Image HTML", compute="_compute_image_html")

    _sql_constraints = [
        ('check_unique_product_name', 'unique(name)', 'Product name must be unique!')
    ]

    @api.depends('image_url')
    def _compute_image_html(self):
        for record in self:
            if record.image_url:
                record.image_html = '<img src="%s" style="max-width: 300px; max-height: 300px;" />' % record.image_url
            else:
                record.image_html = False