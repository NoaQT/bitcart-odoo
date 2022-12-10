# BitcartCC plugin for Odoo

## Integration Requirements

This version requires the following:

* Your Odoo instance
* Running BitcartCC instance: [deployment guide](https://docs.bitcartcc.com/deployment)

## Installing the Plugin

1. Add `payment_bitcartcc` directory to your addons directory (You can take [the latest release](https://github.com/bitcartcc/bitcart-odoo/releases/latest), unzip it and get `payment_bitcartcc` from there)

2. From your Odoo apps page, activate "BitcartCC Payments" app

3. Configure the plugin (see details below)

## Plugin Configuration

After you have enabled the BitcartCC plugin, the configuration steps are:

1. Enter your admin panel URL (for example, https://admin.bitcartcc.com) without slashes. If deployed via configurator, you should use https://bitcart.yourdomain.com/admin
2. Enter your merchants API URL (for example, https://api.bitcartcc.com) without slashes. If deployed via configurator, you should use https://bitcart.yourdomain.com/api
3. Enter your store ID (click on id field in BitcartCC's admin panel to copy id)

Enjoy!
