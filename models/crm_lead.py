from odoo import models, fields, api, _


class CRMLead(models.Model):
    _inherit = 'crm.lead'

    def _notify_thread_by_email(self, message, recipients_data, msg_vals=False,
                                mail_auto_delete=True,
                                model_description=False, force_email_company=False, force_email_lang=False,
                                resend_existing=False, force_send=True, send_after_commit=True,
                                subtitles=None, **kwargs):
        if self._name == 'crm.lead':
            if type(msg_vals) is dict:
                msg_vals.update({'email_layout_xmlid': 'crm_notification.crm_mail_notification_layout'})

        return super()._notify_thread_by_email(message, recipients_data, msg_vals,
                                               mail_auto_delete,
                                               model_description, force_email_company, force_email_lang,
                                               resend_existing, force_send, send_after_commit,
                                               subtitles, **kwargs)
