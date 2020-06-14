from PIL import Image
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

st.title('This is a title')
st.text('This is some text.')
st.write('Hello, *World!* :sunglasses:')

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)

code = '''def hello():
            print("Hello, Streamlit!")'''
st.code(code, language='python')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)


image = Image.open(
    "sunrise.jpg")

st.image(image, caption='Sunrise by the mountains',
         use_column_width=True)

# # ====================================== Flask testing =========================
# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return "Welcome to Home"


# if __name__ == '_main_':
#     app.run(debug=True)
