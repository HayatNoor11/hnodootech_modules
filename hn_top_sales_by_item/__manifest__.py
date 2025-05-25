# -*- coding: utf-8 -*-
{
    'name': "Hn Top Selling Items of the Month",
    'summary': "Sales - Top Selling Items of the Month",
    'description': """
This module allows you to generate a PDF report of the top-selling products for the current month in Odoo Sales. 
You can specify the number of top products to include in the report using a wizard.

Key Features:
- Monthly top-selling product report
- Wizard to input number of items
- Exportable PDF format
- Quick insight for sales performance

Ideal for sales analysis, product trend tracking, and inventory planning.

License: LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html)
    """,
    'author': "HnOdooTech",
    'website': "https://hnodootech.odoo.com",
    'support': 'hayatnoor030@gmail.com',
    'version': '17.0.1.0',
    'license': 'LGPL-3',
    'category': 'Sales/Sales',
    'images': ['static/description/image.jpg'],
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'report/hn_top_sale_item_report.xml',
        'wizard/hn_top_sales_items.xml',
        'views/hn_top_sale_report.xml',
    ],
    'installable': True,
    'application': False,
}
