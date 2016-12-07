# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Project Issue Data',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
This module adds vigorous data. For my tests.
==============================================
    """,
    'depends': ['project_data', 'project_issue'],
    'data': [
        'data/project_issue_data.xml',
    ],
    'installable': True,
    'auto_install': True,
}
