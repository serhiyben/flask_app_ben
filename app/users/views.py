from flask import Blueprint, render_template, request, redirect, url_for, flash, session, make_response

# Створюємо Blueprint
users_bp = Blueprint("users", __name__, template_folder="templates")

# "База даних" користувачів
users_data = {"user1": "123", "admin": "admin123"}

@users_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users_data and users_data[username] == password:
            session["username"] = username
            flash("Ви успішно увійшли!", "success")
            return redirect(url_for("users.profile"))
        else:
            flash("Невірні дані! Спробуйте ще раз.", "danger")
            return redirect(url_for("users.login"))

    return render_template("users/login.html")

@users_bp.route("/profile")
def profile():
    if "username" not in session:
        flash("Будь ласка, увійдіть спочатку.", "warning")
        return redirect(url_for("users.login"))
    
    # Передаємо куки у шаблон для відображення в таблиці
    return render_template("users/profile.html", username=session["username"], cookies=request.cookies)

@users_bp.route("/logout")
def logout():
    session.pop("username", None)
    flash("Ви вийшли з системи.", "info")
    return redirect(url_for("users.login"))

# --- Робота з COOKIES (Завдання 2) ---

@users_bp.route('/add_cookie', methods=['POST'])
def add_cookie():
    key = request.form.get('key')
    value = request.form.get('value')
    expiry = request.form.get('expiry')

    # Створюємо відповідь-перенаправлення
    resp = make_response(redirect(url_for('users.profile')))

    if key and value and expiry:
        try:
            # max_age задається в секундах
            resp.set_cookie(key, value, max_age=int(expiry))
            flash(f'Куку "{key}" успішно додано.', 'success')
        except ValueError:
            flash('Термін дії має бути числом.', 'danger')
    else:
        flash('Заповніть всі поля.', 'warning')
    
    return resp

@users_bp.route('/delete_cookie', methods=['POST'])
def delete_cookie():
    key = request.form.get('key')
    
    resp = make_response(redirect(url_for('users.profile')))
    
    # Видаляємо куку, встановлюючи їй нульовий час життя
    if key:
        resp.delete_cookie(key)
        flash(f'Куку "{key}" видалено.', 'success')
    else:
        flash('Вкажіть ключ куки.', 'warning')
        
    return resp

@users_bp.route('/delete_all_cookies', methods=['POST'])
def delete_all_cookies():
    resp = make_response(redirect(url_for('users.profile')))
    
    cookies = request.cookies
    for key in cookies:
        # Не видаляємо сесійну куку, інакше нас викине з профілю
        if key != 'session':
            resp.delete_cookie(key)
    
    flash('Всі куки (крім сесії) видалено.', 'info')
    return resp

# --- Інші маршрути ---

@users_bp.route("/hi/<string:name>")
def greetings(name):
    return render_template(
        "users/hi.html", name=name.upper(), age=request.args.get("age")
    )

@users_bp.route("/admin")
def admin():
    return redirect(url_for("users.greetings", name="Administrator", age=45))



@users_bp.route('/change_theme/<string:theme>')
def change_theme(theme):
    """Змінює тему оформлення, зберігаючи вибір у куки."""
    
    allowed_themes = ['light', 'dark', 'green']
    
    if theme not in allowed_themes:
        flash('Невідома тема!', 'warning')
        return redirect(url_for('users.profile'))
    
    
    resp = make_response(redirect(url_for('users.profile')))
    
    
    resp.set_cookie('theme', theme, max_age=30*24*60*60)
    
    flash(f'Тему успішно змінено на {theme}.', 'success')
    return resp