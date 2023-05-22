from flask import Flask
from ..app.blueprints.TransactionBlueprint import transaction
from ..app.blueprints.UserBlueprint import user

def CreateApp():
    # TODO: CONFERIR SE ISSO SERIA UM ADAPTER MESMO (E OS BLUEPRINTS)
    app = Flask(__name__)
    app.register_blueprint(transaction, url_prefix='/transaction')
    app.register_blueprint(user, url_prefix='/user')

    @app.route("/", methods = ['GET'])
    def hello_world():
        return "<p>Hello, MoneyHive!</p>"

    return app