# -*- coding: utf-8 -*-
from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = "product.product"

    product_uom_qty = fields.Float('Order Qty', default=1)

    def add_to_so(self):
        print(self._context,"mennnnu")
        active_id = self._context.get('current_id')
        for rec in self:
            self.env['sale.order.line'].create([
                {'product_id': rec.id,
                 'name': rec.name,
                 'price_unit': rec.lst_price,
                 'product_uom_qty': rec.product_uom_qty,
                 'order_id': active_id}])

    def add_to_po(self):
        print('puchase')
        active_id = self._context.get('current_id')
        for rec in self:
            self.env['purchase.order.line'].create([
                {'product_id': rec.id,
                 'name': rec.name,
                 'price_unit': rec.lst_price,
                 'product_uom_qty': rec.product_uom_qty,
                 'order_id': active_id}])
