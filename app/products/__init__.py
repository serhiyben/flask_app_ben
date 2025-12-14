from flask import Flask
from typing import Optional

app: Optional[Flask]

def create_app():
    global app
    app = Flask(__name__)
    ...
    return app

app = create_app()

from flask import Blueprint

products_bp = Blueprint('products', __name__, template_folder='templates')


from . import views, models