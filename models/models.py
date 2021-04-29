# -*- coding: utf-8 -*-

from odoo import models, fields, api


class bikes(models.Model):
    _name = 'bikes.bikes'
    _description = 'bikes.bikes'

    name = fields.Char('name')
    brand = fields.Char('brand')
    motogprider = fields.Char('motogprider')
    engine = fields.One2many('type.type','enginecc',string='engineconfiguration')
    vehicletype = fields.Many2many('type.type','enginecc',string='VEHICLETYPE')

class type(models.Model):
    _name = 'type.type'
    _description = 'type.type'
    name = fields.Char('name')
    enginecc = fields.Many2one('bikes.bikes',string='BIKERNAME')
    bikerid = fields.Many2many('bikes.bikes' ,string='vehicletype')