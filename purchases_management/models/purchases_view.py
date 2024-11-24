from odoo import models, fields, api
from pkg_resources import require


class PurchasesManagement(models.Model):
    _name = 'purchases.management'


    name=fields.Char(required=True)
    country=fields.Char()
    company=fields.Char()
    area=fields.Char()
    neighborhood=fields.Char()
    street=fields.Char()
    building=fields.Float()
    city=fields.Char()
    Postal_code=fields.Char()
    country_state=fields.Char()
    Job_position=fields.Char()
    phone_number=fields.Integer()
    Mobile_phone=fields.Integer()
    e_mail=fields.Char()
    website=fields.Char()
    address=fields.Char()
    language=fields.Char()
    Hashtags=fields.Char()
    Added_value=fields.Integer()
    is_vendor=fields.Char()
    supplier_classification=fields.Char()
    Identity_type=fields.Char()
    Identity_number=fields.Integer( )
    Identity_card=fields.Char()
    purchases=fields.Char()

    level_of_assignment = fields.Selection(
        [('product', 'Product'),
         ('none', 'None'),
         ],
        string="Level",
    )









