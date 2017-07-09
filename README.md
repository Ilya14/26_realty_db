# Real Estate Site

## About project

This project is intended for loading of the realtor agency ads from the 
json format to the database.

## Using

In case of the first use it is necessary to create the database:

```python
with app.app_context():
    db.create_all()
```

For modification of base it is necessary to execute:

```sh
$ python3.5 ./ads_loader.py ./ads.json
```

To hide from delivery on the site outdated ads, it is necessary to specify them by ID list.
For example:

```sh
$ python3.5 ./ads_loader.py ./ads.json 25675 21146
```

To obtain more information execute:

```sh
$ python3.5 ./ads_loader.py -h
usage: ads_loader.py [-h] ads_json [inactive_id [inactive_id ...]]

Script for ads loading from the json-file and database up-dating

positional arguments:
  ads_json     Ads json file name
  inactive_id  ID list of outdated ads

optional arguments:
  -h, --help   show this help message and exit
```

For local use of the website it is necessary to execute:

```sh
$ python3.5 ./server.py
```

The site will be available on http://127.0.0.1:5000/.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
