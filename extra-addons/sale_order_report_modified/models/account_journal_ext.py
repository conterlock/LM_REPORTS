# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from odoo.exceptions import AccessDenied, UserError, ValidationError
from odoo.tools.misc import formatLang, format_date, get_lang
import datetime

class AccountJournalExt(models.Model):
    _inherit = "account.journal"

    cci = fields.Char('CCI')

class SetupBarBankConfigWizard(models.TransientModel):
    _inherit = 'account.setup.bank.manual.config'

    cci = fields.Char('CCI', default=lambda self: self.linked_journal_id.cci)

    def set_linked_journal_id(self):
        """ Called when saving the wizard.
        """
        for record in self:
            selected_journal = record.linked_journal_id
            if record.num_journals_without_account == 0:
                company = self.env.company
                selected_journal = self.env['account.journal'].create({
                    'name': record.new_journal_name,
                    'code': record.new_journal_code,
                    'type': 'bank',
                    'company_id': company.id,
                    'cci': record.cci,
                    'bank_account_id': record.res_partner_bank_id.id,
                })
            else:
                selected_journal.bank_account_id = record.res_partner_bank_id.id
                selected_journal.name = record.new_journal_name
                selected_journal.code = record.new_journal_code
                selected_journal.cci = record.cci

    @api.depends('journal_id')  # Despite its name, journal_id is actually a One2many field
    def _compute_linked_journal_id(self):
        for record in self:
            record.linked_journal_id = record.journal_id and record.journal_id[0] or record.default_linked_journal_id()
            record.linked_journal_id.cci = record.cci
