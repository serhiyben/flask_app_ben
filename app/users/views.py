from flask import Blueprint, render_template, request, redirect, url_for

# Створюємо Blueprint для users
users_bp = Blueprint('users', __name__, template_folder='templates')

@users_bp.route('/hi/<string:name>')
def greetings(name):
    """Сторінка привітання користувача."""
    # Отримуємо параметр age з URL, якщо немає — None
    age = request.args.get('age', None)
    # Пробуємо перетворити age на int, якщо можливо
    try:
        age = int(age) if age is not None else None
    except ValueError:
        age = None

    return render_template('users/hi.html', name=name.upper(), age=age)

@users_bp.route('/admin')
def admin():
    """Перенаправляє на сторінку greetings з фіксованими параметрами."""
    to_url = url_for('users.greetings', name='Administrator', age=45)
    return redirect(to_url)
