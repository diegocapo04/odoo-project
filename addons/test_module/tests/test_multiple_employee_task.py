from odoo.tests.common import TransactionCase

class TestMultipleTask(TransactionCase):
    def test_multiple_employee_task(self):
        employee = self.env['hr.employee'].create({'name':'Oggetto ProvaY'})
        task1 = self.env['project.task'].create({
            'name': 'Task 1',
            'employee_ids': [(6, 0, [employee.id])]
        })
        task2 = self.env['project.task'].create({
            'name': 'Task 2',
            'employee_ids': [(6, 0, [employee.id])]
        })
        self.assertEqual(len(employee.task_ids, 2))
        self.assertSetEqual(set(employee.task_ids.ids), {task1.id, task2.id})