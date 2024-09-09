from odoo import models, fields, api
import pytz


class InheritHrLeave(models.Model):
    _inherit = 'hr.leave'

    @api.model_create_multi
    def create(self, vals_list):
        holidays = super(InheritHrLeave, self).create(vals_list)
        for holiday in holidays:
            message = f"تم تقديم طلب الإجازة ({holiday.holiday_status_id.with_context(lang='ar_001').name}) بتاريخ من {holiday.request_date_from} إلى {holiday.request_date_to} للموظف {holiday.employee_ids.arabic_name if holiday.employee_ids.arabic_name else ''}"            # message = "تم تقديم طلب الإجازة {} بتاريخ من {}".format(
            print("message:", message)
            for employee in holiday.sudo().employee_ids:
                user = employee.sudo().leave_manager_id
                if user:
                    employee_manager = self.env['hr.employee'].search([('user_id','=', user.id)])
                    # employee_manager.sudo().with_context(message=message).send_sms_message()
                # employee.sudo().with_context(message=message).send_sms_message()
        return holidays

    def action_validate(self):
        if self.sudo().employee_ids:
            employee_model = self.sudo().env['ir.model'].search([
                ('model', '=', 'hr.employee')
            ])
            if employee_model:
                ooredo_employee_conf = self.sudo().env['dynamic.integration.configuration'].sudo().search([
                    ('model_id', '=', employee_model.id)
                ])
                if ooredo_employee_conf:
                    # message = f")تم اعتماد طلب الإجازة {self.holiday_status_id.with_context(lang='ar_001').name} بتاريخ من ({self.request_date_from} إلي {self.request_date_to}"
                    message = "تم اعتماد طلب الإجازة (%s) بتاريخ من %s إلى %s " % (self.holiday_status_id.with_context(lang="ar_001").name, self.request_date_from, self.request_date_to)
                    # for employee in self.sudo().employee_ids:
                    #     employee.sudo().with_context(message=message).send_sms_message()
        return super(InheritHrLeave, self).action_validate()

    def action_refuse(self):
        if self.sudo().employee_ids:
            employee_model = self.sudo().env['ir.model'].search([
                ('model', '=', 'hr.employee')
            ])
            if employee_model:
                ooredo_employee_conf = self.sudo().env['dynamic.integration.configuration'].sudo().search([
                    ('model_id', '=', employee_model.id)
                ])
                if ooredo_employee_conf:
                    message = "تم رفض طلب الإجازة (%s) بتاريخ من %s إلى %s " % (
                    self.holiday_status_id.with_context(lang="ar_001").name, self.request_date_from,
                    self.request_date_to)
                    for employee in self.sudo().employee_ids:
                        employee.sudo().with_context(message=message).send_sms_message()
        return super(InheritHrLeave, self).action_refuse()

