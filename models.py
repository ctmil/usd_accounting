from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import datetime

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        res = super(AccountMove, self).action_post()
        for rec in self:
            currency_usd = self.env['res.currency'].search([('name','=','USD')])
            if not currency_usd:
                raise ValdationError('No esta definida la moneda USD en el sistema')
            currency_rate = currency_usd._convert(1, rec.company_id.currency_id, rec.company_id, rec.date)
            for line in rec.line_ids:
                line.rate_usd = currency_rate
                line.debit_usd = line.debit / currency_rate
                line.credit_usd = line.credit / currency_rate
        return res

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    def _compute_balance_usd(self):
        for rec in self:
            rec.balance_usd = rec.debit_usd - rec.credit_usd

    debit_usd = fields.Float('Debito USD')
    credit_usd = fields.Float('Debito USD')
    balance_usd = fields.Float('Saldo USD',compute=_compute_balance_usd)
    rate_usd = fields.Float('Tipo de cambio')


