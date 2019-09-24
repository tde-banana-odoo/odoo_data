# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Lot of Partner Data',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
MULTI DATA !!!
==============
    """,
    'depends': [
        'base',
        'contacts',
        'mail'],
    'data': [
        'data/res_partner_data.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
