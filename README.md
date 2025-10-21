## Flask Calculator App

A simple web-based calculator built with Flask. Features a modern interface with basic arithmetic operations.

### Features
- Basic operations: addition, subtraction, multiplication, division
- AC (All Clear) button to reset the calculator
- +/- button to toggle positive/negative numbers
- % button for percentage calculations
- = button to execute calculations
- Clean, iOS-inspired design

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the App

1. Start the Flask development server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

### Running Tests

The project includes a comprehensive test suite for the calculator UI functionality. To run the tests:

1. Run all tests:
```bash
pytest test_app.py
```

2. Run tests with verbose output:
```bash
pytest test_app.py -v
```

3. Run a specific test class or method:
```bash
pytest test_app.py::TestCalculatorUI::test_addition
```

The test suite covers all calculator operations including addition, subtraction, multiplication, division, percentage calculations, number negation, and edge cases like division by zero and invalid inputs.

### Project Structure
```
.
├── app.py              # Flask application and routes
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Calculator HTML interface
└── static/
    ├── style.css      # Calculator styling
    └── script.js      # Calculator functionality
```
