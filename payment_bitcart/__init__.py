from odoo.addons.payment import reset_payment_acquirer

from . import controllers, models  # noqa: F401


def uninstall_hook(cr, registry):
    reset_payment_acquirer(cr, registry, 'bitcart')
