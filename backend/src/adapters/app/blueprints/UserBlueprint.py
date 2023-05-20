from flask import Blueprint, jsonify
from src.domain.services.RetrieveUserAccounts import RetrieveUserAccounts
from src.adapters.SqlAdapter import SqlAdapter
from src.domain.gates.dto.RetrieveUserAccountDTO import RetrieveUserAccountDTO

user = Blueprint('user', __name__,)

@user.route('/accounts/<user_id>', methods = ['GET'])
def RetrieveUserAccount(user_id: int):
    try:
        accounts = RetrieveUserAccounts(SqlAdapter()).make(user_id)
        res = RetrieveUserAccountDTO().make(accounts)

        return jsonify(res)

    except Exception as e:
        return jsonify(str(e))