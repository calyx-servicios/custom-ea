# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Custom Roles Ea Argentina",
    "summary": """
        New custom groups and permissions \
             in account models for EA Argentina.""",
    "author": "Calyx Servicios S.A.",
    "maintainers": ["JhoneM"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Technical Settings",
    "version": "11.0.1.2.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    "depends": [
        "account_voucher",
        "account_payment_group",
        "account_payment_fix",
        "account_check",
        "account_financial_report",
        "l10n_ar_export_sicore",
        "l10n_ar_account",
        "account_extension",
        "account_lock_date_update",
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "view/account_colletion_manager.xml",
        "view/account_ea_manager.xml",
        "view/billing_payment.xml",
    ],
}
