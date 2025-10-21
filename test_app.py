import pytest
import json
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask application"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


class TestCalculatorUI:
    """Test suite for Flask calculator user interface"""

    def test_index_route_renders(self, client):
        """Test that the index route renders successfully"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Flask Calculator' in response.data
        assert b'display' in response.data

    def test_addition(self, client):
        """Test addition operation"""
        response = client.post('/calculate',
                              json={'operation': 'add', 'num1': 5, 'num2': 3})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == 8

    def test_addition_with_decimals(self, client):
        """Test addition with decimal numbers"""
        response = client.post('/calculate',
                              json={'operation': 'add', 'num1': 2.5, 'num2': 3.7})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == pytest.approx(6.2)

    def test_addition_with_negative_numbers(self, client):
        """Test addition with negative numbers"""
        response = client.post('/calculate',
                              json={'operation': 'add', 'num1': -5, 'num2': 3})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == -2

    def test_subtraction(self, client):
        """Test subtraction operation"""
        response = client.post('/calculate',
                              json={'operation': 'subtract', 'num1': 10, 'num2': 4})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == 6

    def test_subtraction_negative_result(self, client):
        """Test subtraction resulting in negative number"""
        response = client.post('/calculate',
                              json={'operation': 'subtract', 'num1': 3, 'num2': 8})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == -5

    def test_multiplication(self, client):
        """Test multiplication operation"""
        response = client.post('/calculate',
                              json={'operation': 'multiply', 'num1': 6, 'num2': 7})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == 42

    def test_multiplication_by_zero(self, client):
        """Test multiplication by zero"""
        response = client.post('/calculate',
                              json={'operation': 'multiply', 'num1': 5, 'num2': 0})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == 0

    def test_multiplication_with_decimals(self, client):
        """Test multiplication with decimal numbers"""
        response = client.post('/calculate',
                              json={'operation': 'multiply', 'num1': 2.5, 'num2': 4})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == 10.0

    def test_division(self, client):
        """Test division operation"""
        response = client.post('/calculate',
                              json={'operation': 'divide', 'num1': 20, 'num2': 4})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == 5

    def test_division_with_remainder(self, client):
        """Test division that produces decimal result"""
        response = client.post('/calculate',
                              json={'operation': 'divide', 'num1': 10, 'num2': 3})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == pytest.approx(3.333333, rel=1e-5)

    def test_division_by_zero(self, client):
        """Test division by zero returns error"""
        response = client.post('/calculate',
                              json={'operation': 'divide', 'num1': 10, 'num2': 0})
        data = json.loads(response.data)
        assert response.status_code == 400
        assert 'error' in data
        assert 'Cannot divide by zero' in data['error']

    def test_percentage(self, client):
        """Test percentage operation"""
        response = client.post('/calculate',
                              json={'operation': 'percentage', 'num1': 50, 'num2': 0})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == 0.5

    def test_percentage_decimal(self, client):
        """Test percentage with decimal number"""
        response = client.post('/calculate',
                              json={'operation': 'percentage', 'num1': 25.5, 'num2': 0})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == pytest.approx(0.255)

    def test_negate_positive_number(self, client):
        """Test negating a positive number"""
        response = client.post('/calculate',
                              json={'operation': 'negate', 'num1': 42, 'num2': 0})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == -42

    def test_negate_negative_number(self, client):
        """Test negating a negative number"""
        response = client.post('/calculate',
                              json={'operation': 'negate', 'num1': -15, 'num2': 0})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == 15

    def test_negate_zero(self, client):
        """Test negating zero"""
        response = client.post('/calculate',
                              json={'operation': 'negate', 'num1': 0, 'num2': 0})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == 0

    def test_invalid_operation(self, client):
        """Test that invalid operation returns error"""
        response = client.post('/calculate',
                              json={'operation': 'invalid', 'num1': 5, 'num2': 3})
        data = json.loads(response.data)
        assert response.status_code == 400
        assert 'error' in data
        assert 'Invalid operation' in data['error']

    def test_missing_operation(self, client):
        """Test request with missing operation parameter"""
        response = client.post('/calculate',
                              json={'num1': 5, 'num2': 3})
        data = json.loads(response.data)
        assert response.status_code == 400
        assert 'error' in data

    def test_missing_numbers(self, client):
        """Test that missing numbers default to 0"""
        response = client.post('/calculate',
                              json={'operation': 'add'})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == 0

    def test_invalid_number_format(self, client):
        """Test that invalid number format returns error"""
        response = client.post('/calculate',
                              json={'operation': 'add', 'num1': 'abc', 'num2': 5})
        data = json.loads(response.data)
        assert response.status_code == 400
        assert 'error' in data

    def test_malformed_json(self, client):
        """Test that malformed JSON returns error"""
        response = client.post('/calculate',
                              data='not json',
                              content_type='application/json')
        assert response.status_code == 400

    def test_large_numbers(self, client):
        """Test calculator with very large numbers"""
        response = client.post('/calculate',
                              json={'operation': 'multiply', 'num1': 999999, 'num2': 999999})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == 999998000001

    def test_very_small_numbers(self, client):
        """Test calculator with very small decimal numbers"""
        response = client.post('/calculate',
                              json={'operation': 'add', 'num1': 0.0001, 'num2': 0.0002})
        data = json.loads(response.data)
        assert response.status_code == 200
        assert data['result'] == pytest.approx(0.0003)

    def test_zero_operations(self, client):
        """Test operations with zero"""
        # Adding zero
        response = client.post('/calculate',
                              json={'operation': 'add', 'num1': 5, 'num2': 0})
        data = json.loads(response.data)
        assert data['result'] == 5

        # Subtracting zero
        response = client.post('/calculate',
                              json={'operation': 'subtract', 'num1': 5, 'num2': 0})
        data = json.loads(response.data)
        assert data['result'] == 5

        # Dividing zero
        response = client.post('/calculate',
                              json={'operation': 'divide', 'num1': 0, 'num2': 5})
        data = json.loads(response.data)
        assert data['result'] == 0
