# ====================================== Flask testing =========================
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to Home"


if __name__ == '__main__':
    app.run(debug=True)
