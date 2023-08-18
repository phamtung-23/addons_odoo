# -*- coding: utf-8 -*-
 
{
    'name': 'lesson one',
    'version': '1.1',
    'summary': 'This is module of lesson one!',
    'sequence': 10, 
    'description': "lesson one",
    "depends": ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/my_module_action.xml',
        'views/my_module_menus.xml',
        'views/my_module_views.xml',
        'views/product_views.xml',
        'views/category_views.xml',
        'views/task_views.xml',
        'report/my_module_report_template.xml',
        'report/inherit_qweb_template.xml',
        'views/template_product.xml',
        'views/template_tasks.xml',
        'views/template_menus.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'lesson_one/static/src/js/task.js',
        ],
    },
}