#!/usr/bin/python
# -*- coding:utf-8 -*-

from bottle import route, run, template

@route('/hello/:yourwords', methods=['GET', 'POST'])
def hello(yourwords):
    return 'hello ' + yourwords

@route('/template/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='0.0.0.0', port=9700)
