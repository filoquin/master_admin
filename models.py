# -*- coding: utf-8 -*-

from openerp import models, fields, api


class master_admin(models.TransientModel):
    _name = 'master.admin'

    @api.one
    def invalidate_all(self):
        self.env.clear()
