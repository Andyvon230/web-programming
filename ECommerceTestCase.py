import unittest
from ecommerce import app
from flask import url_for

class ECommerceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Your Home Page Content' in response.data)

    def test_products_page(self):
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Products List' in response.data)

    def test_customers_page(self):
        response = self.app.get('/customers')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Customers List' in response.data)

    def test_orders_page(self):
        response = self.app.get('/orders')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Orders List' in response.data)

    def test_order_details_page(self):
        response = self.app.get('/orderDetails')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Order Details' in response.data)

    def test_pagination(self):
        response = self.app.get('/products/page/1')
        self.assertEqual(response.status_code, 200)
        # Add more checks related to pagination

    def test_invalid_route(self):
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
