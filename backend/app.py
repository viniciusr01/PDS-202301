from src.adapters.app.Server import CreateApp
from flask_cors import CORS, cross_origin


app = CreateApp()
CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True)