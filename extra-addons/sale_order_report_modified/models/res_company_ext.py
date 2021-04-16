# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from odoo.exceptions import AccessDenied, UserError, ValidationError
from odoo.tools.misc import formatLang, format_date, get_lang
import datetime

class CompanyExt(models.Model):
    _inherit = "res.company"

    @api.model
    def display_address_ext(self):
        address = ""
        if self.street:
            address = str(self.street)
        if self.street2:
            address += " con " + self.street2

        address += ", " + self.city + ", " + self.state_id.name + ", " + self.country_id.name

        return address