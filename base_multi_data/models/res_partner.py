# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import random

from odoo import api, fields, models, SUPERUSER_ID, _

_logger = logging.getLogger(__name__)


def _create_partners_batch(cr, registry, batch_size=200, batch_count=5, errors=False):
    env = api.Environment(cr, SUPERUSER_ID, {
        'tracking_disable': True,
    })

    base_vals = {
        'country_id': env.ref('base.be').id,
    }
    type_selection = ['contact', 'invoice', 'delivery', 'other']
    street_selection = ['Rue Montluc', 'Rue des Harmonies', 'Rue Romanichel', False]
    titles = env['res.partner.title'].search([]).ids + [False]
    responsibles = env['res.users'].search([('share', '=', False)]).ids + [False]

    env['res.partner'].search([('country_id', '=', base_vals['country_id']), ('user_ids', '=', False), ('is_company', '=', False)]).unlink()
    partners = env['res.partner']
    for x in range(batch_count):
        for y in range(batch_size):
            email = 'test.%03d.%03d@example.com' % (x, y)
            mobile = '0456%03d%03d' % (x, y)
            if errors and y > 0 and y % 20 == 0:
                mobile = False
                email = False
            elif errors and y > 0 and y % 10 == 0:
                email = 'test.%03d.%03d@example.com' % (x, y-1)
                mobile = '0456%03d%03d' % (x, y-1)
            elif errors and y > 0 and y % 5 == 0:
                mobile = 'dummy'
                email = 'dummy'
            create_vals = dict(
                base_vals,
                name='Automatic %03d%03d' % (x, y),
                email=email,
                mobile=mobile,
                street=random.choice(street_selection),
                street2=random.choice(street_selection),
                user_id=random.choice(responsibles),
                title=random.choice(titles),
                type=random.choice(type_selection)
            )
            partners += env['res.partner'].create(create_vals)
        _logger.info('Done batch %s of %s (total: %s)' % (x, batch_size, len(partners)))
    return partners


class Partner(models.Model):
    _inherit = 'res.partner'
    _name = 'res.partner'

    def action_create_batch(self, batch_size=80, batch_count=5):
        new_partners = _create_partners_batch(self.env.cr, self.env.registry, batch_size=batch_size, batch_count=batch_count)
        action = self.env.ref('base.action_partner_form').read()[0]
        action['domain'] = [('id', 'in', new_partners.ids)]
        return action

    def action_create_batch_w_errors(self, batch_size=80, batch_count=10):
        new_partners = _create_partners_batch(self.env.cr, self.env.registry, batch_size=batch_size, batch_count=batch_count, errors=True)
        action = self.env.ref('base.action_partner_form').read()[0]
        action['domain'] = [('id', 'in', new_partners.ids)]
        return action
