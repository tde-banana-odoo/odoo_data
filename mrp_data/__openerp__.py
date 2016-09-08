# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'MRP Data',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': ['base_data', 'mrp'],
    'data': [
        'data/resource_data.xml',
        'data/product_data.xml',
    ],
    'installable': True,
    'auto_install': False,
}
