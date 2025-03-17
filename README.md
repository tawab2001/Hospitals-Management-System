#Hospitals Management System

## Overview
ITI (Hospitals Management System) is a module for Odoo that provides functionalities to manage hospitals, patients, doctors, and departments efficiently.

## Features
### 1. Create New Module
- Created a new module called **"ITI"**.

### 2. Patient Model (**iti.patient**)
- First Name (Required)
- Last Name (Required)
- Birthdate
- History (HTML)
- CR Ratio (Float, Mandatory if PCR is checked)
- Blood Type (Dropdown)
- PCR (Checkbox, Auto-checked if Age < 30)
- Image (Upload Image)
- Address (Text)
- Age (Auto-calculated from Birthdate)
- Email (Unique & Validated)

### 3. Department Model (**iti.department**)
- Name
- Capacity (Integer)
- Is Opened (Boolean, Prevents selection of closed departments)
- Patients (One2many to iti.patient)

### 4. Doctor Model (**iti.doctors**)
- First Name
- Last Name
- Image
- Linked to Patients (Many2Many, Readonly until department is selected)

### 5. Additional Functionalities
- Patient states: (Undetermined, Good, Fair, Serious)
  - Each state change logs history with Created By, Date, and Description.
- Prevents users from selecting closed departments.
- Automatically check PCR if the patient's age is below 30 and show a warning message.
- Hide History field if the patient's age is less than 50.
- Link **Patient Model** to **CRM Customers** with a field **related_patient_id** inside the Misc Group.
- Prevent deletion of CRM customers linked to a patient.
- Add constraints to prevent linking a patient to a customer if the email is already used.

### 6. Access Rights & User Groups
#### **User Group**
- Can create/read/update their own patients' records.
- Can only read departments & doctors.
- Cannot view doctors' fields in patients’ form view.
- Cannot view doctors' menu item.

#### **Manager Group**
- Can create/read/update/delete all patient records.
- Can create/read/update/delete departments.
- Can create/read/update/delete doctors.
- Can view doctors' fields in patients' form view.
- Can view doctors' menu item.

### 7. Reporting
- A patient report can be generated with all necessary details.

## How to Install & Use ITI Module in Odoo

### **Installation**
1. Clone or copy the module to your Odoo **addons** directory:
   ```bash
   cd /odoo/custom/addons
   git clone <repository_link>
   ```
2. Restart Odoo server:
   ```bash
   odoo-bin -c /etc/odoo/odoo.conf -u iti
   ```
3. Activate developer mode in Odoo.
4. Navigate to **Apps** → Search for "ITI" → Click "Install".

### **Usage**
1. **Create a Patient**
   - Go to "Hospital Management" → "Patients" → "Create".
   - Fill in the patient details and save.

2. **Manage Departments & Doctors**
   - Navigate to "Departments" or "Doctors" menus to create new entries.

3. **Assign Patients to Departments & Doctors**
   - Open a patient record and select a department (Only open ones can be chosen).
   - Assign doctors (This field is enabled only after selecting a department).

4. **Check Patient History & Logs**
   - Any state change will automatically log an entry under the patient's record.

5. **Generate Reports**
   - Go to "Reporting" and generate patient reports as needed.

---
This module ensures an efficient hospital management system with robust access control, data integrity, and seamless integration with Odoo CRM.

