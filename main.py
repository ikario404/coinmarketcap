## main.py
import os
import json
import requests
import datetime

# flask
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import session
from flask import send_file
from flask import redirect
from flask import url_for

# ext lib
from flask_bootstrap import Bootstrap
from pprint import pprint


def create_app():
    app = Flask(__name__)
    app.config.update(
        TEMPLATES_AUTO_RELOAD=True
    )
    app._static_folder = 'static/'
    Bootstrap(app)
    return app

try:
    app = create_app()
except BaseException as e:
    print(e)

##########################################################################
# Home
##########################################################################
@app.route('/')
def home():

    btc = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=EUR')
    eth = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=EUR')
    xrp = requests.get('https://api.coinmarketcap.com/v1/ticker/ripple/?convert=EUR')
    exp = requests.get('https://api.coinmarketcap.com/v1/ticker/expanse/?convert=EUR')
    sia = requests.get('https://api.coinmarketcap.com/v1/ticker/siacoin/?convert=EUR')
    zec = requests.get('https://api.coinmarketcap.com/v1/ticker/zcash/?convert=EUR')
    zcl = requests.get('https://api.coinmarketcap.com/v1/ticker/zclassic/?convert=EUR')
    music = requests.get('https://api.coinmarketcap.com/v1/ticker/musicoin/?convert=EUR')

    data = {
        'btc' : btc.json()[0],
        'eth' : eth.json()[0],
        'xrp' : xrp.json()[0],
        'exp' : exp.json()[0],
        'sia' : sia.json()[0],
        'zec' : zec.json()[0],
        'zcl' : zcl.json()[0],
        'music' : music.json()[0]
    }
    # json.dumps(data, indent=4)
    return render_template('home.html', data=data)



@app.route('/api')
def api():
    btc = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=EUR')
    eth = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=EUR')
    xrp = requests.get('https://api.coinmarketcap.com/v1/ticker/ripple/?convert=EUR')
    exp = requests.get('https://api.coinmarketcap.com/v1/ticker/expanse/?convert=EUR')
    sia = requests.get('https://api.coinmarketcap.com/v1/ticker/siacoin/?convert=EUR')
    zec = requests.get('https://api.coinmarketcap.com/v1/ticker/zcash/?convert=EUR')
    zcl = requests.get('https://api.coinmarketcap.com/v1/ticker/zclassic/?convert=EUR')
    music = requests.get('https://api.coinmarketcap.com/v1/ticker/musicoin/?convert=EUR')

    data = {
        'btc' : btc.json()[0],
        'eth' : eth.json()[0],
        'xrp' : xrp.json()[0],
        'exp' : exp.json()[0],
        'sia' : sia.json()[0],
        'zec' : zec.json()[0],
        'zcl' : zcl.json()[0],
        'music' : music.json()[0]
    }

    return json.dumps(data, indent=4)



##########################################################################
# Start
##########################################################################
if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True,host='0.0.0.0', port=8080)
