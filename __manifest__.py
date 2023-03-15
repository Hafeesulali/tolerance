{
    'name': 'Tolerance',
    'version': '16.0.1.0.0',
    'depends': ['base', 'sale', 'contacts', 'purchase', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_tolerance_views.xml',
        'views/po_tolerance_views.xml',
        'views/so_tolerance_views.xml',
        'views/stock_tolerance_views.xml',
        'views/tolerance_wizard_views.xml',
    ],
    'installable': True,

}
