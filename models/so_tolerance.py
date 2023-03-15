from odoo import models, fields, api


class SaleTolerance(models.Model):
    _inherit = "sale.order.line"

    so_tolerance = fields.Float(string="Tolerance")

    @api.onchange("product_template_id")
    def _onchange_product(self):
        self.so_tolerance = self.order_id.partner_id.tolerance
