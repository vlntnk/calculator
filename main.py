from flask import Flask, render_template, jsonify, request


app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.route('/calc', methods=['POST', 'GET'])
def calc():
    expression = request.get_json()
    if expression and 'expression' in expression:
        try:
            result = eval(expression['expression'])
        except ZeroDivisionError:
            result = 'Error'
        data = {'result': result}
    else:
        data = {'result': 'server error'}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000,load_dotenv=True)