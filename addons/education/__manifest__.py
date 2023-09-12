# -*- coding: utf-8 -*-
{
    'name': "Education",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "School of Thought",
    'website': "http://www.yourcompany.com",

    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/assets.xml',
        'views/views.xml',
        'views/menus.xml',
        'views/template_menus.xml',
        'views/templates.xml',
        'views/s_course_lessons.xml',
        'views/snippets.xml',

    ],
   
}