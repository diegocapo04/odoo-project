{
    'name': 'Test Module',
    'version': '2.0',
    'category': 'Testing',
    'summary': 'Modulo di test per verificare il caricamento degli addons',
    'description': """
        Questo è un modulo di test per verificare che Odoo
        carichi correttamente i moduli dalla cartella addons locale.
    """,
    'author': 'Diego Caporale',
    'depends': ['project','hr'],
    'data': [
        'views/project_task_views.xml',
        'views/hr_employee_views.xml',
            ],
    'installable': True,
    'application': False,
    'auto_install': False,
}