# -*- coding: utf-8 -*-
from odoo import models, fields


class Project(models.Model):
    _inherit = 'project.project'

    deparment = fields.Char(
        string='DEPARTMENT',
    )
