from datetime import date, datetime
from flask import Blueprint, jsonify
from src.domain.gates.dto.RetrieveExpensesDTO import RetrieveExpensesDTO
from src.domain.gates.dto.RetrieveIncomesDTO import RetrieveIncomesDTO
from src.domain.services.RetrieveExpensesInAPeriod import RetrieveExpensesInAPeriod
from src.domain.services.RetrieveIncomesInAPeriod import RetrieveIncomesInAPeriod
from src.domain.services.RetrieveUserAccounts import RetrieveUserAccounts
from src.adapters.SqlAdapter import SqlAdapter
from src.domain.gates.dto.RetrieveUserAccountDTO import RetrieveUserAccountDTO

user = Blueprint('user', __name__,)

@user.route('/<user_id>', methods = ['GET'])
def RetrieveUserAccount(user_id: int):
    try:

        user = SqlAdapter().GetUser(user_id)

        res = {'User': {
            'name':user[0][2],
            'email':user[0][1]
            }
        }

        accounts = RetrieveUserAccounts(SqlAdapter()).make(user_id)
        accounts = RetrieveUserAccountDTO().make(accounts)
        res.update(accounts)

        expenses = RetrieveExpensesInAPeriod(SqlAdapter()).make(user_id=str(user_id),
                                                               initial_date=datetime(date.today().year, date.today().month, 1),
                                                               end_date = date.today())

        expenses = RetrieveExpensesDTO().make(expenses)
        res.update(expenses)

        incomes = RetrieveIncomesInAPeriod(SqlAdapter()).make(user_id=str(user_id),
                                                               initial_date=datetime(date.today().year, date.today().month, 1),
                                                               end_date = date.today())

        incomes = RetrieveIncomesDTO().make(incomes)
        res.update(incomes)


        return res

    except TypeError as e:
        return jsonify(str(e)), 400
         

    except Exception as e:
        print(e.args, e.with_traceback)
        return "An internal error occurred. Please, try again later.", 500