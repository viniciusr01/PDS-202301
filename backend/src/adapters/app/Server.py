from flask import Flask
from ..app.blueprints.TransactionBlueprint import transaction

def CreateApp():
    app = Flask(__name__)
    app.register_blueprint(transaction, url_prefix='/transaction')

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    return app