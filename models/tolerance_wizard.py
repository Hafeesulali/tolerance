from odoo import models


class WizardTolerance(models.TransientModel):
    _name = "wizard.tolerance"
    _description = "Wizard Tolerance"

    def action_confirm(self):
        self.env['stock.picking'].browse(self.env.context['active_ids']). \
            write({'state': 'done'})

    def action_reject(self):
        self.env["stock.picking"].browse(self.env.context['active_ids']). \
            write({'state': 'confirmed'})
