from flask import Blueprint, jsonify
from src.domain.services.RetrieveUserAccounts import RetrieveUserAccounts
from src.adapters.SqlAdapter import SqlAdapter
from src.domain.gates.dto.RetrieveUserAccountDTO import RetrieveUserAccountDTO

user = Blueprint('user', __name__,)

@user.route('/<user_id>', methods = ['GET'])
def RetrieveUserAccount(user_id: int):
    try:
        accounts = RetrieveUserAccounts(SqlAdapter()).make(user_id)
        res = RetrieveUserAccountDTO().make(accounts)

        return jsonify(res)

    except TypeError as e:
        return jsonify(str(e)), 400
         

    except Exception as e:
        print(e.args, e.with_traceback)
        return "An internal error occurred. Please, try again later.", 500