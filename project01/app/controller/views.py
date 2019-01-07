from app import app
from flask.views import View
from flask import request


class MyMethodView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if request.method == 'GET':
            return '<h1>Hello World!</h1>This is GET method.'
        elif request.method == 'POST':
            return '<h1>Hello World!</h1>This is POST method.'


app.add_url_rule('/mmview', view_func=MyMethodView.as_view('mmview'))
