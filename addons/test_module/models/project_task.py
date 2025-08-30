from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    x_custom_note = fields.Char(string="Nota Personalizzata0")

    employee_id = fields.Many2one(
        "hr.employee",
        string = "Assegnato a Dipendente"
    )