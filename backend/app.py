from src.adapters.app.Server import CreateApp

app = CreateApp()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True)