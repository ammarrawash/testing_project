# -*- coding: utf-8 -*-
{
    'name': "JBM Portal User Self Service",
    'summary': """Give Access To Porta User To create his Own requests On Backend""",
    'description': """Give Access To Porta User To create his Own requests On Backend""",
    'author': "M.Deeb",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base_portal_user', 'ebs_fusion_contacts', 'ebs_fusion_crm', 'ebs_fusion_documents',
                'hr_work_entry_contract_enterprise', 'hr_expense', 'hr_holidays', 'hr_payroll', 'ebs_lb_payroll',
                'hr_contract', 'hr_attendance', 'ake_early_late_attandence', 'matco_loan_management',
                'jbm_group_access_right_extended','jbm_hr_appraisal','product',
                'jbm_payscale_configuration', 'hr_allowance_request', 'hr_loan_extended', 'hr_dependents_fare', 'hr_employee_custom'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'data/security_role.xml',
        'data/cron_job.xml',
        'views/editor.xml',
        'views/menus.xml',
        'views/hr_employee.xml',
        'views/res_users.xml',
        'views/hr_attendance.xml',
        'views/loan.xml',
        'views/approvals.xml',
        'views/hr_leave.xml',
        'views/product_product.xml',
        'views/product_category.xml',
        'report/permit_over_time.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'jbm_portal_self_service/static/src/css/hr_dashboard.css',
            'jbm_portal_self_service/static/src/css/lib/nv.d3.css',
            'jbm_portal_self_service/static/src/js/hr_dashboard.js',
            'jbm_portal_self_service/static/src/js/administrative_dashboard.js',
            'jbm_portal_self_service/static/src/js/itServicesDashboard.js',
            'jbm_portal_self_service/static/src/js/selfservice_dashboard.js',
            'jbm_portal_self_service/static/src/js/lib/d3.min.js',
        ],
        'web.assets_qweb': [
            'jbm_portal_self_service/static/src/xml/hr_dashboard.xml',
            'jbm_portal_self_service/static/src/xml/adminstrative_dashboard.xml',
            'jbm_portal_self_service/static/src/xml/it_dashboard.xml',
            'jbm_portal_self_service/static/src/xml/selfservice_dashboard.xml',
        ],
    },

    'demo': [],
}
