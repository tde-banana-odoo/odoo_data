# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Slides/eLearning Data with eCommerce',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': ['base_data', 'website_sale_slides'],
    'data': [
        'data/product_data.xml',
        'data/sale_order_data.xml',
        'data/slide_channel_data.xml',
    ],
    'installable': True,
    'auto_install': True,
}
