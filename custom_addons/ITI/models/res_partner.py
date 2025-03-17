from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one(
        'iti.patient',  
        string='Related Patient',  

     )
    # @api.constrains('related_patient_id')
    # def _check_unique_patient(self):
    #     for record in self:
    #         if record.related_patient_id:
    #             existing = self.search([
    #                 ('related_patient_id', '=', record.related_patient_id.id),
    #                 ('id', '!=', record.id)  
    #             ])
    #             if existing:
    #                 raise ValidationError("This patient is already assigned to another partner!")
    
    # @api.constrains("related_patient_id", "email")
    # def _check_patient_email(self):
    #     for record in self:
    #         if record.related_patient_id and record.email:
    #             other_partners = self.search(
    #                 [
    #                     ("id", "!=", record.id),
    #                     ("email", "=", record.email),
    #                     ("related_patient_id", "!=", False),
    #                 ]
    #             )

    #             if other_partners:
    #                 raise ValidationError(
    #                     "This email is already used by another customer with a linked patient!")



    from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    related_patient_id = fields.Many2one(
        'iti.patient',  
        string='Related Patient',  
    )

    @api.constrains("related_patient_id", "email")
    def _check_patient_constraints(self):
        for record in self:
            if record.related_patient_id:
                existing_patient = self.search([
                    ('related_patient_id', '=', record.related_patient_id.id),
                    ('id', '!=', record.id)  
                ])
                if existing_patient:
                    raise ValidationError("This patient is already assigned to another partner!")

            if record.email:
                existing_email = self.search([
                    ('email', '=', record.email),
                    ('id', '!=', record.id),
                    ('related_patient_id', '!=', False)
                ])
                if existing_email:
                    raise ValidationError("This email is already used by another customer with a linked patient!")

                

    @api.constrains("vat", "is_company")
    def _check_vat_for_crm_customers(self):
        for record in self:
            if record.is_company and not record.vat:
                raise ValidationError(" VAT is required for companies")