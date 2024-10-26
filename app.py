from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Load the HTML interface
@app.route('/')
def index():
    with open("index.html") as file:
        return render_template_string(file.read())

# Endpoint for addition
@app.route('/add', methods=['GET'])
def add():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify(result=a + b)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
