{
    "name": "Integracion entre modulo delivery y localización argentina",
    "version": "19.0.1.1.1",
    "category": "Localization/Argentina",
    "sequence": 14,
    "author": "ADHOC SA",
    "website": "www.adhoc.com.ar",
    "license": "AGPL-3",
    "depends": ["delivery_ux", "l10n_ar_stock_ux"],
    "data": [
        "views/report_deliveryslip.xml",
    ],
    "demo": [],
    "installable": True,
    # Multi-company: never auto-install database-wide; install explicitly where needed.
    "auto_install": False,
    "application": False,
}
