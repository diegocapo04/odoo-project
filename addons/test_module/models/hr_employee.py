from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    hr_note = fields.Char(string="Note sui progetti")

    task_ids = fields.Many2many(
        "project.task",
        "task_employee_rel"
        "employee_id",
        "task_id",
        string = "Task assegnate"
    )