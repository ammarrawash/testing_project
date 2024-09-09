from odoo import api, fields, models, _


class Authorised_Signatory_CR(models.Model):
    _name = 'authorised.signatory.cr'
    _description = "name"

    partner_id = fields.Many2one('res.partner', "Name")
    name = fields.Char("Name")
    email = fields.Char("Email")
    mobile = fields.Char("Mobile")
    extension = fields.Char("Extension")
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    passport_no = fields.Char("Passport Number")
    qid_no = fields.Char("QID No")
    nationality_id = fields.Many2one('res.country', "Nationality")
    authority_level = fields.Char("Authority Level")
