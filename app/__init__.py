from flask import Flask

def create_app():
    # створюємо Flask-додаток
    app = Flask(__name__)

    # завантажуємо конфігурацію (якщо є config.py)
    app.config.from_pyfile("../config.py", silent=True)

    # Імпортуємо та реєструємо Blueprints
    from app.users.views import users_bp
    app.register_blueprint(users_bp, url_prefix="/users")

    from app.pages.views import pages_bp
    app.register_blueprint(pages_bp)

    # Якщо є другий Blueprint (products)
    try:
        from app.products.views import products_bp
        app.register_blueprint(products_bp, url_prefix="/products")
    except ModuleNotFoundError:
        # Якщо products ще не створений — просто пропускаємо
        pass

    return app

# створюємо головний екземпляр застосунку
app = create_app()
