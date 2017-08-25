import requests
import json
import argparse
import logging

from server import app
from models import db, Ads


def get_json_ads(json_file_name):
    if json_file_name is not None:
        logging.info('Receiving ads from file "%s"...', json_file_name)
        with open(json_file_name, 'r') as file_handler:
            return json.load(file_handler)
    else:
        ads_url = 'https://devman.org/assets/ads.json'
        logging.info('Receiving ads from url  "%s"...', ads_url)
        return json.loads(requests.get(ads_url).text)


def migrate(json_ads):
    inactive_ids = get_inactive_ids(json_ads)

    for inactive_id in inactive_ids:
        ad = Ads.query.get(inactive_id)
        ad.active = False
        db.session.add(ad)

    for json_ad in json_ads:
        ad = Ads.query.get(json_ad['id'])
        if ad is not None:
            ad = ad_update(ad, json_ad)
        else:
            ad = ad_create(json_ad)
        db.session.add(ad)

    db.session.commit()


def get_inactive_ids(json_ads):
    json_ids = set([json_ad['id'] for json_ad in json_ads])
    db_ids = set([ad.ad_id for ad in Ads.query.values(Ads.ad_id)])
    return list(db_ids.difference(json_ids))


def ad_update(ad, json_ad):
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
    ad.active = True
    return ad


def ad_create(json_ad):
    return Ads(ad_id=json_ad['id'],
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
    parser = argparse.ArgumentParser(
        description='Script for ads loading from the url or json-file and database up-dating'
    )
    parser.add_argument('--file_name', help='Ads json file name')
    return parser.parse_args()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s# %(levelname)-8s [%(asctime)s] %(message)s',
        datefmt=u'%m/%d/%Y %I:%M:%S %p'
    )

    args = get_args()
    json_ads = get_json_ads(args.file_name)

    with app.app_context():
        migrate(json_ads)
