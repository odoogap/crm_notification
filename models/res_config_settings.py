from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def crm_open_email_layout(self):
        layout = self.env.ref('crm_notification.crm_mail_notification_layout', raise_if_not_found=False)
        if not layout:
            raise UserError(_("This layout seems to no longer exist."))
        return {
            'type': 'ir.actions.act_window',
            'name': _('CRM Mail Layout'),
            'view_mode': 'form',
            'res_id': layout.id,
            'res_model': 'ir.ui.view',
        }
