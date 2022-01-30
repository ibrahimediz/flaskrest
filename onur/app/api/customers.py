from app.api import bp

@bp.route('/customers/<int:id>',methods=['GET'])
def get_customer(id):
    return jsonify(Customer.query.get_or_404(id).to_dict())

@bp.route('/customers',methods=['GET'])
def get_customers():
    return jsonify(Customer.to_collection_dict(Customer.query.all()))

@bp.route('/customers',methods=['POST'])
def create_customer():
    pass

@bp.route('/customers/<int:id>',methods=['PUT'])
def update_customer(id):
    pass