import unittest
from app import app


class ProductBlueprintTestCase(unittest.TestCase):

    def setUp(self):
        """Налаштування тестового клієнта."""
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_product_list_page(self):
        """Перевірка доступності сторінки зі списком продуктів."""
        response = self.client.get("/products/list")
        self.assertEqual(response.status_code, 200)

    def test_product_list_content(self):
        """Перевірка, що сторінка містить назви продуктів."""
        response = self.client.get("/products/list")
        self.assertIn(b"\xd0\x9d\xd0\xbe\xd1\x83\xd1\x82\xd0\xb1\xd1\x83\xd0\xba", response.data)
        self.assertIn(b"\xd0\xa1\xd0\xbc\xd0\xb0\xd1\x80\xd1\x82\xd1\x84\xd0\xbe\xd0\xbd", response.data)
