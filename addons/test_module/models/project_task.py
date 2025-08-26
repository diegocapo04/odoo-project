from odoo import models, fields

class ProjectTask(models.Model):
    _inherit = 'project.task'

    x_custom_note = fields.Char(string="Nota Personalizzata")