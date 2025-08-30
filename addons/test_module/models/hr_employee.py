from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    x_custom_note = fields.Char(string="Nota Personalizzata1")

    task_ids = fields.One2many(
        "project.task",
        "employee_id",
        string = "Task assegnate"
    )