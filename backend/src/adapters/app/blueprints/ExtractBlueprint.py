from datetime import date, datetime
from flask import Blueprint, current_app, jsonify, request
from src.domain.gates.dto.RetrieveExtractDTO import RetrieveExtractDTO
from src.domain.services.RetrieveExtractInAPeriod import RetrieveExtractInAPeriod
from src.adapters.SqlAdapter import SqlAdapter
from src.utils.ValidObject import ValidObject

extract = Blueprint('extract', __name__,)

@extract.route('/<account_id>', methods = ['GET'])
def RetrieveUserAccount(account_id: int):
    try:
        if request.headers['Content-Type'] != 'application/json':
            current_app.logger.debug(request.headers['Content-Type'])
            return jsonify(msg=('Header Error'))

        data = request.get_json()

        if not ValidObject().make(data, [
            "type",
            "initial_date"
        ]):
            return TypeError("This method require the 'type' and 'initial_date' at least")
        
        
        initial_date = datetime.strptime(data["initial_date"], '%Y-%m-%d')
        end_date = datetime.strptime(data["end_date"], '%Y-%m-%d') if "end_date" in data.keys() else date.today()

        extract = RetrieveExtractInAPeriod(SqlAdapter()).make(account_id=str(account_id),
                                                            type=data["type"],
                                                            initial_date=initial_date,
                                                            end_date = end_date,
                                                            number_of_days = data["number_of_days"] if "number_of_days" in data.keys() else None)

        res = RetrieveExtractDTO().make(extract)
        
        return jsonify(res)

    except TypeError as e:
        return jsonify(str(e)), 400
         

    except Exception as e:
        print(e.args, e.with_traceback)
        return "An internal error occurred. Please, try again later.", 500