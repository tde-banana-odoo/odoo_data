# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Paypal Private Data',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """""",
    'depends': ['base_data', 'payment_paypal'],
    'data': [
        'data/configuration_data_private.xml',  # comment if necessary
    ],
    'installable': True,
    'auto_install': True,
}
