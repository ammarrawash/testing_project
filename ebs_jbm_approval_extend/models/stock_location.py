# -*- coding: utf-8 -*-from odoo import models, fields, apiclass StockLocation(models.Model):    _inherit = 'stock.location'    is_material_request_location = fields.Boolean(string="Is Material Request Location?")