from odoo import fields, models, api

class Partner(models.Model):
    _inherit = 'res.partner'

    is_seller = fields.Boolean(string='Es Vendedor')
    code_seller = fields.Char(string='Cod Vendedor')