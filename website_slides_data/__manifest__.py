# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Slides/eLearning Data',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': ['base_data', 'website_slides'],
    'data': [
        'data/res_partner_data.xml',
        'data/slide_channel_tag_data.xml',
        'data/slide_channel_data.xml',
        'data/slide_slide_data.xml',
        'data/slide_user_data.xml',
    ],
    'installable': True,
    'auto_install': True,
}
