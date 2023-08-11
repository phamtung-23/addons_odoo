# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models

class MyModule(models.Model):
    _name = "my.module"
    _description = "this is my module!"

    name = fields.Char(string="Name")
    date = fields.Date(string="Date")
    amount = fields.Float(string="Amount")
    active = fields.Boolean(string="Active", default=True)