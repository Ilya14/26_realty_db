import requests
import json

from datetime import datetime
from server import app
from models import db, Ads


def get_json_ads(url):
    return requests.get(url).json()


def json_print(json_content):
    print(json.dumps(json_content, sort_keys=True, indent=4, ensure_ascii=False))


def migrate(json_ads):
    new_building_age = 2
    for json_ad in json_ads:
        if not json_ad['under_construction']:
            age = datetime.today().year - json_ad['construction_year']
        ad = Ads(settlement=json_ad['settlement'],
                 under_construction=json_ad['under_construction'],
                 description=json_ad['description'],
                 price=json_ad['price'],
                 oblast_district=json_ad['oblast_district'],
                 living_area=json_ad['living_area'],
                 has_balcony=json_ad['has_balcony'],
                 address=json_ad['address'],
                 construction_year=json_ad['construction_year'],
                 rooms_number=json_ad['rooms_number'],
                 premise_area=json_ad['premise_area'],
                 active=age <= new_building_age)
        db.session.add(ad)
    db.session.commit()


if __name__ == '__main__':
    url = 'https://devman.org/assets/ads.json'
    json_ads = get_json_ads(url)

    with app.app_context():
        json_print(json_ads)
        migrate(json_ads)
