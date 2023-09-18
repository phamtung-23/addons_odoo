# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Education(models.Model):
    _name = 'education'
    _description = 'Education Tutorial'

    name = fields.Char(string='Name')
    type_of_course = fields.Selection([
        ('online', 'Online'),
        ('offline', 'Offline'),
    ])
    level_of_course = fields.Selection([
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    number_of_lesson = fields.Integer(string='Number of Lesson')

    # Adding new fields
    image = fields.Binary(string='Image', attachment=True)
    html_description = fields.Html(string='Description')
    image_url = fields.Char(compute='_compute_image_url', string='Image URL', store=False)

    status = fields.Selection([
        ('new', 'New'),
        ('open', 'Open'),
    ])

    is_free = fields.Boolean(string='Is Free?')
    price = fields.Float(string='Price')

    @api.depends('image')
    def _compute_image_url(self):
        for record in self:
            if record.image:
                record.image_url = '/web/image/education/%s/image/' % (record.id)
            else:
                record.image_url = False