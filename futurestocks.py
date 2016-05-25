import csv
import urllib2
def future_stock_info():
    now_price_list = []
    buy_price_list = []
    stocks = []
    stocks_dict = {}
    url = 'http://finance.yahoo.com/d/quotes.csv?s=AZO+CHD+CPRT+CTAS+CVS+DHR+EXPD+FDS+FL+ICE+IEX+INGR+MTD+MYL+NKE+ORCL+PYPL+RMD+SBUX+SEIC+TMK+TMO+TSCO+WBA&f=nl1kj'
    url_euro = 'http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1&s=USDEUR=X'
    response = urllib2.urlopen(url)
    csvreader = csv.reader(response)
    stocksinternet=list(csvreader)
    sum_profit = 0
    response_euro = urllib2.urlopen(url_euro)
    csvreader_euro = csv.reader(response_euro)
    eurodolar_list = list(csvreader_euro)
    eurodolar = eurodolar_list[0][1]
    return stocksinternet

def growth_stock_info():

    url = 'http://finance.yahoo.com/d/quotes.csv?s=AMZN+BCR+BIIB+CTSH+DG+DVA+EQIX+ORLY+ROST+SRCL+TSCO+UNH&f=nl1kj'
    url_euro = 'http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1&s=USDEUR=X'
    response = urllib2.urlopen(url)
    csvreader = csv.reader(response)
    growthstocks=list(csvreader)
    response_euro = urllib2.urlopen(url_euro)
    csvreader_euro = csv.reader(response_euro)
    eurodolar_list = list(csvreader_euro)
    eurodolar = eurodolar_list[0][1]
    return growthstocks
