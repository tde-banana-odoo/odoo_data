# -*- coding: utf-8 -*-

from openerp import api, fields, models, tools, _


class MassCreate(models.Model):
    _name = 'res.partner.mass.create'

    email = fields.Char('Email')
    counter = fields.Integer('Counter')

    @api.multi
    def action_update(self):
        for i in range(0, self.counter + 1):
            self.env['res.partner'].create({'name': self.email, 'email': self.email})
        return True
