# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from odoo.exceptions import AccessDenied, UserError, ValidationError
from odoo.tools.misc import formatLang, format_date, get_lang
import datetime

class SaleOrderExt(models.Model):
    _inherit = "sale.order"

    method_pay = fields.Many2one('method.pay.sh', string="Metodo de Pago")

    def put_spaces(self):
        param = self.env['ir.config_parameter'].sudo().search([('key', '=', "sh-001")], limit=1)
        banks = self.env['account.journal'].search([])
        if param:
            num = int(param.value)
        else:
            num = 19

        return list(range(num-len(self.order_line)-len(banks)))

    def convert_date_letters(self):
        """this method transforms the date to letters"""
        month = [_('January'),_('February'),_('March'),_('April'),_('May'),_('June'),_('July'),_('August'),_('September'),_('October'),_('November'),_('December')]
        date = _('%s the %s the %s') % (datetime.datetime.now().day, month[datetime.datetime.now().month-1], datetime.datetime.now().year)
        day = datetime.datetime.now().day
        month = month[datetime.datetime.now().month-1]
        year = datetime.datetime.now().year
        return [date, day, month, year]

    def _get_amounts_format_report(self):
        """This method return the amounts for report"""
        vals = {
            'amount_untaxed_ext': formatLang(self.env, value=self.amount_untaxed, currency_obj=self.currency_id),
            'amount_tax_ext': formatLang(self.env, value=self.amount_tax, currency_obj=self.currency_id),
            'amount_total_ext': formatLang(self.env, value=self.amount_total, currency_obj=self.currency_id)
        }
        return vals

    def get_days_order(self):
        for line in self:
            if line.date_order and line.commitment_date:
                message = str(abs(line.date_order - line.commitment_date).days) + " Días"
                return message
            else:
                return ""

class SaleOrderLineExt(models.Model):
    _inherit = "sale.order.line"

    sequence_cont = fields.Integer(string='Sequence', compute="_get_sequence_cont")

    def _get_sequence_cont(self):
        lines = self.env['sale.order.line'].search([('order_id', '=', self.order_id.id)])
        count = 1
        for line in lines:
            line.sequence_cont = count
            count += 1


    def get_formar_amount(self, amount):
        return formatLang(self.env, value=amount)
