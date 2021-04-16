# -*- coding: utf-8 -*-
{
    'name': "Sale Order Report Modified",

    'description': """Reports for Sale""",

    'author': "Soluciones Softhard, C.A.",
    'website': "http://www.solucionesofthard.com",
    'installable': True,
    'depends': ['base', 'sale', 'sale_stock'],
    'data': [
        'reports/report_sale_order.xml',
        'views/partner_view_form_ext.xml',
        'views/account_journal_ext.xml',
        'views/sale_order_ext.xml',
        'data/data_sale_order.xml',
        'security/ir.model.access.csv'
    ],
}
