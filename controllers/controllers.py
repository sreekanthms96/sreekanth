# -*- coding: utf-8 -*-
from odoo import http


class Bikes(http.Controller):
    @http.route('/bikes/bikes/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/bikes/bikes/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('bikes.listing', {
            'root': '/bikes/bikes',
            'objects': http.request.env['bikes.bikes'].search([]),
        })

    @http.route('/bikes/bikes/objects/<model("bikes.bikes"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('bikes.object', {
            'object': obj
        })
