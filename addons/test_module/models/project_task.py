from odoo import models, fields, api

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

    @api.onchange("employee_ids")
    def _onchange_employee_ids(self):
        """Sincronizza user_ids ogni volta che aggiungi/rimuovi dipendenti in form view"""
        self.user_ids = [(6, 0, self.employee_ids.mapped("user_id").ids)]

    @api.model
    def create(self, vals):
        res = super().create(vals)
        if res.employee_ids:
            res._sync_users()
        return res

    def write(self, vals):
        result = super().write(vals)
        if "employee_ids" in vals or "stage_id" in vals:
            for task in self:
                task._sync_users()
        return result

    def unlink(self):
        """Prima della cancellazione, svuota i collegamenti anche su user_ids"""
        for task in self:
            task.user_ids = [(5, 0, 0)]  # rimuove tutti gli user
        return super().unlink()

    def _sync_users(self):
        """Metodo centrale per sincronizzare i dipendenti con gli user"""
        self.user_ids = [(6, 0, self.employee_ids.mapped("user_id").ids)]