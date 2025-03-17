from odoo import models, fields

class Doctor(models.Model):
    _name = 'iti.doctor'
    _description = 'Doctor'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    image = fields.Binary(string='Image')
    department_id = fields.Many2one('iti.department', string='Department')