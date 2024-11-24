from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SafTargetManagement(models.Model):
    _name = 'sfa.target.definition'

    target_name = fields.Char(string='Target Name', required=True)
    salesman_id = fields.Many2one('res.partner', string='Salesman')
    target_type = fields.Many2one('sfa.target.type', string='Target Type')
    period = fields.Char(readonly=True)
    line_ids = fields.One2many('sfa.target.definition.line', 'sfa_target', string='Lines')
    branch_id = fields.Many2one(
        'res.company', default=lambda self: self.env.company, required=True,
        domain="[('id', 'in', allowed_company_ids)]")


    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')

    @api.constrains('date_from', 'date_to')
    def _check_dates(self):
        for record in self:
            if record.date_from and record.date_to:
                if record.date_from > record.date_to:
                    raise ValidationError("Date From cannot be after Date To.")


class ProjectLine(models.Model):
    _name = 'sfa.target.definition.line'

    sfa_target = fields.Many2one('sfa.target.definition', string='Sfa Target')
    product_category_id = fields.Many2one('product.category', string='Product Category')
    product = fields.Many2one('product.product',string='Product')
    customer = fields.Many2one('res.partner', string='Customer')
    target = fields.Integer(string='Target')

    level_of_assignment_line = fields.Selection(
        [('product', 'Product'),
         ('product_category', 'Product Category'),
         ('none', 'None'),
         ],
        related='sfa_target.target_type.level_of_assignment', invisible=True

    )
    customer_base=fields.Boolean(string='Customer Base',  related='sfa_target.target_type.customer_base')


