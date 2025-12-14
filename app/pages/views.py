from flask import Blueprint, render_template, redirect, url_for, flash
import logging
from app.pages.forms import ContactForm

pages_bp = Blueprint('pages', __name__, template_folder='templates')

# Налаштування логування
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

@pages_bp.route("/")
def index():
    return render_template("index.html", title="Головна")

@pages_bp.route("/resume")
def resume():
    return render_template("resume.html", title="Резюме")

@pages_bp.route("/contacts", methods=["GET", "POST"])
def contacts():
    form = ContactForm()
    
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data
        
        
        logging.info(f"Form submitted: Name={name}, Email={email}, Subject={subject}")
        
        flash(f"Повідомлення успішно надіслано! Дякуємо, {name}.", "success")
        return redirect(url_for('pages.contacts'))
    
    return render_template("contacts.html", title="Контакти", form=form)