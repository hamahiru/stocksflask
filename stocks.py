import csv
import urllib2
def stock_info():
    now_price_list = []
    buy_price_list = []
    stocks = []
    stocks_dict = {}
    url = 'http://finance.yahoo.com/d/quotes.csv?s=AAPL+GOOG+GOOGL+MDT+GILD+FISV+CWS&f=nl1kj'
    url_euro = 'http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1&s=USDEUR=X'
    stock_info = [['AAPL',17,98],['GOOG',3,162],['GOOGL',7,162],['MDT',65,23.19],['GILD',22,81.66],['FISV',15,81.77],['CWS',50,26.01]]
    response = urllib2.urlopen(url)
    csvreader = csv.reader(response)
    stocksinternet=list(csvreader)
    for stock1, stock2 in zip(stock_info, stocksinternet):
        stocks.append(stock1+stock2)
    sum_profit = 0
    response_euro = urllib2.urlopen(url_euro)
    csvreader_euro = csv.reader(response_euro)
    eurodolar_list = list(csvreader_euro)
    eurodolar = eurodolar_list[0][1]
    for stock in stocks:
        buy_price = stock[1] * float(stock[2])
        price_now = stock[1] * float(stock[4]) * float(eurodolar)
        profit = price_now - buy_price
        sum_profit += profit
        stock.append(buy_price)
        stock.append(price_now)
        stock.append(profit)
    return stocks
