# -*- coding: utf-8 -*-

from openerp import api, fields, models, tools, _


class account_invoice(models.Model):
    _name = 'mail.followers.mass.add'

    res_model = fields.Char('Related Doc Model', required=True,
                            default=lambda self: self._context.get('active_model', False))
    res_id = fields.Integer('Related Doc Id', required=True,
                            default=lambda self: self._context.get('active_id', 0))
    mode = fields.Selection(string='Mode',
                            selection=[('add', 'Add'), ('reset', 'Reset')],
                            default='add')
    partner_ids = fields.Many2many(string='Recipients', comodel_name='res.partner')
    email_list = fields.Char('Email Based')
    new_follower_ids = fields.Many2many(
        string='Followers to Add', comodel_name='res.partner',
        compute='_compute_new_follower_ids')

    @api.depends('partner_ids', 'email_list')
    def _compute_new_follower_ids(self):
        addresses = tools.email_split(self.email_list)
        partners = self.env['res.partner'].search([('email', 'in', addresses)])
        partners = partners | self.partner_ids
        self.new_follower_ids = partners.ids

    @api.multi
    def action_update(self):
        if self.mode == 'add':
            doc = self.env[self.res_model].browse(self.res_id)
            doc.message_subscribe(self.new_follower_ids.ids)
        else:
            self.env['mail.followers'].search([('res_model', '=', self.res_model), ('res_id', '=', self.res_id)]).unlink()
        return True
