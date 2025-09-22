from odoo.tests.common import TransactionCase

class TestModelsRelation(TransactionCase):
    def test_employee_task_relation(self):
        employee = self.env['hr.employee'].create({'name':'Utente ProvaX'})
        task = self.env['project.task'].create({
            'name':'Task Assegnato',
            'employee_ids':[(6,0,employee.id)]
        })
        self.assertIn(employee, task.employee_ids)
        self.assertIn(task, employee.task_ids)