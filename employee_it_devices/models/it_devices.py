from odoo import models, fields, api


class ItDevices(models.Model):
    _name = 'it.devices'

    name = fields.Char()
