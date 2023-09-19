from odoo import models, fields, api

class ShopModel(models.Model):
    _name = 'shop.managerment'
    _description = 'Shop Managerment'
    
    name = fields.Char(string='Shop Name', required=True)
    code = fields.Char(string='Shop Code', required=True)
    shop_type_id = fields.Many2one('shop.type.managerment', string='Shop Type', required=True)
    parent_region_id = fields.Many2one('parent.regions.managerment', string='Parent Region')
    region_id = fields.Many2one('regions.managerment', string='Region', domain="[('parent_regions_id', '=', parent_region_id)]")
    city_id = fields.Many2one('city.managerment', string='City', domain="[('regions_id', '=', region_id)]")
    district_id = fields.Many2one('district.managerment', string='District', domain="[('city_id', '=', city_id)]")

    address = fields.Char(string='Address')
    latitude = fields.Float(string='Latitude')
    longitude = fields.Float(string='Longitude')
    channel_id = fields.Many2one('channel.managerment', string='Channel')
    status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')],
        string='Status', default='active', required=True)

    @api.onchange('parent_region_id')
    def _onchange_parent_region(self):
      self.region_id = False
      self.district_id = False 
      self.city_id = False

    @api.onchange('region_id')
    def _onchange_region(self):
      self.district_id = False
      self.city_id = False

    @api.onchange('city_id') 
    def _onchange_district(self):
      self.district_id = False