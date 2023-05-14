from flask import Flask
from ..app.blueprints.TransactionBlueprint import transaction
from ..app.blueprints.UserBlueprint import user

def CreateApp():
    app = Flask(__name__)
    app.register_blueprint(transaction, url_prefix='/transaction')
    app.register_blueprint(user, url_prefix='/user')

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    return app