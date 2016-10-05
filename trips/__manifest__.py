# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Trips',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
Organize and manage trips !
===========================
    """,
    'depends': ['mail', 'rating', 'website', 'base_data'],
    'data': [
        'data/trips_data.xml',
        'data/mail_template_data.xml',
        'security/ir.model.access.csv',
        'views/trips_views.xml',
        'views/trips_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
