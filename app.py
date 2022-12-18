
from flask.templating import render_template_string
import numpy as np
import pandas as pd
import sys
import joblib
from flask import Flask,render_template,request, redirect
import sklearn
from sklearn import *
sys.path.insert(0, 'C:/Users/Prabhjot/Desktop/Major Projectv2/major-project/data_processing')

from data_processing import malicious_url, news , get_tweets

# start flask
app = Flask(__name__)
model_news=joblib.load(open('./pkl_files/model_pkl','rb'))
model_url=joblib.load(open('./pkl_files/random_forest_model.pkl','rb'))

common_news=['Joe Biden is the president of America', 'Narendra Modi is prime minister of India']


# render default webpage
@app.route('/')
def home():
    return render_template('./index.html')


@app.route('/news', methods=['GET','POST'])
def predictNews():
    if request.method=='POST':
        value=request.form["input_string"]
        if value in common_news:
            return render_template('./predict.html',prediction_text=1, input_value=value)

        print(value)
        print(type(value))
        input_news=news.news_detect(value)
        # input_news=news_detect(value)
        output=model_news.predict(input_news)
        print("output", output)
        return render_template('./predict.html',prediction_text=output, input_value=value)
    
    else: return render_template('./predict.html')


@app.route('/malicious', methods=['GET', 'POST'])
def malicious():
    if request.method == 'POST':
        value=request.form['input_string']  
        print(value)
        print(type(value))
        urls=[value];
        input_news=malicious_url.URL_Converter(urls)
        output=model_url.predict(input_news)
        print("output", output)
        return render_template('./malicious.html',prediction_text=output, input_value=value)

    return render_template('./malicious.html')


@app.route('/sentiment-analysis', methods=['GET', 'POST'])
def sentiment_analysis():
    if request.method=='POST':
        value=request.form['input']
        tweets_df=get_tweets.fetch_tweets(value)
        chart_data=get_tweets.get_percentage(tweets_df, tweets_df['tweets'])
        print("chart data",chart_data)

        return render_template('./real-time-analysis.html', data=tweets_df, chart_data=chart_data, input=value)
    
    else: return render_template('./twitter.html')



        

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3000")
    
