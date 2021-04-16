from odoo import fields, models, api

class MethodPay(models.Model):
    _name = 'method.pay.sh'

    name = fields.Char('Nombre')
