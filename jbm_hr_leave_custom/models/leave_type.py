# -*- coding: utf-8 -*-from odoo import models, fields, api, _class InheritHLeaveType(models.Model):    _inherit = 'hr.leave.type'    validation_document_after = fields.Integer(string="Validation Document After")