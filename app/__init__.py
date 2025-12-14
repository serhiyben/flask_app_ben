from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

# Ініціалізуємо розширення глобально (поки що не прив'язуємо до конкретного app)
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    # Створюємо екземпляр додатку
    app = Flask(__name__)

    # Завантажуємо налаштування з об'єкта конфігурації (відповідно до імені)
    app.config.from_object(config[config_name])

    # Ініціалізуємо розширення з цим конкретним додатком
    db.init_app(app)
    migrate.init_app(app, db)

    # --- Реєстрація Blueprints ---
    from app.users.views import users_bp
    app.register_blueprint(users_bp, url_prefix="/users")

    from app.pages.views import pages_bp
    app.register_blueprint(pages_bp)

    # Блюпринт для продуктів (опціональний, як у вас було)
    try:
        from app.products.views import products_bp
        app.register_blueprint(products_bp, url_prefix="/products")
    except ImportError:
        pass

    # Тут пізніше буде реєстрація блюпринта для постів (Lab 6, Частина 2)
    # from app.posts.views import posts_bp
    from app.posts import posts_bp
    app.register_blueprint(posts_bp, url_prefix="/post")

    # --- Обробник помилок ---
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app