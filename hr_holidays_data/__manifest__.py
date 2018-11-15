# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Holidays Data',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': ['hr_data', 'hr_holidays'],
    'data': [
        'data/hr_leave_type_data.xml',
        'data/res_partner_data.xml',
    ],
    'installable': True,
    'auto_install': True,
}
