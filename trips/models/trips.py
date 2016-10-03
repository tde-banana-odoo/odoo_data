# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class TripLocation(models.Model):
    _name = 'trip.location'
    _description = 'Trip Location'

    name = fields.Char('Trip Location', required=True)
    image = fields.Binary('Image', attachment=True)
    user_id = fields.Many2one('res.users', 'Responsible', default=lambda self: self.env.uid)
    partner_id = fields.Many2one('res.partner', 'Customer')
    short_description = fields.Text('Short Description')
    description = fields.Html('Description')
    dog_permission = fields.Boolean('Dog Allowed', default=False)


class TripAttendee(models.Model):
    _name = 'trip.attendee'
    _description = 'Trip Attendee'

    name = fields.Char('Name')
    email = fields.Char('Email')
    partner_id = fields.Many2one('res.partner', 'Customer')

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        if self.partner_id:
            self.name = self.partner_id.name
            self.email = self.partner_id.email

    @api.model
    def create(self, vals):
        if vals.get('partner_id'):
            partner = self.env['partner_id'].browse(vals['partner_id'])
            vals['name'] = partner.name
            vals['email'] = partner.email
        attendee = super(TripAttendee, self).create(vals)
        return attendee
