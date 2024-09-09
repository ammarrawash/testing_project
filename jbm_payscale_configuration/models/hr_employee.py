from odoo import models, fields, api, _


class EmployeeCustom(models.Model):
    _inherit = 'hr.employee'

    payscale_id = fields.Many2one(comodel_name="employee.payscale", string="Pay Scale")
