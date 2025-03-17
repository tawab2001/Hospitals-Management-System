from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class PatientLog(models.Model):
    _name = "iti.patient.log"
    _description = "Patient Log History"



    patient_id = fields.Many2one(
        "iti.patient", string="Patient", required=True, ondelete="cascade"
    )
    date = fields.Datetime(
        string="Date", default=lambda self: fields.Datetime.now(), readonly=True
    )
    description = fields.Text(string="Description", required=True)

class Patient(models.Model):
    _name = "iti.patient"
    _description = "ITI Patient"

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    birthdate = fields.Date(string="Birth Date")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    history = fields.Html(string="History")
    cr_ratio = fields.Float(string="CR Ratio")
    pcr = fields.Boolean(string="PCR")
    image = fields.Image(string="Image", attachment=True)
    address = fields.Text(string="Address")
    email = fields.Char(string="Email", required=True)
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], string="State", default="undetermined")
    # department_id = fields.Many2one("iti.department", string="Department")
    department_id = fields.Many2one(
    "iti.department", 
    string="Department", 
    domain=[("is_opened", "=", True)]
)
    doctor_ids = fields.Many2many("iti.doctor", string="Doctors")
    department_capacity = fields.Integer(string="Department Capacity", related="department_id.capacity", readonly=True)
    # related_patient_id = fields.Many2one('iti.patient', string='Related Patient')
    # customer_ids = fields.One2many(
    #     "res.partner", "related_patient_id", string="Related Customers"
    # )
    
    

    log_history_ids = fields.One2many(
        "iti.patient.log", "patient_id", string="Log History"
    )

    @api.depends('birthdate')
    def _compute_age(self):
        for record in self:
            if record.birthdate:
                today = fields.Date.today()
                record.age = today.year - record.birthdate.year - ((today.month, today.day) < (record.birthdate.month, record.birthdate.day))
            else:
                record.age = 0

    @api.onchange('birthdate')
    def _onchange_birthdate(self):
        for record in self:
            if record.birthdate:
                today = fields.Date.today()
                age = today.year - record.birthdate.year - ((today.month, today.day) < (record.birthdate.month, record.birthdate.day))
                if age < 30:
                    record.pcr = True
                    return {
                        'warning': {
                            'title': 'PCR Checked',
                            'message': 'PCR has been automatically checked because age is lower than 30.'
                        }
                    }

    @api.onchange('pcr')
    def _onchange_pcr(self):
        if self.pcr:
            self.cr_ratio = 0.0  

    @api.constrains('email')
    def _check_email(self):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        for record in self:
            if not re.match(email_regex, record.email):
                raise ValidationError("Invalid email address.")
            if self.search([('email', '=', record.email), ('id', '!=', record.id)]):
                raise ValidationError("Email address must be unique.")

    @api.onchange("state")
    def _onchange_state(self):

        if self.state:

            return {
                "warning": {
                    "title": "State Changed",
                    "message": f"State will be changed to {self.state}",
                }
            }
    # def write(self, vals):
    #     res = super(Patient, self).write(vals)
    #     if 'state' in vals:
    #         self.env["iti.patient.log"].create({
    #         "patient_id": self.id,
    #         "description": f"State changed to {self.state}"
    #      })
    #     return res
    def write(self, vals):
     if 'state' in vals:
        old_state = self.state  # حفظ القيمة القديمة قبل التحديث
    
     res = super(Patient, self).write(vals)
    
     if 'state' in vals:
        self.env["iti.patient.log"].create({
            "patient_id": self.id,
            "description": f"State changed from {old_state} to {self.state}"
        })
     return res
    
    @api.depends("first_name", "last_name")
    def _compute_name(self):
        for rec in self:
            rec.name = (
                f"{rec.first_name} {rec.last_name}"
                if rec.first_name and rec.last_name
                else "New Patient"
            )