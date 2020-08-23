from flask import Flask, request, render_template, redirect, flash
from forex_python.converter import CurrencyRates, CurrencyCodes, Decimal, RatesNotAvailableError

app = Flask(__name__)
app.config['SECRET_KEY'] = "itisasecret"
currencys=['ALL','USD','EUR','JPY','GBP','CHF','CAD','ZAR','CNH','SEK','NZD']

@app.route('/')
def homepage():
    return render_template('index.html',currency=currencys)

@app.route('/',methods=['POST'])
def form_handler():
    fromCurr = request.form.get('fromCurr')
    toCurr = request.form.get('toCurr')
    amt = request.form.get('amt')
    to_curr_symbol = CurrencyCodes().get_symbol(toCurr)
    from_curr_symbol = CurrencyCodes().get_symbol(fromCurr)
    resAmt = converter(fromCurr, toCurr, amt)
    return render_template('index.html',currency=currencys,result=f"You could get {to_curr_symbol}{resAmt} {toCurr} with {from_curr_symbol}{amt} {fromCurr}")

def converter(start,end,initAmt):
    curr_decimal = CurrencyRates(force_decimal=True)
    amt_dec = Decimal(initAmt)
    result = round(curr_decimal.convert(start,end,amt_dec),2)
    return result
