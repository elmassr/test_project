from email.policy import default

from odoo import models, fields, api
import time
from odoo.tests import users



class ProjectOsama(models.Model):
    _name = 'project.osama'
    _description = 'Project Osama'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Project Name')
    project_id = fields.Many2one('project.project', string='Related Project')
    task_id = fields.Many2one('project.task', string='Related Task')
    date_from = fields.Date(string='Start Date', tracking=True)
    date_to = fields.Date(string='End Date', tracking=True)
    duration_date = fields.Integer(string='Duration', compute='_compute_duration_date')
    confirm_time = fields.Datetime('Confirm Time')
    elapsed_time = fields.Float('Elapsed Time (seconds)', compute='_compute_elapsed_time')
    line_ids = fields.One2many('project.osama.line', 'product_id', string='Lines')
    create_time = fields.Datetime(default=fields.Datetime.now())
    time_spent = fields.Char(string='Time Spent')
    start_time = fields.Float(string='Start Time', default=0.0)
    end_time = fields.Float(string='End Time', default=0.0)
    date_start = fields.Datetime(string='Start Date', required=True)
    date_end = fields.Datetime(string='End Date', required=True)
    date_stop = fields.Datetime(string='End Date', required=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], default='draft')

    def action_draft(self):
        self.state = 'draft'

    def action_confirm(self):
        self.state = 'confirm'
        self.confirm_time = fields.Datetime.now()
        self.start_time = self._get_current_time()

    def action_in_progress(self):
        self.end_time = self._get_current_time()
        time_difference = self.end_time - self.start_time
        self.time_spent = f"{time_difference} seconds"
        self.state = 'in_progress'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'

    def _get_current_time(self):
        return time.time()

    @api.depends('date_from', 'date_to')
    def _compute_duration_date(self):
        for record in self:
            if record.date_from and record.date_to:
                delta = fields.Date.from_string(record.date_to) - fields.Date.from_string(record.date_from)
                record.duration_date = delta.days
            else:
                record.duration_date = 0

    @api.depends('line_ids.total_amount')
    def _compute_elapsed_time(self):
        for record in self:
            if record.confirm_time:
                elapsed = (fields.Datetime.now() - record.confirm_time).total_seconds()
                record.elapsed_time = elapsed
            else:
                record.elapsed_time = 0


class ProjectLine(models.Model):
    _name = 'project.osama.line'

    product_id = fields.Many2one('project.osama', string='Project')
    tax_excl = fields.Float(string='Tax Excluded')
    product = fields.Many2one('product.product')
    description = fields.Char(string='Description')
    quantity = fields.Float(string='Quantity')
    unit_price = fields.Float(string='Unit Price')
    taxes = fields.Many2many('account.tax', string='Taxes')
    price_subtotal = fields.Float(string='Subtotal')
    delivered = fields.Boolean(string='Delivered')
    discount = fields.Float(string='Discount')
    invoiced = fields.Boolean(string='Invoiced')
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)

    def _compute_total_amount(self):
        for line in self:
            line.total_amount = (line.unit_price * line.quantity) * (1 - (line.discount / 100))