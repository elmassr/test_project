from odoo import models, fields
from odoo.tests import users


# class ProjectOsamaLine(models.Model):
#     _name = 'project.osama.line'
#     _description = "Project Osama Line"
#
#
#
#     product_uom_qty = fields.Float(string="Qty")
#     product_uom=fields.Float(string='product_uom')
#
# product_uom_qty = fields.Float(
#     string="Quantity",
#     compute='_compute_product_uom_qty',
#     digits='Product Unit of Measure', default=1.0,
#     store=True, readonly=False, required=True, precompute=True)
#
# product_uom = fields.Many2one(
#     comodel_name='uom.uom',
#     string="Unit of Measure",
#     compute='_compute_product_uom',
#     store=True, readonly=False, precompute=True, ondelete='restrict',
#     domain="[('category_id', '=', product_uom_category_id)]")


