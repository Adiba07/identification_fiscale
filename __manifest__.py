# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Identification Fiscale',
    'version': '0.1',
    'author': 'Adiba Boufeldja',
    'category': 'Extension de res partner',
    'description': "un module qui va herite de gestion facturation",
    'depends': [
                'account_invoicing'
                ],
    'installable': True,
    'application': True,
    'data': [
             'views/identification_fiscale.xml'
             ],
    'website' :'www.modulen1.com',
    'license' : 'GPL-2',
}
