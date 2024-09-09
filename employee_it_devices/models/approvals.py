from odoo import models, fields, api


class InheritApprovals(models.Model):
    _inherit = 'approval.request'

    it_devices_id = fields.Many2many('it.devices')
    is_it_device = fields.Boolean(related="category_id.is_it_device")
