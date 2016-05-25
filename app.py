
from stocks import stock_info
from flask import Flask
from futurestocks import future_stock_info
from futurestocks import growth_stock_info
from despensa import despensa_lista
from despensa import update
from despensa import update_lista
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def profits():
    sum_profit = 0
    stocks = stock_info()
    for stock in stocks:
        sum_profit += stock[9]
    return render_template('index.html', stocks = stocks, profit = sum_profit)

@app.route('/future')
def future():
    sum_profit = 0
    stocks = future_stock_info()
    return render_template('future.html', stocks = stocks)

@app.route('/growth')
def growth():
    sum_profit = 0
    stocks = growth_stock_info()
    return render_template('future.html', stocks = stocks)

@app.route('/comic')
def comic():
    return render_template('comic.html')

@app.route('/despensa')
def despensa():
    lista = despensa_lista()
    return render_template('despensa.html', lista = lista)

@app.route('/update', methods=["POST"])
def update():
    if request.method == "POST":
        prod = request.json['prod']
        kop = request.json['kop']
        lista = update_lista(prod, kop)
        return render_template('despensa.html', lista = lista)
        # get url that the user has entered



if __name__ == '__main__':
    app.debug = True
    app.run()
