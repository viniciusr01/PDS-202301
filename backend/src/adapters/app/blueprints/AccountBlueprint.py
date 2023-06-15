from flask import Blueprint, current_app, jsonify, request
from flask_cors import cross_origin
from src.adapters.SqlAdapter import SqlAdapter
from src.domain.gates.AccountFactory import AccountFactory
from src.domain.services.MakeAccount import MakeAccount


account = Blueprint('account', __name__,)

@account.route('/', methods = ['POST'])
def AddCategory():
    try:
        if request.headers['Content-Type'] != 'application/json':
                current_app.logger.debug(request.headers['Content-Type'])
                return jsonify(msg=('Header Error'))

        data = request.get_json()['data']

        return jsonify(MakeAccount(SqlAdapter()).make(AccountFactory().make(obj=data)))


    except TypeError as e:
        return jsonify(str(e)), 400
         

    except Exception as e:
        print(e.with_traceback, e.args)
        return "An internal error occurred.", 500