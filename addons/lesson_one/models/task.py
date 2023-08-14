# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class Task(models.Model):
    _name = 'my.module.task'
    _description = 'this is my module Task!!!'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')],
        string='Priority', default='low', compute='_compute_priority')
    stage = fields.Selection([
        ('to_do', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')],
        string='Stage', default='to_do')
    date_deadline = fields.Date(string='Deadline')
    
    @api.depends('date_deadline','stage')
    def _compute_priority(self):
        for task in self:
            if task.date_deadline and task.stage == 'in_progress' and task.date_deadline < fields.Date.today():
                task.priority = 'high'
            else:
                task.priority = 'medium'

    def button_start(self):
        self.write({'stage': 'in_progress'})
    
    def button_done(self):
        self.write({'stage': 'done'})
