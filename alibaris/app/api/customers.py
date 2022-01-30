from app.api import bp
from app.models import Customer
from flask import jsonify

@bp.route('/customers', methods = ['GET'])
def get_all_customers():
    all_customers = Customer.query.all()
    return jsonfiy(to_dict(all_customers))

@bp.route('/customers/<int:id>', methods = ['GET'])
def get_customer(id:int):
    return jsonify(Customer.query.get_or_404(id).to_dict())

@bp.route('/customers', methods = ['POST'])
def create_customer():
    pass

@bp.route('/customers/<int:id>', methods = ['PUT'])
def update_customer():
    pass





