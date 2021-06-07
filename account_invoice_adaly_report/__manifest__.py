# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Adaly Invoice Report",
    "summary": """
        Create a custom invoice PDF report""",
    "author": "Calyx Servicios S.A.",
    "maintainers": ["JhoneM"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Invoice",
    "version": "11.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    "depends": ["account"],
    "data": [
        "views/account_invoice_view.xml",
        "report/account_invoice_custom_report.xml",
        "report/account_invoice_report_template.xml",
    ],
}
