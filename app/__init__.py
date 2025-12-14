from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
from config import config

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)
# ------------------------


db = SQLAlchemy(metadata=metadata)
migrate = Migrate()
def create_app(config_name='default'):
    
    app = Flask(__name__)

   
    app.config.from_object(config[config_name])

    # Ініціалізуємо розширення з цим конкретним додатком
    db.init_app(app)
    migrate.init_app(app, db)

    # --- Реєстрація Blueprints ---
    from app.users.views import users_bp
    app.register_blueprint(users_bp, url_prefix="/users")

    from app.pages.views import pages_bp
    app.register_blueprint(pages_bp)

    # Реєстрація блюпринта продуктів (Lab 7)
    # Прибираємо try-except, щоб бачити помилки, якщо вони є
    from app.products.views import products_bp
    app.register_blueprint(products_bp, url_prefix="/products")

    # Реєстрація блюпринта для постів (Lab 6)
    from app.posts import posts_bp
    app.register_blueprint(posts_bp, url_prefix="/post")

    # --- Обробник помилок ---
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app