from flask import Blueprint, render_template

pages_bp = Blueprint('pages', __name__, template_folder='templates')

@pages_bp.route("/")
def index():
    return render_template("index.html", title="Головна")

@pages_bp.route("/resume")
def resume():
    return render_template("resume.html", title="Резюме")

@pages_bp.route("/contacts")
def contacts():
    return render_template("contacts.html", title="Контакти")
