from odoo import models, fields


class CustomerTolerance(models.Model):
    _inherit = "res.partner"

    tolerance = fields.Float(string="Tolerance")
