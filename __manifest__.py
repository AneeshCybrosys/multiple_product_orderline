# -*- coding: utf-8 -*-
{
    'name': "Select Multiple Products In OrderLine",

    'summary': """
        Helps to select multiple products into the sale and purchase order line """,

    'description': """
        description
    """,

    'author': "Minions 6",

    'version': '15.0.1.0.0',
    'depends': ['sale', 'purchase'],

    'data': [
        'views/sale_order_views.xml',
        'views/purchase_order_views.xml'
    ],
}
