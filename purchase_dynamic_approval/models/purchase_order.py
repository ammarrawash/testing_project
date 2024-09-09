# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _


class PurchaseOrder(models.Model):
    _name = 'purchase.order'
    _inherit = ['purchase.order', 'dynamic.approval.mixin']
    _state_from = ['sent']
    _state_to = ['purchase']


    def _action_final_approve(self):
        """ mark order as approved """
        self.ensure_one()
        self._run_final_approve_function()
        if self._name == 'purchase.order':
            self.button_confirm()
        super(PurchaseOrder, self)._action_final_approve()
        # else:
        #     super(PurchaseOrder, self)._action_final_approve()


    # def _action_reset_original_state(self, reason='', reset_type='reject'):
    #     if self._name == 'purchase.order' and reset_type == 'reject':
    #         self.state = 'rejected'
    #     res = super(PurchaseOrder, self)._action_reset_original_state(reason='', reset_type='reject')
    #
    #     return res
