# -*- coding: utf-8 -*-
from odoo import models, fields, api


class test_module(models.Model):
    _name = 'test.model'
    _description = "Test Model"

    name = fields.Char(required=True)
    start_date = fields.Date()
    end_date = fields.Date()
    duration = fields.Float(compute='_value_pc')
    tester = fields.Many2one(comodel_name='res.partner')

    @api.depends('start_date', 'end_date')
    def _value_pc(self):
        for record in self:
            if record.end_date and record.start_date:
                record.duration = (record.end_date - record.start_date).days
            else:
                record.duration = 0
