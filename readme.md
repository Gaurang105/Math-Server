
# Math Server with Flask

A simple Flask web server that allows users to perform basic arithmetic operations via URLs and view a history of recent calculations.

## Features

- Perform arithmetic operations via URL endpoints.
- View the history of the last 20 operations.
- Automatic storage and retrieval of operation history using a pickle file.
- Interactive home page with sample endpoints.

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/Gaurang105/Math-Server.git
```

2. Go the project directory and run install packages listed in requirements.txt:

```bash
pip install -r requirements.txt
```

3. Run the server.

4. Navigate to `http://127.0.0.1:3000/` in your browser.

## Usage

### Arithmetic Operations
To perform arithmetic operations, use the following URL structure:

```bash
http://127.0.0.1:3000/[NUMBER_1]/[OPERATION]/[NUMBER_2]/[OPTIONAL: ADDITIONAL OPERATIONS AND NUMBERS]
```

Supported operations include:

- plus - Addition
- minus - Subtraction
- into - Multiplication
- divided - Division

Examples:

- `http://127.0.0.1:3000/5/plus/3` : 5 + 3
- `http://127.0.0.1:3000/3/minus/5/plus/8` : 3 - 5 + 8


### View Operation History

To view the last 20 operations:
```bash
http://127.0.0.1:3000/history
```