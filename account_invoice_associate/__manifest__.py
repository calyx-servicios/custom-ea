# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Account invoice Associate',
    'summary': """
        This module modifies the user_id field's behaviour and name """,

    'author': 'Calyx Servicios S.A., Odoo Community Association (OCA)',
    'maintainers': ['marcooegg'],

    'website': 'http://odoo.calyx-cloud.com.ar/',
    'license': 'AGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'invoicing',
    'version': '11.0.1.0.0',
    # see https://odoo-community.org/page/development-status
    'development_status': 'Production/Stable',

    'application': False,
    'installable': True,
    'external_dependencies': {
        'python': [],
        'bin': [],
    },

    # any module necessary for this one to work correctly
    'depends': ['account_invoicing'],


     'data': [
         'views/account_invoice_view.xml',
         'views/partner_view.xml',
     ],

}
