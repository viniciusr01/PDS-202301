from flask import Blueprint, current_app, jsonify, request
from src.domain.services.MakeTransaction import MakeTransaction
from src.adapters.SqlAdapter import SqlAdapter
from src.domain.gates.TransactionFactory import TransactionFactory



transaction = Blueprint('transaction', __name__,)

@transaction.route('/', methods = ['POST'])
def CreateTransaction():
    try:
        if request.headers['Content-Type'] != 'application/json':
                current_app.logger.debug(request.headers['Content-Type'])
                return jsonify(msg=('Header Error'))

        data = request.get_json()

        MakeTransaction(SqlAdapter()).make(data['user']['cpf'], 
                        TransactionFactory().make(obj=data['transaction']))

        return jsonify(msg = "Sucesso")

    except Exception as e:
        return jsonify(str(e))