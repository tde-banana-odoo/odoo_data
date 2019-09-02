# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Slides/eLearning Data with Survey',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': ['base_data', 'website_slides_survey'],
    'data': [
        'data/survey_survey_data.xml',
        'data/slide_slide_data.xml',
    ],
    'installable': True,
    'auto_install': True,
}
