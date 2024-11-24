# __manifest__.py
{
    'name': 'SFA Journey',
    'version': '17.0',
    'author': 'mohamed ',
    'category': 'Sales',
    'depends': ['base', 'hr', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sfa_journey_views.xml',
        'views/sfa_journey_plan_views.xml',
        'views/sfa_journey_assignment_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
