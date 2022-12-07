
from flask.templating import render_template_string
import numpy as np
import pandas as pd
import joblib
from flask import Flask,render_template,request
import sklearn
from sklearn import *

from data_processing import malicious_url, news

# start flask
app = Flask(__name__)
model_news=joblib.load(open('./pkl_files/model_pkl','rb'))
model_url=joblib.load(open('./pkl_files/random_forest_model.pkl','rb'))


# render default webpage
@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/news')
def input():
    return render_template('./predict.html')

@app.route('/malicious')
def malicious():
    return render_template('./malicious.html')

@app.route('/malicious_output', methods=['POST'])
def malicious_output():
    value=request.form["input_string"]
    print(value)
    print(type(value))
    urls=[value];
    input_news=malicious_url.URL_Converter(urls)
    # input_news=news_detect(value)
    output=model_url.predict(input_news)
    print("output", output)
    return render_template('./malicious.html',prediction_text=output)


@app.route('/predict', methods=['POST'])
def predict():
    value=request.form["input_string"]
    print(value)
    print(type(value))
    urls=[value];
    input_news=malicious_url.URL_Converter(urls)
    # input_news=news_detect(value)
    output=model_url.predict(input_news)
    print("output", output)
    return render_template('predict.html',prediction_text=output, input_value=value)



safe_websites=['github.com', 'stackoverflow.com', 'facebook.com', 'instagram.com', 'leetcode.com', 'https://guru.gndec.ac.in', 'gndec.ac.in']






if __name__ == "__main__":
    app.run(host="0.0.0.0", port="33")
    
