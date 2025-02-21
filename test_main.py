import unittest
from main import app

class TestQuadraticCalculator(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_calculate_roots_valid(self):
        response = self.app.post('/', data={'a': '1', 'b': '-5', 'c': '6'})
        self.assertIn('Корни уравнения:', response.data.decode('utf-8'))

    def test_zero_a_coefficient(self):
        response = self.app.post('/', data={'a': '0', 'b': '2', 'c': '1'})
        response_text = response.data.decode('utf-8')
        self.assertIn("Коэффициент &#39;a&#39; не может быть меньше или равен нулю", response_text)

    def test_invalid_input(self):
        response = self.app.post('/', data={'a': 'a', 'b': 'b', 'c': 'c'})
        self.assertIn('Введите числовые значения для a, b, c', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
