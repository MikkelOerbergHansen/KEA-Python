# pip install pandas pandas_datareader flask numpy matplotlib bs4 scikit-learn
# pip3 install pandas pandas_datareader flask numpy matplotlib bs4 scikit-learn

import pandas as pd
from flask import Flask, jsonify, render_template, redirect, request, Markup
import math
import numpy as np
import datetime
from pandas import Series, DataFrame
import pandas_datareader.data as web
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from random import randrange
import json
import requests
import os
import warnings
from scipy.linalg import LinAlgWarning
from bs4 import BeautifulSoup

# run matplotlib in backend
matplotlib.use('Agg')

# warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings(action='ignore', category=LinAlgWarning, module='sklearn')

app = Flask(__name__)

my_dir = os.path.dirname(__file__)

def generatePlot(ma1, ma2, ticker):
    def calcDate(interval):
        if interval == 'month':
            time = 30
        elif interval == 'year':
            time = 365
        elif interval == 'fiveYear':
            time = 1825
        tod = datetime.datetime.now()
        d = datetime.timedelta(days = time)
        a = tod - d
        selectedDate = a.date().isoformat()
        return selectedDate

    start_date = datetime.datetime(2019, 5, 9)
    end_date = datetime.datetime.now().date().isoformat() 
    stocks_df = web.DataReader(ticker, 'yahoo', start_date, end_date)
    closing_price_df= stocks_df['Adj Close']

    closing_price_df.index = pd.to_datetime(closing_price_df.index)

    ma_1 = closing_price_df.rolling(window=ma1).mean()
    ma_1.index = pd.to_datetime(ma_1.index)
    ma_1.dropna(inplace=True)
    ma_2 = closing_price_df.rolling(window=ma2).mean()
    ma_2.index = pd.to_datetime(ma_2.index)
    ma_2.dropna(inplace=True)

    plt.figure(figsize = (12,6))
    plt.plot(closing_price_df, label='Adj Closing Price', linewidth = 2)
    plt.plot(ma_1, label=f'{ma1} Day SMA', linewidth = 1.5)
    plt.plot(ma_2, label=f'{ma2} Day SMA', linewidth = 1.5)
    plt.xlabel('Date')
    plt.ylabel('Adjusted Closing Price ($)')
    plt.title(ticker)
    plt.legend()
    plt.savefig(os.path.join(my_dir, 'static/images/mac.png'))

