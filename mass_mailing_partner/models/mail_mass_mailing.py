# Copyright 2015 Pedro M. Baeza <pedro.baeza@tecnativa.com>
# Copyright 2015 Antonio Espinosa <antonio.espinosa@tecnativa.com>
# Copyright 2015 Javier Iniesta <javieria@antiun.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class MailMassMailingList(models.Model):
    _inherit = 'mail.mass_mailing.list'

    partner_mandatory = fields.Boolean(string="Mandatory Partner",
                                       default=False)
    partner_category = fields.Many2one(comodel_name='res.partner.category',
                                       string="Partner Tag")
