{
    'name': 'Base Advanced Approval',
    'summary': 'Allow to set advanced approval cycle',
    'author': 'Intalio EverTeam',
    'maintainer': 'Abdalla Mohamed',
    'website': 'https://www.intalio.com/',
    'version': '15.0.1.1.0',
    'category': 'Hidden/Tools',
    'license': 'OPL-1',
    'depends': [
        'base',
        'resource',
        'mail',
    ],
    'data': [
        'security/ir_module_category.xml',
        'security/res_groups.xml',
        'security/ir_rule.xml',
        'security/ir.model.access.csv',
        'wizards/approve_dynamic_approval_wizard.xml',
        'wizards/reject_dynamic_approval_wizard.xml',
        'wizards/recall_dynamic_approval_wizard.xml',
        'views/dynamic_approval.xml',
        'views/dynamic_approval_request.xml',
        'views/ir_ui_menu.xml',
        'views/res_config_settings.xml',
        'data/mail_activity_type.xml',
        'data/ir_cron.xml',
        "templates/tier_validation_templates.xml",
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
