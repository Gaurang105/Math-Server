from flask import Flask, jsonify

app = Flask(__name__)


def process_math(operations):
    expression = ""
    for segment in operations:
        if segment == 'plus':
            expression += '+'
        elif segment == 'minus':
            expression += '-'
        elif segment == 'into':
            expression += '*'
        elif segment == 'divided':
            expression += '/'
        else:
            expression += segment

    try:
        result = eval(expression)
        return expression, result
    except Exception as e:
        return str(e), None

@app.route('/')
def index():
    return 'Welcome to the Math Server!'

if __name__ == '__main__':
    app.run(debug=True, port=3000)
