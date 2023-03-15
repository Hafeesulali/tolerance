from odoo import models, fields


class PurchaseTolerance(models.Model):
    _inherit = "purchase.order.line"

    po_tolerance = fields.Float(string="Tolerance",
                                related="order_id.partner_id.tolerance")