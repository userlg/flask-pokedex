from flask import Flask

def init_app() -> None:
    app = Flask(__name__)

    return app

app = init_app()