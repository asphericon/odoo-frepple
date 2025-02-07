# -*- coding: utf-8 -*-
{
    "name": "frepple data",
    "summary": "Test data for frepple",
    "description": "This addon loads test and demo data for frepple in odoo.",
    "author": "frePPLe",
    "license": "Other OSI approved licence",
    "category": "Uncategorized",
    "version": "15.0.0",
    "depends": ["mrp_subcontracting"],
    "data": [
        "data/product.template.csv",
        "data/mrp.workcenter.csv",
        "data/mrp.bom.csv",
        "data/mrp.production.xml",
        "data/sale.order.xml",
        "data/purchase.order.xml",
        "data/stock.warehouse.orderpoint.csv",
        "data/product.supplierinfo.xml",
        "data/config.xml",
    ],
    "autoinstall": False,
    "installable": True,
    "price": 0,
    "currency": "EUR",
    "images": ["static/description/images/freppledata.png"],
}
