from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class BudgetPreparation(models.Model):
    _name = 'budget.preparation'
    _inherit = ['dynamic.approval.mixin', 'mail.thread', 'mail.activity.mixin']
    _state_from = ['draft', 'confirm', 'validate1']
    _state_to = ['validate','cancel']
    _description = 'Budget Preparation'

    name = fields.Char(string="Name", required="1")
    description = fields.Char(string="Description")
    from_date = fields.Date(string="From Date", required="1")
    to_date = fields.Date(string="To Date", required="1")
    department = fields.Many2one('hr.department', string="Department", required="1")
    state = fields.Selection(
        [('draft', 'Draft'), ('confirm', 'Confirm'), ('validate1', 'Approved'), ('validate', 'Validated'),
         ('cancel', 'Cancel')],
        string="Status", default="draft", required="1", tracking=True)
    user_id = fields.Many2one('res.users', string="Responsible", required="1")
    budget_preparation_lines = fields.One2many('budget.preparation.line', 'budget_preparation_id')
    is_department_manager = fields.Boolean(string="Is department manager", compute="compute_is_department_manager")


    @api.constrains('from_date', 'to_date')
    def _validate_date_interval(self):
        for rec in self:
            from_date = rec.from_date
            to_date = rec.to_date
            if all((from_date, to_date)):
                if from_date.year != to_date.year:
                    raise ValidationError(_("The Interval period has to be in the same year"))


    @api.depends('department')
    def compute_is_department_manager(self):
        for record in self.sudo():
            is_department_manager = False
            if record.department and record.department.manager_id:
                if record.department.manager_id.user_id == self.env.user:
                    is_department_manager = True
            record.is_department_manager = is_department_manager

    # def action_confirm(self):
    #     self.state = 'confirm'
    #
    # def action_approve(self):
    #     self.state = 'approve'

    def action_validate(self):
        self.state = 'validate'

    def action_cancel(self):
        self.state = 'cancel'


class BudgetPreparationLine(models.Model):
    _name = 'budget.preparation.line'
    _description = 'Budget Preparation Line'

    budget_preparation_id = fields.Many2one('budget.preparation')
    budget_position_id = fields.Many2one('account.budget.post', string="Budget position", required="1")
    planned_amount = fields.Monetary(string="Planned Amount", required="1")
    approved_amount = fields.Monetary(string="Approved Amount")
    analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string='Analytic Account')
    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related="company_id.currency_id")
    company_ids = fields.Many2many('res.company', 'company_budget_preparation_rel', 'budget_preparation_id', 'company_id',
                                   string='Companies',default=lambda self: self.env.company)
