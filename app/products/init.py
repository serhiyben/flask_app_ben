from app.products.views import products_bp
app.register_blueprint(products_bp, url_prefix="/products")
