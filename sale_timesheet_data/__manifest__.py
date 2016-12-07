# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Sale Timesheet Data',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': ['sale_data', 'timesheet_data', 'sale_timesheet'],
    'data': [
        'data/sale_data.xml',
        'data/timesheet_data.xml',
    ],
    'installable': True,
    'auto_install': True,
}
