{
    'name': 'Test Module',
    'version': '1.0',
    'category': 'Testing',
    'summary': 'Modulo di test per verificare il caricamento degli addons',
    'description': """
        Questo è un modulo di test per verificare che Odoo
        carichi correttamente i moduli dalla cartella addons locale.
    """,
    'author': 'Diego Caporale',
    'depends': ['project'],
    'data': ['views/project_task_views.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
}