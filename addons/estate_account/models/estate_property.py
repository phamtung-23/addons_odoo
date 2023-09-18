# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.\

from odoo import fields, models, api, exceptions

class EstateProperty(models.Model):
    _inherit = "estate.model"

    def sold_action(self):
        res = super(EstateProperty, self).sold_action()

        # Create an empty customer invoice
        invoice = self.env['account.move'].create({
            'partner_id': self.buyer_id.id,
            'move_type': 'out_invoice',
        })

        # Calculate invoice lines
        selling_price = self.selling_price
        administrative_fees = 100.00
        line_vals = [
            {
                'name': 'Property Sale - 6% of Selling Price',
                'quantity': 1,
                'price_unit': selling_price * 0.06,
            },
            {
                'name': 'Administrative Fees',
                'quantity': 1,
                'price_unit': administrative_fees,
            }
        ]
 
        # Create invoice lines
        invoice_line_ids = []
        for line_val in line_vals:
            line = self.env['account.move.line'].create({
                'move_id': invoice.id,
                'name': line_val['name'],
                'quantity': line_val['quantity'],
                'price_unit': line_val['price_unit'],
            })
            invoice_line_ids.append(line.id)

        # Update invoice with lines
        invoice.write({'invoice_line_ids': [(6, 0, invoice_line_ids)]})
        return res