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


class WorkcenterSkill(models.Model):
    _name = "mrp.workcenter.skill"
    _description = "List of workcenter skill associations"
    _rec_name = "skill"

    workcenter = fields.Many2one("mrp.workcenter", "Work Center", required=True)
    skill = fields.Many2one("mrp.skill", "Skill", required=True)
    priority = fields.Integer(
        "priority",
        default=1,
        help="Priority of this workcenter to fulfill requirements for this skill",
    )
    export_to_frepple = fields.Boolean(related="workcenter.export_to_frepple")
    # secondary_skill_ids = fields.One2many(related="workcenter.secondary_skill_ids")
