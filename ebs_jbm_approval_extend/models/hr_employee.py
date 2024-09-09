# -*- coding: utf-8 -*-from odoo import models, fields, _class HREmployee(models.Model):    _inherit = 'hr.employee'    custody_count = fields.Integer(string="Custody", compute='_compute_custody_count')    def _compute_custody_count(self):        internal_picking = self.env['stock.picking.type'].search([('code', '=', 'internal')])        for rec in self:            rec.custody_count = self.env['stock.picking'].search_count(                [('partner_id', '!=', False), ('partner_id', '=', rec.user_id.partner_id.id),                 ('picking_type_id', 'in', internal_picking.ids),                 ('state', '=', 'done')])    def view_employee_custody(self):        self.ensure_one()        internal_picking = self.env['stock.picking.type'].search([('code', '=', 'internal')])        formview_ref = self.env.ref('stock.view_picking_form', False)        treeview_ref = self.env.ref('stock.vpicktree', False)        return {            'name': _('Employee Custody'),            'view_mode': 'tree, form',            'views': [(treeview_ref and treeview_ref.id or False, 'tree'),                      (formview_ref and formview_ref.id or False, 'form')],            'res_model': 'stock.picking',            'domain': [('partner_id', '!=', False), ('partner_id', '=', self.user_id.partner_id.id),                       ('picking_type_id', 'in', internal_picking.ids),                       ('state', '=', 'done')],            'type': 'ir.actions.act_window',        }