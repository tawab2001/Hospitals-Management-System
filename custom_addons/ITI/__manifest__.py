{
    'name': 'Hospital Management System',
    'version': '1.0',
    'category': 'Healthcare',
    'summary': 'Manage hospital departments, doctors, and patients',
    'description': 'Module to manage hospital departments, doctors, and patients.',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base', 'contacts','web', 'crm'],
    'data': [
        'security/security.xml',
        "security/ir.model.access.csv",
        'views/department_views.xml',
        'views/doctor_views.xml',
        'views/res_partner_views.xml',
        'views/patient_views.xml',
        'views/menu_views.xml',
        "reports/iti_patient_report.xml",
    ],
  
    'installable': True,
    'application': True,
}