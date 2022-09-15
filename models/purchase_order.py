# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "purchase.order"

    def multiple_products(self):
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'view_id': self.env.ref('multiple_product_orderline.view_product_purchase_multiple_product_list').id,
            'res_model': 'product.product',
            'context': "{'create': False}",
        }