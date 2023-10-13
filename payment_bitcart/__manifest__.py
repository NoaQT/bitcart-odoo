{
    "name": "Bitcart Payments",
    "version": "1.0.2",
    "author": "Bitcart",
    "category": "Accounting/Payment Providers",
    "summary": "Self-hosted, open-source cryptocurrency payment processor and developer solutions",
    "website": "https://bitcart.ai",
    "depends": ["payment"],
    "data": [
        "views/payment_bitcart_templates.xml",
        "views/payment_acquirer_views.xml",
        "views/payment_transaction_views.xml",
        "data/payment_acquirer_data.xml",
    ],
    "images": ["static/description/banner.png"],
    "application": True,
    "uninstall_hook": "uninstall_hook",
    "license": "LGPL-3",
}
