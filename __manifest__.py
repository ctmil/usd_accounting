# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'usd_accounting',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Contabilidad bimonetaria',
    'depends': ['web','product','account'],
    'data': [
        #'security/ir.model.access.csv',
        #'data/data.xml',
        'account_view.xml',
        ],
    'demo': [
        ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
