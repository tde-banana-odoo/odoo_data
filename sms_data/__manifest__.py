# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'SMS Data',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': ['base_data', 'mail_data', 'sms'],
    'data': [
        'data/configuration_data.xml',
        'data/configuration_data_private.xml',  # comment if necessary
        # 'data/configuration_data_private_11.xml',  # comment if necessary
        'data/configuration_data_private_12.xml',  # comment if necessary
    ],
    'installable': True,
    'auto_install': True,
}
