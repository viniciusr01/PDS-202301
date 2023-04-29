from flask import Blueprint, current_app, jsonify, request
from ....domain.services.MakeTransaction import MakeTransaction
from ....adapters.SqlAdapter import SqlAdapter


transaction = Blueprint('transaction', __name__,)

@transaction.route('/', methods = ['POST'])
def CreateTransaction():
    if request.headers['Content-Type'] != 'application/json':
            current_app.logger.debug(request.headers['Content-Type'])
            return jsonify(msg=('Header Error'))

    data = request.get_json()

    MakeTransaction(SqlAdapter, 
                    data['user']['cpf'], 
                    data['transaction'])

    return jsonify(msg = "Sucesso")
