# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'HR Data',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': ['base_data', 'hr'],
    'data': [
        'data/hr_data.xml',
        'data/hr_employee_data.xml',
    ],
    'installable': True,
    'auto_install': True,
}
