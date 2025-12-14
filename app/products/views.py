from flask import Blueprint, render_template


products_bp = Blueprint('products', __name__, template_folder='templates')

@products_bp.route('/list')
def product_list():
    """Відображення списку продуктів."""
    products = [
        {"name": "Ноутбук", "price": 25000},
        {"name": "Смартфон", "price": 18000},
        {"name": "Навушники", "price": 2500}
    ]
    return render_template('products/list.html', products=products)
