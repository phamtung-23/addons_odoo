# -*- coding: utf-8 -*-
{
    'name': 'Coffeemug Base',
    'version': '1.1',
    'category': 'Uncategorized',
    'summary': 'Replaces Odoo branding with custom SIRS branding',
    'description': """
        Replaces the Odoo logo in the header with a custom logo SIRS
        Replaces the Odoo favicon with a custom favicon SIRS
        Replaces the Odoo copyright notice in the footer with a custom SIRS copyright notice 
    """,
    'depends': [],
    'data': [
        'views/templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'post_init_hook': '_post_install_hook',
    'assets': {
        'web.assets_frontend': [
            '/coffeemug_base/static/src/css/hide_odoo.css',
        ],
        'web.assets_backend': [
            '/coffeemug_base/static/src/js/user_menu.js',
            '/coffeemug_base/static/src/js/change_title.js',
            '/coffeemug_base/static/src/xml/icon_template.xml',
            '/coffeemug_base/static/src/js/add_icon_systray.js',
            # '/coffeemug_base/static/src/xml/switch_company_menu.xml',
            # '/coffeemug_base/static/src/js/switch_company_menu.js'
        ],
    },
}