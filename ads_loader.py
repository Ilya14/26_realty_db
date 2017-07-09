import json
import argparse

from server import app
from models import db, Ads


def get_json_ads(json_file_name):
    with open(json_file_name, 'r') as file_handler:
        return json.load(file_handler)


def migrate(json_ads, inactive_ids):
    for json_ad in json_ads:
        ad = Ads.query.get(json_ad['id'])
        if ad is not None:
            ad = ad_update(ad, json_ad, inactive_ids)
        else:
            ad = ad_create(json_ad)
        db.session.add(ad)
    db.session.commit()


def ad_update(ad, json_ad, inactive_ids):
    ad.settlement = json_ad['settlement']
    ad.under_construction = json_ad['under_construction']
    ad.description = json_ad['description']
    ad.price = json_ad['price']
    ad.oblast_district = json_ad['oblast_district']
    ad.living_area = json_ad['living_area']
    ad.has_balcony = json_ad['has_balcony']
    ad.address = json_ad['address']
    ad.construction_year = json_ad['construction_year']
    ad.rooms_number = json_ad['rooms_number']
    ad.premise_area = json_ad['premise_area']
    if ad.active is True:
        ad.active = json_ad['id'] not in inactive_ids
    return ad


def ad_create(json_ad):
    return Ads(id=json_ad['id'],
               settlement=json_ad['settlement'],
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
               active=True)


def get_args():
    parser = argparse.ArgumentParser(description='Script for ads loading from the json-file and database up-dating')
    parser.add_argument('ads_json', help='Ads json file name')
    parser.add_argument('inactive_ids', metavar='inactive_id', type=int, nargs='*', help='ID list of outdated ads')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    json_ads = get_json_ads(args.ads_json)

    with app.app_context():
        migrate(json_ads, args.inactive_ids)