def multiStock(ticker1, ticker2, ticker3, ticker4, from_date, to_date):
    def parseDate(date):
        format_str = '%m/%d/%y'
        datetime_obj = datetime.datetime.strptime(date, format_str).date().isoformat()
        return datetime_obj

    start_date = parseDate(from_date)
    end_date = parseDate(to_date)

    tickers = [ticker1, ticker2, ticker3, ticker4]
    comp_stocks_df = web.DataReader(tickers,'yahoo', start_date,end_date)['Adj Close']

    retscomp = comp_stocks_df.pct_change()
    corr = retscomp.corr()

    plt.scatter(retscomp[ticker1], retscomp[ticker2], alpha=0.3)
    plt.xlabel(f'Returns {ticker1}')
    plt.ylabel(f'Returns {ticker2}')

    plt.title(f'Returns on {ticker1} and {ticker2}')

    plt.savefig(os.path.join(my_dir, 'static/images/scatter.png'))

    plt.clf()

    plt.imshow(corr, cmap='hot', interpolation='none')
    plt.colorbar()
    plt.xticks(range(len(corr)), corr.columns)
    plt.yticks(range(len(corr)), corr.columns)
    plt.savefig(os.path.join(my_dir, 'static/images/heatmap.png'))

    plt.clf()
    
    plt.scatter(retscomp.mean(), retscomp.std())
    plt.xlabel('Expected returns')
    plt.ylabel('Risk')
    for label, x, y in zip(retscomp.columns, retscomp.mean(), retscomp.std()):
        plt.annotate(
            label, 
            xy = (x, y), xytext = (randrange(30),50),
            textcoords = 'offset points', ha = 'right', va = 'bottom',
            bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
            arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

    plt.savefig(os.path.join(my_dir, 'static/images/riskreturn.png'))

    plt.clf()

def parseDate(date):
    format_str = "%m/%d/%y"
    datetime_obj = datetime.datetime.strptime(date, format_str).date().isoformat()
    return datetime_obj

def forecast(ma1, ma2, ticker, from_date, to_date):
    plt.clf()
  
    if to_date == '0':
        end_date = datetime.datetime.now().date().isoformat()
    else:
        end_date = to_date

    start_date = parseDate(from_date)

    stocks_df = web.DataReader(ticker, 'yahoo', start_date, end_date)

    closing_price_df= stocks_df['Adj Close']

    closing_price_df.index = pd.to_datetime(closing_price_df.index)

    ma_1 = closing_price_df.rolling(window=ma1).mean()
    ma_1.index = pd.to_datetime(ma_1.index)
    ma_1.dropna(inplace=True)

    ma_2 = closing_price_df.rolling(window=ma2).mean()
    ma_2.index = pd.to_datetime(ma_2.index)
    ma_2.dropna(inplace=True)

    dfreg = stocks_df.loc[:,['Adj Close','Volume']]
    dfreg['HL_PCT'] = (stocks_df['High'] - stocks_df['Low']) / stocks_df['Close'] * 100.0
    dfreg['PCT_change'] = (stocks_df['Close'] - stocks_df['Open']) / stocks_df['Open']  * 100.0

    dfreg.fillna(value=99999, inplace = True)
    forecast_out = int(math.ceil(0.01*len(dfreg)))

    forecast_col = 'Adj Close'
    dfreg['label'] = dfreg[forecast_col].shift(-forecast_out)
    X = np.array(dfreg.drop(['label'], 1))

    # Train for model generation and evaluation 
    X_lately = X[-forecast_out:]
    X = X[:-forecast_out]

    y = np.array(dfreg['label'])
    y = y[:-forecast_out]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    
    # Linear regression
    clfreg = LinearRegression(n_jobs=-1)
    clfreg.fit(X_train, y_train)
    
    # Quadratic regression
    clfpoly2 = make_pipeline(PolynomialFeatures(2), Ridge())
    clfpoly2.fit(X_train, y_train)

    clfpoly3 = make_pipeline(PolynomialFeatures(3), Ridge())
    clfpoly3.fit(X_train, y_train)

    # KNN Regression 
    clfknn = KNeighborsRegressor(n_neighbors=2)
    clfknn.fit(X_train, y_train)

    # Evaluation 
    conf_reg = clfreg.score(X_test, y_test)
    confpoly2 = clfpoly2.score(X_test, y_test)
    confpoly3 = clfpoly3.score(X_test, y_test)
    confidenceknn = clfknn.score(X_test, y_test)

    forecast_set = clfreg.predict(X_lately)
    dfreg['Forecast'] = np.nan

    np.array([191.54990963, 188.1837365 , 185.22907692, 191.73701731,
        202.68987939, 201.99275306, 204.57470538, 204.22774733,
        206.14309605, 207.74508456, 208.88960301])
    last_date = dfreg.iloc[-1].name
    last_unix = last_date
    next_unix = last_unix + datetime.timedelta(days=1)

    for i in forecast_set:
        next_date = next_unix
        next_unix += datetime.timedelta(days=1)
        dfreg.loc[next_date] = [np.nan for _ in range(len(dfreg.columns)-1)]+[i]

    dfreg['Adj Close'].tail(500).plot(color='black')
    dfreg['Forecast'].tail(500).plot(color='orange', label='Forecast')

    forecastHTML = pd.DataFrame(dfreg['Forecast'].tail(8)).to_html(header=False)
    
    soup = BeautifulSoup(forecastHTML, 'html.parser')
    empty_cols = soup.find('thead').find_all(lambda tag: not tag.contents)
    for tag, col in zip(empty_cols, pd.DataFrame(dfreg['Forecast'].tail(8))):
        tag.string = str(col)
    finalforecastHTML = soup.decode_contents()

    def trend():
        forecastDF = dfreg['Forecast'].tail(500).dropna()
        if forecastDF.tail(1).squeeze() > forecastDF.head(1).squeeze(): 
            return 'Bullish'
        elif forecastDF.tail(1).squeeze() < forecastDF.head(1).squeeze():
            return 'Bearish'
        else:
            return 'Neutral'

    forecastedTrend = trend()

    plt.title(ticker)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.plot(ma_1, label=f'{ma1} Day SMA', linewidth = 1.5, color='pink')
    plt.plot(ma_2, label=f'{ma2} Day SMA', linewidth = 1.5, color='aqua')
    plt.legend(loc='best')

    plt.savefig(os.path.join(my_dir, 'static/images/predict.png'))
    plt.close()

    results = {
        'trend': forecastedTrend,
        'html': finalforecastHTML
    }

    return results

def scrape(stock):
    url = f'https://finviz.com/quote.ashx?t={stock}'
    header = {
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
      "X-Requested-With": "XMLHttpRequest"
    }
    r = requests.get(url, headers=header)
    dfs = pd.read_html(r.text)

    df = dfs[5]
    col1 = df[[0,1]].set_index(0)[1]
    marketCap = col1['Market Cap']
    col2 = df[[10,11]].set_index(10)[11]
    price = col2['Price']
    dailyChange = col2['Change']
    week = col2['Perf Week']
    month = col2['Perf Month']
    quarter = col2['Perf Quarter']
    
    try:
        newsList = []
        headlines = pd.read_html(r.text, attrs={'id': 'news-table'})[0][1]
        if headlines.size >= 10:
            for i in range(0, 10):
                headline = headlines[i]
                newsList.append(headline)
    except:
        print('No headlines')
        
    data = {
        'cap': marketCap,
        'price': price,
        'day': dailyChange,
        'week': week,
        'month': month,
        'quarter': quarter,
        'headlines': newsList
    }
    return data

@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/data")
def get_data():
    start_date = datetime.datetime(2016, 1, 1)
    end_date = datetime.datetime.now().date().isoformat() 
    stocks_df = web.DataReader('FB', 'yahoo', start_date, end_date)
    return jsonify(stocks_df.to_dict("records"))

@app.route("/multistock/", methods = ["GET", "POST"])
def multi():
    return render_template("multistock.html")

@app.route('/prediction/<stock>', methods=['GET', 'POST'])
def prediction(stock):
    if request.method == 'POST':
        stock = request.form['ticker']
        ticker = request.form['ticker']
        ma1 = int(request.form['ma1'])
        ma2 = int(request.form['ma2'])
        from_date = request.form['from_date']
        to_date = request.form['to_date']
        crossover = ''

        results = forecast(ma1, ma2, ticker, from_date, to_date)
        
        data = scrape(ticker)

        cap = data['cap']
        price = data['price']
        day = data['day']
        week = data['week']
        month = data['month']
        quarter = data['quarter']
        headlines = data['headlines']
        trend = results['trend']
        value = Markup(results['html'])

        return render_template("index.html", from_date=from_date, to_date=to_date, ma1=ma1, ma2=ma2, ticker=ticker, crossover=crossover, trend=trend, cap=cap, price=price, day=day, week=week, month=month, quarter=quarter, value=value, headlines=headlines)   
    else:
        return render_template('index.html')

@app.route('/multistock/', methods=["GET", "POST"])
def multistock():
    if request.method == 'POST':
        ticker1 = request.form['symbol1']
        ticker2 = request.form['symbol2']
        ticker3 = request.form['symbol3']
        ticker4 = request.form['symbol4']
        from_date = request.form['from_date']
        to_date = request.form['to_date']
        multiStock(ticker1, ticker2, ticker3, ticker4, from_date, to_date)
        return render_template('multistock.html', ticker1=ticker1, ticker2=ticker2, ticker3=ticker3, ticker4=ticker4, from_date=from_date, to_date=to_date)
    else:
        return render_template('multistock.html')

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html')

@app.errorhandler(500)
def notFound(error):
    return render_template('error.html')

if __name__ == "__main__":
    app.run()