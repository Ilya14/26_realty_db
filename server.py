from flask import Flask, make_response, redirect, render_template, request, jsonify, abort
from werkzeug.contrib.fixers import ProxyFix
from models import db, Ads


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config.from_object('config')
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def ads_list():
    if request.method == 'POST':
        return render_template('ads_panel.html')
    elif request.method == 'GET':
        return render_template('ads_list.html')


if __name__ == '__main__':
    app.run()
