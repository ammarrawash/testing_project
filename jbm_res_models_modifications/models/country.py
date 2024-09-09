# -*- coding: utf-8 -*-

from odoo import models, fields


class RESCountry(models.Model):
    _inherit = 'res.country'

    nationality = fields.Char(string="Nationality")
