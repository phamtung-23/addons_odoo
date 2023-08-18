from odoo import http
from odoo.http import request
import json


class TaskAPI(http.Controller):
     # task
    @http.route('/tasks', auth='public', website=True)
    def product(self, **kw):
        products = request.env['my.module.task'].search([])
        return request.render('lesson_one.tasks_template')

    @http.route('/tasks/<int:task_id>', auth='public', website=True)
    def product_detail(self, task_id, **kw):
        return request.render('lesson_one.task_detail_template')

    @http.route('/api/tasks', type='http', auth='none', methods=['GET'], csrf=False)
    def get_tasks(self, **kw):
        tasks = request.env['my.module.task'].sudo().search([])

        task_data = []
        for task in tasks:
            task_data.append({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'priority': task.priority,
                'stage': task.stage,
                'date_deadline': task.date_deadline.strftime('%Y-%m-%d'),
            })

        response = {
            'status': 'success',
            'data': task_data,
        }

        return json.dumps(response)

    @http.route('/api/task/<int:task_id>', type='http', auth='none', methods=['GET'], csrf=False)
    def get_task_id(self, task_id, **kw):
        task = request.env['my.module.task'].sudo().browse(task_id)

        if not task:
            response = {
                'status': 'error',
                'message': 'Task not found',
            }
        else:
            task_data = {
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'priority': task.priority,
                'stage': task.stage,
                'date_deadline': task.date_deadline.strftime('%Y-%m-%d'),
            }
            response = {
                'status': 'success',
                'data': task_data,
            }

        return json.dumps(response)