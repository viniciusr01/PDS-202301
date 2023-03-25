from flask import Flask 
from flask_cors import CORS
from flask import request


app = Flask("Money Hive")
CORS(app)


@app.route("/")
def home():
    return "<h1>Hello Word</h1>"



app.run(debug=True)