from odoo import models, fields


class Branch(models.Model):
    _name = 'branch.branch'
    _description = 'Branch'

    name = fields.Char(string='Branch Name', required=True)
    company_id = fields.Many2one('res.company', string='Company',  required=True)







class SaleOrder(models.Model):
    _inherit = 'sale.order'

    branch_id = fields.Many2one( 'branch.branch', string="branch1")


class ResUsers(models.Model):
    _inherit = 'res.users'

    branch = fields.Many2one('branch.branch',string='Branch')


#
#
# class AccountInvoice(models.Model):
#     _inherit = 'account.move'
#
#     branch_id = fields.Many2one('branch', string='Branch')
#
#
# class ProductTemplate(models.Model):
#     _inherit = 'product.template'
#
#     custom_field_1 = fields.Char(string='Custom Field 1')
#     custom_field_2 = fields.Float(string='Custom Field 2')
#
#
# class AccountPayment(models.Model):
#     _inherit = 'account.payment'
#
#     invoice_ids=fields.Char(string="invoice_ids")
#
#     def create(self, vals):
#         payment = super(AccountPayment, self).create(vals)
#
#         if payment.invoice_ids:
#             invoice = payment.invoice_ids.sorted(key=lambda x: x.invoice_date)[0]
#             payment.invoice_ids = [(4, invoice.id)]
#
#         return payment
#
#
#
#
#     def create_groups(self):
#         group_manager = self.env['res.groups'].create({
#             'name': 'Manager',
#             'category_id': self.env.ref('base.module_category_hidden').id,
#         })
#
#         group_user = self.env['res.groups'].create({
#             'name': 'Custom User',
#             'category_id': self.env.ref('base.module_category_hidden').id,
#         })
#
#         self.env['ir.model.access'].create({
#             'name': 'branch_manager_access',
#             'model_id': self.env.ref('branch.model_branch').id,  # استخدم معرف النموذج الصحيح هنا
#             'group_id': group_manager.id,
#             'perm_read': 1,
#             'perm_write': 1,
#             'perm_create': 1,
#             'perm_unlink': 1,
#         })
#
#         self.env['ir.model.access'].create({
#             'name': 'branch_user_access',
#             'model_id': self.env.ref('branch.model_branch').id,  # استخدم معرف النموذج الصحيح هنا
#             'group_id': group_user.id,
#             'perm_read': 1,
#             'perm_write': 0,
#             'perm_create': 0,
#             'perm_unlink': 0,
#         })
#
#     def init(self):
#         self.create_groups()
#
