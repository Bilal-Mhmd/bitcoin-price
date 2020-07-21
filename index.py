# bitcoin-price
from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/price', methods=['POST'])
def bitcoin_price():
    request.form['show price']
    response = requests.get(
        f'https://api.coindesk.com/v1/bpi/currentprice.json').json()
    t_updated = response['time']['updated']
    t_iso = response['time']['updatedISO']
    t_uk = response['time']['updateduk']
    bpi = response['bpi']
    bpi_GBP = bpi['GBP']
    bpi_EUR = bpi['EUR']

    return render_template('price.html', time_updated=t_updated, time_updatedISO=t_iso,
                           time_updateduk=t_uk, disclaimer=response['disclaimer'],
                           chartName=response['chartName'],
                           bpi_USD_code=bpi['USD']['code'],
                           bpi_USD_rate=bpi['USD']['rate'],
                           bpi_USD_symbol="$",
                           bpi_USD_description=bpi['USD']['description'],
                           bpi_GBP_code=bpi_GBP['code'],
                           bpi_GBP_symbole="£",
                           bpi_GBP_rate=bpi_GBP['rate'],
                           bpi_GBP_description=bpi_GBP['description'],
                           bpi_EUR_symbole="€",
                           bpi_EUR_rate=bpi_EUR['rate'],
                           bpi_EUR_description=bpi_EUR['description'],
                           bpi_EUR_code=bpi_EUR['code'],)


if __name__ == '__main__':
    app.run(debug=True)
