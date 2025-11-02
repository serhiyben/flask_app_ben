from flask import Blueprint, render_template

products_bp = Blueprint('products', __name__, template_folder='templates')

@products_bp.route('/list')
def product_list():
    products = ["Ноутбук", "Смартфон", "Навушники"]
    return render_template('products/list.html', products=products)
