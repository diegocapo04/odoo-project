from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    project_note = fields.Char(string="Note del team")

    employee_ids = fields.Many2many(
        "hr.employee",
        "task_employee_rel",
        "task_id",
        "employee_id",
        string = "Assegnato a Dipendente"
    )