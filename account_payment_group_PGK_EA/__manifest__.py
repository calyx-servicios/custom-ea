# pylint: disable=missing-module-docstring,pointless-statement
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Account Payment Group PGK EA",
    "summary": """
        This module extends functionalities for account_payment_group.
        New field to filter customer receipts with no matched documents in payments.
    """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["<Github Username/s>"],
    "website": "https://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Accounting",
    "version": "11.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "post_init_hook": 'post_init_hook',
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    # any module necessary for this one to work correctly
    "depends": ["account_payment_group"],
    'data': [
         'views/account_payment_group_view.xml',
    ]
}
