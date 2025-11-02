from flask import Flask

def create_app():
    app = Flask(__name__)

    # Імпортуємо й реєструємо Blueprints
    from app.users.views import users_bp
    from app.products.views import products_bp

    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(products_bp, url_prefix="/products")

    return app

# Головний екземпляр застосунку
app = create_app()
