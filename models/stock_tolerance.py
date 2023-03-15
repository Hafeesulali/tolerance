from odoo import models, fields


class StockTolerance(models.Model):
    _inherit = "stock.move"
    delivery_tolerance = fields.Float(string="Tolerance",
                                      related="sale_line_id.so_tolerance")


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        for line in self.move_ids:
            maximum_quantity = line.product_uom_qty + line.delivery_tolerance
            minimum_quantity = line.product_uom_qty - line.delivery_tolerance
            res = super(StockPicking, self).button_validate()
            if minimum_quantity <= line.quantity_done <= maximum_quantity:
                return res
            else:
                return {
                    'type': 'ir.actions.act_window',
                    'name': 'warning',
                    'view_mode': 'form',
                    'res_model': 'wizard.tolerance',
                    'target': 'new'
                }
