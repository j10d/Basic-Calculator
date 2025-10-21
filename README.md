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
