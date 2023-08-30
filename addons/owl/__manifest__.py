# -*- coding: utf-8 -*-
{
    'name': 'Owl Tutorial',
    'version': '1.0',
    'category': 'OWL',
    'summary': 'Owl tutorial',
    'description': """
        Owl tutorial 
    """,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/todo_list.xml',
    ],
    'installable': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'owl/static/src/components/*/*.js',  
            'owl/static/src/components/*/*.xml',  
            'owl/static/src/components/*/*.scss',
              
        ]
    }
}