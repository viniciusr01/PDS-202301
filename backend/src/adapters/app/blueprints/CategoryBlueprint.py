from flask import Blueprint, current_app, jsonify, request
from flask_cors import cross_origin
from src.domain.services.MakeCategory import MakeCategory
from src.adapters.SqlAdapter import SqlAdapter
from src.domain.gates.CategoryFactory import CategoryFactory


category = Blueprint('category', __name__,)

@category.route('/', methods = ['POST'])
@cross_origin()
def AddCategory():
    try:
        if request.headers['Content-Type'] != 'application/json':
                current_app.logger.debug(request.headers['Content-Type'])
                return jsonify(msg=('Header Error'))

        data = request.get_json()

        return jsonify(MakeCategory(SqlAdapter()).make(CategoryFactory().make(obj=data['category'])))


    except TypeError as e:
        return jsonify(str(e)), 400
         

    except Exception as e:
        print(e.with_traceback, e.args)
        return "An internal error occurred.", 500