
from stocks import stock_info
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def profits():
    sum_profit = 0
    stocks = stock_info()
    for stock in stocks:
        sum_profit += stock[9]
    return render_template('index.html', stocks = stocks, profit = sum_profit)

if __name__ == '__main__':
    app.debug = True
    app.run()
