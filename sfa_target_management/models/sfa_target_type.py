from odoo import models, fields, api


class SafTargetType(models.Model):
    _name = 'sfa.target.type'


    name=fields.Char(required=True)
    level_of_assignment = fields.Selection(
        [('product', 'Product'),
         ('product_category','Product Category'),
         ('none', 'None'),
         ],

    )
    target_point = fields.Selection(
        [('so_confirm', 'So Confirm'),
         ('invoice_validation', 'Invoice Validation'),
         ('payment', 'Payment'),
         ('delivery_validation','Delivery Validation')
         ],

    )
    target_on = fields.Selection(
        [('amount', 'Amount'),
         ('quantity', 'Quantity'),
         ('count', 'Count'),
         ],

    )
    customer_base=fields.Boolean(string='Customer Base')

    branch_id = fields.Many2one(
        'res.company', default=lambda self: self.env.company, required=True,
        domain="[('id', 'in', allowed_company_ids)]")
