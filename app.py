#!/usr/bin/env python3

import os
import json
import telegram


os.environ["HOWDOI_DISABLE_CACHE"] = 'true'

from flask import Flask, request, Response
from howdoi import howdoi

TELEGRAM_BOT_START_TEXT = """
Howdy! I am the goto magic bot for your coding needs.

Forget Google and talk to me. I can respond to any of your coding queries. For example, coding `Python` and forgot about if/else syntax, just ask me

```
use condition in python
```
or, you can make it more real..

```
connect to mysql using python
```
Did you know that I speak multiple languages?

```
make http request in golang
```
Try me now! :)

"""

app = Flask(__name__)

def _howdoi(query):
    parser = howdoi.get_parser()
    args = vars(parser.parse_args(query.split(' ')))

    return howdoi.howdoi(args)

def telegram_respond_start(bot, chat_id):
    bot.send_message(chat_id=chat_id,
        text=TELEGRAM_BOT_START_TEXT,
        parse_mode=telegram.ParseMode.MARKDOWN)

def telegram_respond_text(bot, chat_id, text):
    bot.send_message(chat_id=chat_id,
        text=text,
        parse_mode=telegram.ParseMode.MARKDOWN)

@app.route('/telegram', methods = ['GET', "POST"])
def telegram_webhook():
    bot = telegram.Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])
    body = json.loads(request.data)
    chat_id = body["message"]["chat"]["id"]
    query = body["message"]["text"]

    if not query:
        return 'NO QUERY'

    if query == '/start':
        telegram_respond_start(bot, chat_id)
    else:
        text = '```\n' + _howdoi(query) + '\n```'
        telegram_respond_text(bot, chat_id, text)

    return 'OK'

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


