# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Marketing Automation Data',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': ['base_data', 'marketing_automation'],
    'data': [
        'data/mass_mailing_data.xml',
        'data/marketing_automation_data.xml',
        'data/res_partner_data.xml',
    ],
    'installable': True,
    'auto_install': True,
}
