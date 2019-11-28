#!/usr/bin/env python3

import os

os.environ["HOWDOI_DISABLE_CACHE"] = 'true'

from flask import Flask, request
from howdoi import howdoi

app = Flask(__name__)

def _howdoi(query):
    parser = howdoi.get_parser()
    args = vars(parser.parse_args(query.split(' ')))

    return howdoi.howdoi(args)

@app.route('/telegram')
def telegram_webhook():
    body = request.data

    # TODO: Respond to bot webhook
    # https://core.telegram.org/bots/api#message

@app.route('/howdoi')
def hdi():
    query = request.args.get('query')

    if not query:
        return ''

    return _howdoi(query)

@app.route('/')
def readme():
    return "https://github.com/gleitz/howdoi"

if __name__ == '__main__':
    app.run(debug=False)


