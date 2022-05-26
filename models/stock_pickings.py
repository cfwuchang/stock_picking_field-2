
from odoo import api,fields,models,_
class StockPickings(models.Model):
    _inherit = "stock.picking"

    x_origin = fields.Char(string=u"项目号")

    # @api.constrains('scheduled_date')
    # def _get_origin(self):
    #     if self.picking_type_code=='internal':
    #         att_model = self.env['mrp.production']
    #         query = [("state","!=","draft"),("state","!=","cancel"),("state","!=","done")]
    #         for i in att_model.search(query):
    #             if i.name in self.origin:
    #                 # self.x_origin=i.product_id.name
    #                 self.write({'x_origin':i.product_id.name})
    
    @api.onchange('x_origin')
    @api.constrains('scheduled_date')
    def get_origin(self):
        att_model = self.env['mrp.production']
        query = [("state","!=","draft"),("state","!=","cancel"),("state","!=","done")]
        for i in att_model.search(query):
            try:
                if i.name in self.origin:
                    # self.x_origin=i.product_id.name
                    self.write({'x_origin':i.product_id.name})
            except:
                pass