=================
Hide Product Cost
=================

.. |badge1| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

|badge1|

This module hides the Cost Price (standard_price) field on product forms
from all users. The cost price remains visible to admin users and
users with Purchase or Accounting access.

**Table of contents**

.. contents::
   :local:

Installation
============

1. Copy the ``product_hide_cost`` folder to your Odoo addons directory.
2. Update the apps list in Odoo (Settings > Apps > Update Apps List).
3. Search for "Hide Product Cost" and install it.

Configuration
=============

No configuration is required. Once installed, the module automatically hides
the cost price field from users who do not belong to either:

- Purchase / User (``purchase.group_purchase_user``)
- Invoicing / Accountant (``account.group_account_user``)

Usage
=====

After installation, the cost price field will be hidden on:

- Product Template form view
- Product Variant form view

Users with Purchase or Accounting access will continue to see the cost price
as normal.

Features
========

- **Automatic hiding**: No manual configuration needed
- **Group-based access**: Uses Odoo's built-in security groups
- **Covers both views**: Hides cost on both product.template and product.product forms

Support
=======

For support, please contact SJR Nebula:

- Website: https://sjr.ie
- Email: info@sjr.ie

Credits
=======

Authors
-------

* SJR Nebula

Contributors
------------

* John Ashurst
