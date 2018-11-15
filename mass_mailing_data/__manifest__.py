# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Mass Mailing Data',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': ['base_data', 'mass_mailing'],
    'data': [
        'data/res_partner_data.xml',
        'data/mass_mailing_data.xml',
    ],
    'installable': True,
    'auto_install': True,
}
