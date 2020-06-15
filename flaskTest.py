# ====================================== Flask testing =========================
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to Home"


@app.route('/add')
def add():
    a = 10
    b = 90
    return str(a + b)


@app.route("/addParam", methods=['GET'])
def add_param():
    a = request.args.get('a')
    b = request.args.get('b')

    return str(int(a) + int(b))


if __name__ == '__main__':
    app.run(debug=True)
