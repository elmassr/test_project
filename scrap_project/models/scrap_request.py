from odoo import models, fields, api


class ProjectOsama(models.Model):
    _name = 'scrap.request'
#
    name = fields.Char(string='Name')
    employee_id = fields.Many2one('hr.employee' ,string='Employee')
#

    request_info = fields.Char(string='Request Info')
    request_by_id = fields.Many2one('res.users' ,string='Request By')
    office = fields.Char(string='Office')
    department_id = fields.Many2one('hr.department',string='Department')
    general_info = fields.Char(string='General')
    request_date = fields.Date(string='Request Data', default=fields.Date.context_today)
    operation_type = fields.Char(string='Operation Type')
    additional_info = fields.Char(string='Additional Info')

    scrap_reason = fields.Char(string='Scrap Reason')
    additional_info=fields.Char(string='Additional Info')
    attachments=fields.Binary(string='Attachments')
    form_location=fields.Char(string='Form Location')
    destination_location=fields.Char(string='Destination Location')
    transfer=fields.Char(string='Transfer')
    line_ids = fields.One2many('scrap.request.line', 'product_id', string='Lines')


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
    _name = 'scrap.request.line'

    product_id = fields.Many2one('scrap.request', string='Product')
    quantity = fields.Integer(string='Quantity')
    serial_number = fields.Float(string='Serial Number')

#
#
