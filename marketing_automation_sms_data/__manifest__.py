# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Marketing Automation SMS Data',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': ['base_data', 'marketing_automation_sms'],
    'data': [
        'data/mailing_data.xml',
        'data/marketing_campaign_data.xml',
    ],
    'installable': True,
    'auto_install': True,
}
