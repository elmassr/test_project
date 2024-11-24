from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'



    supplier = fields.Many2one('res.partner', string="supplier", required=True)
    vendor=fields.Boolean(string='Vendor')

