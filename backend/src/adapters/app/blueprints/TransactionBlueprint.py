from flask import Blueprint, current_app, jsonify, request
from flask_cors import cross_origin
from src.domain.services.MakeTransaction import MakeTransaction
from src.adapters.SqlAdapter import SqlAdapter
from src.domain.gates.TransactionFactory import TransactionFactory



transaction = Blueprint('transaction', __name__,)

@transaction.route('/', methods = ['POST'])
@cross_origin()
def CreateTransaction():
    try:
        if request.headers['Content-Type'] != 'application/json':
                current_app.logger.debug(request.headers['Content-Type'])
                return jsonify(msg=('Header Error'))

        data = request.get_json()

        return jsonify(MakeTransaction(SqlAdapter()).make(TransactionFactory().make(obj=data['transaction'])))


    except TypeError as e:
        return jsonify(str(e)), 400
         

    except Exception as e:
        print(e.with_traceback, e.args)
        return "An internal error occurred. Please, try again later.", 500