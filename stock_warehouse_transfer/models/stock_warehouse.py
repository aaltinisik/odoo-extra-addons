# -*- encoding: utf-8 -*-
#
#Created on Apr 12, 2019
#
#@author: dogan
#
from openerp import models, fields, api


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'
    
    transfer_location_id = fields.Many2one('stock.location', string='Transfer Location')