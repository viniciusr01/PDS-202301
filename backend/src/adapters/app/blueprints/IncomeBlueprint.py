from datetime import date, datetime
from flask import Blueprint, current_app, jsonify, request
from flask_cors import cross_origin
from src.domain.services.RetrieveIncomesInAPeriod import RetrieveIncomesInAPeriod
from src.domain.gates.dto.RetrieveIncomesDTO import RetrieveIncomesDTO
from src.adapters.SqlAdapter import SqlAdapter
from src.utils.ValidObject import ValidObject

income = Blueprint('income', __name__,)


@income.route('/<user_id>', methods = ['GET'])
@cross_origin()
def RetrieveIncomes(user_id: int):
    try:
        if request.headers['Content-Type'] != 'application/json':
            current_app.logger.debug(request.headers['Content-Type'])
            return jsonify(msg=('Header Error'))

        data = request.get_json()

        if not ValidObject().make(data, [
            "initial_date"
        ]):
            return TypeError("This method require the 'initial_date' at least")
        
        initial_date = datetime.strptime(data["initial_date"], '%Y-%m-%d')
        end_date = datetime.strptime(data["end_date"], '%Y-%m-%d') if "end_date" in data.keys() else date.today()

        income = RetrieveIncomesInAPeriod(SqlAdapter()).make(user_id=str(user_id),
                                                               initial_date=initial_date,
                                                               end_date = end_date)

        res = RetrieveIncomesDTO().make(income)
        
        return jsonify(res)

    except TypeError as e:
        return jsonify(str(e)), 400
         

    except Exception as e:
        print(e.args, e.with_traceback)
        return "An internal error occurred. Please, try again later.", 500