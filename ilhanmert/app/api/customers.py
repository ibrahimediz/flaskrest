from app.api import bp

@bp.route('/customers/<int:id>',methods=['GET'])
def get_customer(id):
    pass


@bp.route('/customers', methods=['GET'])
def get_customers():
    pass

@bp.route('/customers', methods=['POST'])
def create_customer():
    pass

@bp.route('/customers', methods=['POST'])
def update_customer():
    pass

