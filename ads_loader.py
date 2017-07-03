import json
import argparse

from datetime import datetime
from server import app
from models import db, Ads


def get_json_ads(json_file_name):
    with open(json_file_name, 'r') as file_handler:
        return json.load(file_handler)


def json_print(json_content):
    print(json.dumps(json_content, sort_keys=True, indent=4, ensure_ascii=False))


def migrate(json_ads):
    new_building_age = 2
    for json_ad in json_ads:
        if json_ad['construction_year'] is not None:
            age = datetime.today().year - json_ad['construction_year']
            active = (age <= new_building_age) or json_ad['under_construction']
        else:
            active = False
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
                 active=active)
        db.session.add(ad)
    db.session.commit()


def get_args():
    parser = argparse.ArgumentParser(description='Script for ads loading from the json-file and database up-dating')
    parser.add_argument('ads_json', help='Ads json file name')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    json_ads = get_json_ads(args.ads_json)

    with app.app_context():
        json_print(json_ads)
        migrate(json_ads)
