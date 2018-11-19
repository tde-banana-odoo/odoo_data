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
        'data/configuration_data.xml',
        'data/configuration_data_private.xml',  # comment me if necessary
        'data/res_partner_category_data.xml',
        'data/res_partner_data.xml',
        'data/res_partner_data_private.xml',  # comment me if necessary
        'data/res_partner_data_private_11.xml',  # comment me if necessary
        # 'data/res_partner_data_private_12.xml',  # comment me if necessary
    ],
    'installable': True,
    'auto_install': False,
}
