from flask import Flask, jsonify
import pickle

app = Flask(__name__)

try:
    with open('history.pkl', 'rb') as f:
        HISTORY = pickle.load(f)
except:
    HISTORY = []


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


@app.route('/<path:operation>')
def math_operation(operation):
    operations = operation.split('/')
    expression, result = process_math(operations)
    
    if result is not None:
        # Store in history
        if len(HISTORY) >= 20:
            HISTORY.pop(0)  # we'll remove the oldest operation if have 20 operations already
        HISTORY.append({"question": expression, "answer": result})
        
        # saving file
        with open('history.pkl', 'wb') as f:
            pickle.dump(HISTORY, f)
        
        return jsonify(question=expression, answer=result)
    else:
        return jsonify(error=expression), 400


# Route to display the last 20 operations.
@app.route('/history')
def history():
    return jsonify(history=HISTORY[-20:])

if __name__ == '__main__':
    app.run(debug=True, port=3000)
