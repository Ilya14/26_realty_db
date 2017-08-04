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

For modification of base with use of the url https://devman.org/assets/ads.json it is necessary to execute:

```sh
$ python3.5 ./ads_loader.py
```

or with use of the json-file:
```sh
$ python3.5 ./ads_loader.py --file_name=./ads.json
```

To obtain more information execute:

```sh
$ python3.5 ./ads_loader.py -h
usage: ads_loader.py [-h] [--file_name FILE_NAME]

Script for ads loading from the url or json-file and database up-dating

optional arguments:
  -h, --help            show this help message and exit
  --file_name FILE_NAME
                        Ads json file name
```

For local use of the site it is necessary to execute:

```sh
$ python3.5 ./server.py
```

The site will be available on http://127.0.0.1:5000/.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
