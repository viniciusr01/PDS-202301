from flask import Flask
from ..app.blueprints.TransactionBlueprint import transaction
from ..app.blueprints.UserBlueprint import user
from ..app.blueprints.ExtractBlueprint import extract
from ..app.blueprints.ExpenseBlueprint import expense
from ..app.blueprints.AuthBlueprint import auth

def CreateApp():
    # TODO: CONFERIR SE ISSO SERIA UM ADAPTER MESMO (E OS BLUEPRINTS)
    app = Flask(__name__)
    app.register_blueprint(transaction, url_prefix='/transaction')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(extract, url_prefix='/extract')
    app.register_blueprint(expense, url_prefix='/expense')
    app.register_blueprint(auth, url_prefix='/auth')


    @app.route("/", methods = ['GET'])
    def hello_world():
        return "<p>Hello, MoneyHive!</p>"

    return app