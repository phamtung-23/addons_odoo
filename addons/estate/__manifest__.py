# -*- coding: utf-8 -*-

{
    'name': 'estate',
    'version': '0.2',
    'summary': 'This is my new module!',
    'sequence': 10, 
    'description': "estate estate estate",
    "depends": [
        "base",
        "web",
    ],
    'data': [
        'security/estate_model_security.xml',
        'security/ir.model.access.csv',
        'views/estate_type_action.xml',
        'views/estate_menus.xml',
        'views/estate_view.xml',
        'views/estate_type_view.xml',
        'views/estate_tag_view.xml',
        'views/estate_offer_view.xml',
        'views/res_users_form_inheritance_view.xml',
    ],
}