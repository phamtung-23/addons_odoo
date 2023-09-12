from odoo import http
from odoo.http import request
import json

class Api(http.Controller):
    @http.route('/api/cources', type='http', auth='none', methods=['GET', 'POST'])
    def test(self, **kw):
        partnerList = request.env['res.partner'].sudo().search([])
        
        partners = []

        for partner in partnerList:
            partners.append({
                'id': partner.id,
                'name': partner.name,
                'email': partner.email  
            })
        return json.dumps(partners)

    @http.route('/api/partner/create', type='json', auth='none', methods=['POST'])
    def create_partner(self, **kw):
        try:
            result = request.env['res.partner'].sudo().create(kw)
            return {'message': 'successfully!'}
        except Exception as e:
            return {'message': 'error!', 'error_details': str(e)}

    @http.route('/api/partner/edit', type='json', auth='none', methods=['POST'])
    def edit_partner(self, **kw):
        try:
            contact_user = request.env['res.partner'].sudo().search([('id', '=', kw['id'])])
            if not contact_user:
                return {'message': 'User does not exist!'}

            user_edit = contact_user.write({'name': kw['name'], 'email': kw['email']})
            if user_edit:
                return {'message': 'Successfully edited!'}
            else:
                return {'message': 'Edit did not succeed!'}
        except Exception as e:
            return {'message': 'Error: ' + str(e)}

    @http.route('/api/partner/delete', type='json', auth='none', methods=['POST'])
    def delete_partner(self, **kw):
        try:
            # Check if 'id' is provided in the request data
            if 'id' in kw:
                partner_id = int(kw['id'])
                partner = request.env['res.partner'].sudo().search([('id', '=', partner_id)])

                if partner:
                    partner.unlink()  # Delete the record
                    return {'message': 'Record deleted successfully!'}
                else:
                    return {'message': 'Record not found!'}
            else:
                return {'message': 'ID parameter is missing from the request data!'}
        except Exception as e:
            return {'message': 'Error: ' + str(e)}
                