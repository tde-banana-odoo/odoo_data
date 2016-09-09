# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Timesheet Data',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': ['hr_timesheet', 'project_data', 'product_data'],
    'data': [
        'data/res_partner_data.xml',
        'data/project_data.xml',
        'data/timesheet_data.xml',
    ],
    'installable': True,
    'auto_install': True,
}
