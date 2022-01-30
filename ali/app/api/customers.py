from app.api import bp
from app.models import User
from flask import jsonify

@bp.route('/user/<int:user_id>', methods=['GET'])
def get_customer(user_id):
    return jsonify(User.query.get_or_404(user_id).to_dict())

@bp.route('/customers', methods=['GET'])
def get_customers():
    pass

@bp.route('/customers', methods=['POST'])
def create_customer():
    pass

@bp.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    pass