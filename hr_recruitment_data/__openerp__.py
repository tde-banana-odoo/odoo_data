# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Recruitment Data',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': ['hr_data', 'hr_recruitment'],
    'data': [
        'data/hr_recruitment_data.xml',
    ],
    'installable': True,
    'auto_install': True,
}
