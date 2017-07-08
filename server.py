import math

from flask import Flask, render_template, request
from werkzeug.contrib.fixers import ProxyFix
from models import db, Ads
from datetime import datetime

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config.from_object('config')
db.init_app(app)


def get_page(page_number, query_data):
    ads_query = Ads.query.filter_by(active=True)
    ads_query = ads_query.filter_by(oblast_district=query_data['oblast_district'])
    if query_data['min_price'] is not '':
        ads_query = ads_query.filter(Ads.price >= query_data['min_price'])
    if query_data['max_price'] is not '':
        ads_query = ads_query.filter(Ads.price <= query_data['max_price'])
    if 'new_building' in query_data:
        new_building_age = 2
        ads_query = ads_query.filter(Ads.construction_year >= datetime.today().year - new_building_age)
    ads = ads_query.order_by(Ads.price).all()
    ads_on_page = 15
    pages_count = math.ceil(len(ads) / ads_on_page)
    begin = (page_number - 1) * ads_on_page
    end = begin + ads_on_page
    return ads[begin: end], pages_count


@app.route('/')
def ads_list():
    return render_template('ads_list.html')


@app.route('/<int:page>', methods=['POST'])
def ads_page(page):
    ads, pages_count = get_page(page, request.form)
    if len(ads) == 0:
        return render_template('not_found.html')
    else:
        return render_template('ads_page.html', ads=ads, active_page=page, pages_count=pages_count)


if __name__ == '__main__':
    app.run()
