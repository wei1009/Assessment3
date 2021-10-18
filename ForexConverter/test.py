from unittest import TestCase
from werkzeug.utils import html
from app import app

class FlaskTests(TestCase):

    def setUp(self):
        app.config['TESTING'] = True

    def test_homepage(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code,200)
            self.assertIn('<div>\n<form action="/convert">', html)

    def test_vaild_data(self):
        with app.test_client() as client:
            res = client.get("/convert?covertfrom=USD&covertto=USD&amount=1")
            self.assertEqual(res.status_code,302)
            self.assertEqual(res.location,"http://localhost/exchangeResult?convertedAmount=1.0&convertToSymbol=US%24")

    def test_invalid_data(self):
        with app.test_client() as client:
            res = client.get("/convert?covertfrom=AAA&covertto=USD&amount=100")
            html = res.get_data(as_text=True)
            self.assertIn('<div style=\'font-weight: bold;color:red\'>Not a vaild code: AAA</div>\n<div>', html)
            self.assertEqual(res.status_code,200)

    def test_result_page(self):
        with app.test_client() as client:
            res = client.get("/exchangeResult?convertedAmount=100.0&convertToSymbol=US%24")
            html = res.get_data(as_text=True)
            self.assertIn('<p>The result is US$100.0<div></p>', html)
            self.assertEqual(res.status_code,200)
