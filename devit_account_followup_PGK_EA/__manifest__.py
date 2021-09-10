# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Payment Follow-up Management PGK",
    "summary": """
        Payment Follow-Up / Send Email and letters""",
    "author": "Calyx Servicios S.A.",
    "maintainers": ["AndresAndrade"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    "category": "Technical Settings",
    "version": "11.0.1.0.0",
    'depends': ['devit_account_followup'],
    'data': [
        'data/account_followup_data.xml',
    ],
    'demo': ['demo/account_followup_demo.xml'],
    'images': [
    ],
    'installable': True,
    'auto_install': False,
}
