# -*- coding: utf-8 -*-

from . import models
from odoo import api, SUPERUSER_ID


def _post_install_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['res.company'].related_company_logo()
    env['res.users'].update_odoo_bot_details()


