# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class TripLocation(models.Model):
    _name = 'trip.location'
    _description = 'Trip Location'
    _inherit = ['mail.thread']

    name = fields.Char('Trip Location', required=True)
    image = fields.Binary('Image', attachment=True)
    user_id = fields.Many2one('res.users', 'Responsible', default=lambda self: self.env.uid)
    partner_id = fields.Many2one('res.partner', 'Customer')
    short_description = fields.Text('Short Description')
    description = fields.Html('Description')
    attendee_ids = fields.One2many('trip.attendee', 'location_id', 'Attendees')
    attendee_count = fields.Integer('# Attendees', compute='_compute_attendee_count')
    dog_permission = fields.Boolean('Dog Allowed', default=False)

    @api.one
    @api.depends('attendee_ids.location_id')
    def _compute_attendee_count(self):
        self.attendee_count = len(self.attendee_ids)


class TripAttendee(models.Model):
    _name = 'trip.attendee'
    _description = 'Trip Attendee'
    _inherit = ['mail.thread']

    name = fields.Char('Name')
    email = fields.Char('Email')
    partner_id = fields.Many2one('res.partner', 'Customer')
    location_id = fields.Many2one('trip.location', 'Location', required=True)
    user_id = fields.Many2one('res.users', 'Responsible', related='location_id.user_id', store=True)

    @api.model
    def create(self, vals):
        if vals.get('partner_id'):
            partner = self.env['res.partner'].browse(vals['partner_id'])
            vals['name'] = partner.name
            vals['email'] = partner.email
        attendee = super(TripAttendee, self).create(vals)
        return attendee
