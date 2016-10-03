# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.addons.website.models.website import slug


class TripLocation(models.Model):
    _name = 'trip.location'
    _description = 'Trip Location'
    _inherit = ['mail.thread', 'website.seo.metadata', 'website.published.mixin']

    name = fields.Char('Trip Location', required=True, track_visibility='always')
    image = fields.Binary('Image', attachment=True)
    user_id = fields.Many2one('res.users', 'Responsible', default=lambda self: self.env.uid)
    partner_id = fields.Many2one('res.partner', 'Customer')
    short_description = fields.Text('Short Description')
    description = fields.Html('Description')
    attendee_ids = fields.One2many('trip.attendee', 'location_id', 'Attendees')
    attendee_count = fields.Integer('# Attendees', compute='_compute_attendee_count')
    dog_permission = fields.Boolean('Dog Allowed', default=False, track_visibility='onchange')

    @api.one
    @api.depends('attendee_ids.location_id')
    def _compute_attendee_count(self):
        self.attendee_count = len(self.attendee_ids)

    @api.multi
    @api.depends('name')
    def _compute_website_url(self):
        super(TripLocation, self)._compute_website_url()
        for location in self:
            if location.id:
                location.website_url = '/trip/%s' % slug(location)

    @api.multi
    def _track_subtype(self, init_values):
        if 'dog_permission' in init_values and self.dog_permission:
            return 'trips.mt_dog'
        return super(TripLocation, self)._track_subtype(init_values)

    @api.multi
    def action_get_ratings(self):
        action = self.env['ir.actions.act_window'].for_xml_id('rating', 'action_view_rating')
        return dict(action, domain=[('res_id', 'in', self.attendee_ids.ids), ('res_model', '=', 'trip.attendee')])


class TripAttendee(models.Model):
    _name = 'trip.attendee'
    _description = 'Trip Attendee'
    _inherit = ['mail.thread', 'utm.mixin', 'rating.mixin']

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

    @api.multi
    def action_send_rating(self):
        rating_template = self.env.ref('trips.mail_template_trip_location_rating')
        for location in self:
            location.rating_send_request(rating_template, reuse_rating=False, force_send=True)
