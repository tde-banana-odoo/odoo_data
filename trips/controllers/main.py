# -*- coding: utf-8 -*-

from odoo.http import Controller, request, route


class TripController(Controller):

    @route(['/trips', '/trips/page/<int:page>'], type='http', auth="public", website=True)
    def trips(self, page=1):
        location_domain = []
        locations = request.env['trip.location'].search(location_domain)

        values = {
            'locations': locations,
        }

        return request.render("trips.trip_locations_main", values)

    @route(['/trip/<model("trip.location"):location>'], type='http', auth="public", website=True)
    def trip(self, location):
        values = {
            'location': location,
            'main_object': location,
        }

        return request.render("trips.trip_location_main", values)
