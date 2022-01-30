from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import customers, errors, tokens

#. GET /api/userse/<id>
#  GET /api/users
#. PUT /api/users/<id>
# POST /api/users