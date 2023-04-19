{
    'name': 'crm_notification',
    'version': '16.0.1.1',
    'category': 'layout',
    'description': "The CRM Email Notification Template Simplifier is a module designed to simplify the appearance of"
                   "CRM email notifications/email in order to avoid them being marked as spam or ending up in the "
                   "recipient's junk folder.",
    'depends': [
        'base',
        'crm'
    ],
    'data': [
        'data/crm_email_template.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
