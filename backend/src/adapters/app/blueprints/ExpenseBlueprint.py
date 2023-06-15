from datetime import date, datetime
from flask import Blueprint, current_app, jsonify, request
from flask_cors import cross_origin
from src.domain.gates.dto.RetrieveExpensesDTO import RetrieveExpensesDTO
from src.domain.services.RetrieveExpensesInAPeriod import RetrieveExpensesInAPeriod
from src.adapters.SqlAdapter import SqlAdapter
from src.utils.ValidObject import ValidObject

expense = Blueprint('expense', __name__,)
    
@expense.route('/<user_id>/<initial_date>/<end_date>', methods = ['GET'])
@cross_origin()
def RetrieveExpenses(user_id: int, initial_date: str, end_date: str):
    try:
        initial_date = datetime.strptime(initial_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        expense = RetrieveExpensesInAPeriod(SqlAdapter()).make(user_id=str(user_id),
                                                               initial_date=initial_date,
                                                               end_date = end_date)

        res = RetrieveExpensesDTO().make(expense)
        
        return jsonify(res)

    except TypeError as e:
        return jsonify(str(e)), 400
         

    except Exception as e:
        print(e.args, e.with_traceback)
        return "An internal error occurred. Please, try again later.", 500
    
    