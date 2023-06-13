from flask import Flask
from ..app.blueprints.TransactionBlueprint import transaction
from ..app.blueprints.UserBlueprint import user
from ..app.blueprints.ExtractBlueprint import extract
from ..app.blueprints.IncomeBlueprint import income
from ..app.blueprints.ExpenseBlueprint import expense
from ..app.blueprints.CategoryBlueprint import category
from ..app.blueprints.AuthBlueprint import auth

from flask import Flask
from flask_cors import CORS, cross_origin

def CreateApp():
    # TODO: CONFERIR SE ISSO SERIA UM ADAPTER MESMO (E OS BLUEPRINTS)
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.register_blueprint(transaction, url_prefix='/transaction')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(extract, url_prefix='/extract')
    app.register_blueprint(income, url_prefix='/income')
    app.register_blueprint(expense, url_prefix='/expense')
    app.register_blueprint(category, url_prefix='/category')
    app.register_blueprint(auth, url_prefix='/auth')


    @app.route("/", methods = ['GET'])
    @cross_origin()
    def hello_world():
        return "<p>Hello, MoneyHive!</p>"

    return app