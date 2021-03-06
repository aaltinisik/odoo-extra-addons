# -*- coding: utf-8 -*-
# Copyright© 2017 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)


import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)

class ProductProduct(models.Model):
    _inherit = "product.product"

    main_category = fields.Many2one(
        comodel_name='product.category',
        string="Top Level Category",
        related="product_tmpl_id.main_category",
        store=True
    )
    second_category = fields.Many2one(
        comodel_name='product.category',
        string="2nd Level Category",
        related="product_tmpl_id.second_category",
        store=True
    )
    third_category = fields.Many2one(
        comodel_name='product.category',
        string="Third Level Category",
        related="product_tmpl_id.third_category",
        store=True
    )