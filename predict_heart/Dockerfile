FROM continuumio/anaconda3:4.4.0
MAINTAINER UNP,https://unp.education

COPY ./demo /usr/local/python

EXPOSE 8501

WORKDIR /usr/local/python

RUN pip install -r requirements.txt

CMD streamlit run predict_heart_disease.py