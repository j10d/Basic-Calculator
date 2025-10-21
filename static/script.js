let currentValue = '0';
let previousValue = null;
let operator = null;
let waitingForOperand = false;

const display = document.getElementById('display');

function updateDisplay() {
    display.textContent = currentValue;
}

function appendNumber(num) {
    if (waitingForOperand) {
        currentValue = num;
        waitingForOperand = false;
    } else {
        if (currentValue === '0' && num !== '.') {
            currentValue = num;
        } else {
            if (num === '.' && currentValue.includes('.')) {
                return;
            }
            currentValue += num;
        }
    }
    updateDisplay();
}

function setOperator(op) {
    if (operator !== null && !waitingForOperand) {
        calculate();
    }
    previousValue = parseFloat(currentValue);
    operator = op;
    waitingForOperand = true;
}

function calculate() {
    if (operator === null || previousValue === null) {
        return;
    }

    const current = parseFloat(currentValue);
    let operationMap = {
        '+': 'add',
        '-': 'subtract',
        '×': 'multiply',
        '÷': 'divide'
    };

    const operation = operationMap[operator];

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            operation: operation,
            num1: previousValue,
            num2: current
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            currentValue = 'Error';
        } else {
            currentValue = String(data.result);
        }
        updateDisplay();
        operator = null;
        previousValue = null;
        waitingForOperand = true;
    })
    .catch(error => {
        currentValue = 'Error';
        updateDisplay();
    });
}

function clearAll() {
    currentValue = '0';
    previousValue = null;
    operator = null;
    waitingForOperand = false;
    updateDisplay();
}

function toggleSign() {
    const current = parseFloat(currentValue);

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            operation: 'negate',
            num1: current,
            num2: 0
        })
    })
    .then(response => response.json())
    .then(data => {
        if (!data.error) {
            currentValue = String(data.result);
            updateDisplay();
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function percentage() {
    const current = parseFloat(currentValue);

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            operation: 'percentage',
            num1: current,
            num2: 0
        })
    })
    .then(response => response.json())
    .then(data => {
        if (!data.error) {
            currentValue = String(data.result);
            updateDisplay();
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Initialize display
updateDisplay();
