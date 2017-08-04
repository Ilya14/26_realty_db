from flask import Flask, render_template, request
from werkzeug.contrib.fixers import ProxyFix
from models import db, Ads
from datetime import datetime

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config.from_object('config')
db.init_app(app)


def get_query_params(query_data):
    return {
        'oblast_district': query_data.get('oblast_district', default=None, type=str),
        'min_price': query_data.get('min_price', default=None, type=int),
        'max_price': query_data.get('max_price', default=None, type=int),
        'new_building': query_data.get('new_building', default=None, type=bool)
    }


def get_page(query_data):
    return query_data.get('page', default=1, type=int)


def get_filtered_ads(query_params):
    ads_query = Ads.query.filter_by(active=True)
    if query_params['oblast_district'] is not None:
        ads_query = ads_query.filter_by(oblast_district=query_params['oblast_district'])
    if query_params['min_price'] is not None:
        ads_query = ads_query.filter(Ads.price >= query_params['min_price'])
    if query_params['max_price'] is not None:
        ads_query = ads_query.filter(Ads.price <= query_params['max_price'])
    if query_params['new_building']:
        new_building_age = 2
        ads_query = ads_query.filter(Ads.construction_year >= datetime.today().year - new_building_age)
    return ads_query


@app.route('/')
def ads_page():
    query_data = request.args
    query_params = get_query_params(query_data)
    filtered_ads = get_filtered_ads(query_params)
    page = get_page(query_data)
    ads_per_page = 15
    ads = filtered_ads.order_by(Ads.price).paginate(page, ads_per_page, False)
    return render_template('ads_list.html', ads=ads, params=query_params)


if __name__ == '__main__':
    app.run()
