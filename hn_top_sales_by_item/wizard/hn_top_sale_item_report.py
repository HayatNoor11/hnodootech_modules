# -*- coding: utf-8 -*-

from datetime import datetime, date
from dateutil.relativedelta import relativedelta

from odoo import models, fields, api

class TopSaleItem(models.TransientModel):
    _name = 'hn.topsaleitem.report'
    _description = 'HnTopSaleItem'
    
    
    today = date.today()
    first_day = today.replace(day=1)
    last_day = date(today.year,today.month,1)+relativedelta(months=1,days=-1)
    
    start_date = fields.Date(
        'Start Date',
        required = True,
        default=first_day,
    )
    end_date = fields.Date(
        'End Date',
        required = True,
        default=last_day,
    )
    top_sale_value = fields.Integer(
        'No of Products (Top)',
        default = lambda self:('50'),
        required = True,
    )
    
    def top_sale_item(self):
        data = self.sudo().read()[0]
        return self.env.ref('hn_top_sales_by_item.hn_top_sale_report_items').report_action(self, data=data, config=False)   # odoo 11
