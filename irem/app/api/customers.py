from app.api import bp

@bp.route('/customers/<int:id>',methods = ['GET'])
def get_user(id):
    pass

@bp.route('/customers',methods=['GET'])
def get_users():
    pass

@bp.route('/customers',methods=['POST'])
def create_user():
    pass

@bp.route('/customers/<int:id>',methods=['PUT'])
def update_customer(id):
    pass