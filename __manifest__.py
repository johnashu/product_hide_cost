{
    "name": "Hide Product Cost",
    "summary": "Hide cost price field from all users. Cost price remains visible to admin users and users with Purchase or Accounting access.",
    "version": "17.0.0.0.0",
    "category": "Sales/Sales",
    "author": "SJR Nebula - John Ashurst",
    "website": "https://sjr.ie",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "product",
        "purchase",
        "account",
    ],
    "data": [
        "views/product_views.xml",
    ],
    "images": ["static/description/icon.png"],
}
