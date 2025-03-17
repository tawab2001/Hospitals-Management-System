from odoo import models, fields

class Department(models.Model):
    _name = 'iti.department'
    _description = 'Department'

    name = fields.Char(string='Name', required=True)
    capacity = fields.Integer(string='Capacity')
    is_opened = fields.Boolean(string='Is Opened')
    patient_ids = fields.One2many('iti.patient', 'department_id', string='Patients')