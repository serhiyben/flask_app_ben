from flask import Flask
from typing import Optional

app: Optional[Flask]

def create_app():
    global app
    app = Flask(__name__)
    ...
    return app

app = create_app()
