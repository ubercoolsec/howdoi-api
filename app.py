#!/usr/bin/env python3

from flask import Flask, request
from howdoi import howdoi

app = Flask(__name__)

@app.route('/howdoi')
def hdi():
    query = request.args.get('query')

    if not query:
        return ''

    parser = howdoi.get_parser()
    args = vars(parser.parse_args(query.split(' ')))

    return howdoi.howdoi(args)

@app.route('/')
def readme():
    return "https://github.com/gleitz/howdoi"

if __name__ == '__main__':
    app.run()


