from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

loaded_model = pickle.load(open('XGBoost.pkl', 'rb'))


@app.route('/')
def getModel():
    return str(loaded_model)


if __name__ == '__main__':
    app.run()
