# -*- coding: utf-8 -*-from odoo import models, fields, api, _class AccountType(models.Model):    _name = "account.type"    _description = "Account Type"    name = fields.Char(string="Name", required=True)    code = fields.Char(string="Code", required=True)