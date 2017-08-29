#!/usr/bin/env python
# encoding: utf-8

# python 3.6

import os
import sys
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def index():
    # return "zimuzu.tv crawler site"

    # return render_template('index.html')
    # return render_template('templates\\index.html')

@app.route('/')
@app.route('/today.html')
def today():
    from core import today

    dtdate = datetime.strftime(datetime.now(), "%m-%d")

    datas = today.update()

    # print(type(data))
    # print(datas)


    return render_template('today.html', datas=datas, dtdate=dtdate)


if __name__ == '__main__':
    app.run('127.0.0.1',23333)
