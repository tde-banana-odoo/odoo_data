# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Slides/eLearning Data (full version)',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': [
        'sale_product_configurator',
        'website_sale_slides_data',
        'website_slides_survey_data',
        'website_slides_forum_data'
    ],
    'data': [
        'data/product_data.xml',
    ],
    'installable': True,
    'auto_install': True,
}
