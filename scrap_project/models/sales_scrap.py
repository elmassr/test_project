from odoo import models, fields, api


class ProjectOsama(models.Model):
    _name = 'sales.scrap'

    name = fields.Char(string='Name')
    request_date = fields.Date(string='Requset Data')
    product_categories = fields.Char(string='Product Categories')
    source_location = fields.Char(string='Source Location')
    sales_price = fields.Float(string='Sales Price')
    note = fields.Char(string='Note')
    starting_price = fields.Float(string='Starting Price')
    sales_method = fields.Float(string='Sales Method')
    attachment = fields.Char(string='Attachment')
    sale_order = fields.Integer(string='Sale order')

    line_ids = fields.One2many('sales.scrap.line', 'product_id', string='Lines')


    state = fields.Selection([
    ('draft', 'Draft'),
    ('submit', 'Submitted'),
    ('confirm', 'Confirmed'),
    ('transfer_done', 'Transfer Done'),
    ('sale_done', 'Sale_Done'),
    ('rejected', 'Rejected'),
    ('canceled', 'Canceled'),
        ], default='draft')


class ProjectLine(models.Model):
    _name = 'sales.scrap.line'

    product_id = fields.Many2one('sales.scrap', string='Product')
    seq = fields.Integer(string='Seq')
    partner = fields.Char(string='Partner')
    offer = fields.Integer(string='Offer')

