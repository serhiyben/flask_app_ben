"""Insert initial data

Revision ID: 5fd56699f537
Revises: 95687cfe9f87
Create Date: 2025-12-14 23:23:42.345938

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Float, Boolean


# revision identifiers, used by Alembic.
revision = '5fd56699f537'
down_revision = '95687cfe9f87'
branch_labels = None
depends_on = None


def upgrade():
    categories_table = table('categories',
        column('id', Integer),
        column('name', String)
    )

    products_table = table('products',
        column('id', Integer),
        column('name', String),
        column('price', Float),
        column('active', Boolean),
        column('category_id', Integer)
    )

    # 2. Вставляємо Категорії
    op.bulk_insert(categories_table, [
        {'id': 1, 'name': 'Electronics'},
        {'id': 2, 'name': 'Books'},
        {'id': 3, 'name': 'Clothing'}
    ])

    # 3. Вставляємо Товари
    op.bulk_insert(products_table, [
        {'name': 'Laptop', 'price': 1200.0, 'active': True, 'category_id': 1},
        {'name': 'Smartphone', 'price': 800.0, 'active': True, 'category_id': 1},
        {'name': 'Python Book', 'price': 20.0, 'active': True, 'category_id': 2},
        {'name': 'T-Shirt', 'price': 25.0, 'active': False, 'category_id': 3}
    ])


def downgrade():
    op.execute("DELETE FROM products WHERE name IN ('Laptop', 'Smartphone', 'Python Book', 'T-Shirt')")
    op.execute("DELETE FROM categories WHERE name IN ('Electronics', 'Books', 'Clothing')")
