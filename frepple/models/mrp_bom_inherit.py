# -*- coding: utf-8 -*-

from odoo import models, fields


class BomInherit(models.Model):
    _inherit = "mrp.bom"

    product_qty_maximum = fields.Float(
        'Maximum Quantity',
        digits='Unit of Measure',
        help="This should be the highest quantity that this product can be produced in.")
