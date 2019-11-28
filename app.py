#!/usr/bin/env python3

import os
import json
import requests

os.environ["HOWDOI_DISABLE_CACHE"] = 'true'
telegramURL = "https://api.telegram.org/bot" + os.environ["HOWDOIBOT_API_KEY"] + "/sendMessage"

from flask import Flask, request, Response
from howdoi import howdoi

app = Flask(__name__)

def _howdoi(query):
    parser = howdoi.get_parser()
    args = vars(parser.parse_args(query.split(' ')))

    return howdoi.howdoi(args)

def telegram_respond_text(chat_id, text):
    r = {}
    r["chat_id"] = chat_id
    r["text"] = text
    headers = {'content-type': 'application/json'}

    return Response(requests.post(telegramURL, data=json.dumps(r), headers=headers))

@app.route('/telegram', methods = ['GET', "POST"])
def telegram_webhook():
    body = json.loads(request.data)
    chat_id = body["message"]["chat"]["id"]
    query = body["message"]["text"]

    if not query:
        return ''

    if query == '/start':
        return telegram_respond_text(chat_id,
            'Howdy! Tell me what you want to know about coding, such as: loop in Java')

    return telegram_respond_text(chat_id, _howdoi(query))

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
