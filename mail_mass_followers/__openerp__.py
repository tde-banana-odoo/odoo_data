# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Followers Tools',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
Play with followers. For my tests.
===================================
    """,
    'depends': ['base', 'mail'],
    'data': [
        'security//ir.model.access.csv',
        'wizard/mail_followers_mass_add_views.xml',
        'wizard/res_partner_mass_create_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
