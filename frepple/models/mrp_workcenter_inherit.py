# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 by frePPLe bv
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from odoo import models, fields


class WorkcenterInherit(models.Model):
    _inherit = "mrp.workcenter"

    owner = fields.Many2one(
        "mrp.workcenter",
        "Owner",
        required=False,
        help="Groups workcenters together in groups",
    )
    tool = fields.Boolean(
        "is a tool",
        default=False,
        help="Mark workcenters that are tools, fixtures or holders. The same tool needs to accompany a manufacturing order through all its work orders.",
    )
    workcenter_skill_ids = fields.One2many(
        "mrp.workcenter.skill",
        "workcenter",
        string="Skills",
        help="Skills the work center has",
        
    )
    export_to_frepple = fields.Boolean(
        "Export to frePPLe",
        default=False,
        help="Mark workcenters to export them into frePPLe for planning.",
    )
    is_frepple_constrained = fields.Boolean(
        "Constrained in frePPLe",
        default=False,
        tracking=True,
        help="Mark workcenters to be constrained in frePPLe.",
    )
