# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'User / Partner Data',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': ['base', 'mail'],
    'data': [
        'data/res_partner_data.xml',
        'data/configuration_data.xml',
    ],
    'installable': True,
    'auto_install': False,
}
