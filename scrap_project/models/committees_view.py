from odoo import models, fields, api


class ProjectOsama(models.Model):
    _name = 'committees.view'


    name = fields.Char(string='Name Of Committee')
    description=fields.Char(string='Description')


    # line_ids = fields.One2many('committees.view.line', 'product_id', string='Lines')
