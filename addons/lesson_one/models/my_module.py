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
    title = fields.Char(string="Title")
    author = fields.Char(string="Author")
    publication_date = fields.Date(string="Publication Date")
    genre = fields.Selection([
        ("fantasy", "Fantasy"),
        ("thriller", "Thriller"),
        ("romance", "Romance"),
        ("horror", "Horror"),
    ], string="Genre")

    def action_activate(self):
        self.active = True
    
    def action_deactivate(self):
        self.active = False

    def action_genre(self):
        self.genre = "fantasy"