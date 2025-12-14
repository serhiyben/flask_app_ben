from flask import Flask


def create_app():

    app = Flask(__name__)

    app.config.from_pyfile("../config.py", silent=True)

    from app.users.views import users_bp

    app.register_blueprint(users_bp, url_prefix="/users")

    from app.pages.views import pages_bp

    app.register_blueprint(pages_bp)

    try:
        from app.products.views import products_bp

        app.register_blueprint(products_bp, url_prefix="/products")
    except ModuleNotFoundError:

        pass

    return app


app = create_app()
