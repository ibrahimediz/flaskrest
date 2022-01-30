from app.api import bp
from app.models import Customer
from flask import jsonify

@bp.route('/customers/<int:id>',methods=['GET'])
def get_customer(id):
    return jsonify(Customer.query.get_or_404(id).to_dict())

@bp.point('/customers',methods=['GET'])
def get_customers():

    return jsonify(Customer.query.all().to_dict())
    

@bp.route('/customers',methods=['POST'])
def create_customer():

    pass

@bp.route('/customers/<int:id>',methods=['PUT'])
def update_customer():

    pass