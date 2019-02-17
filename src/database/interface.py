import pymongo
from configparser import ConfigParser
import os
import urllib


def get_config():
    current_path = os.path.abspath(os.path.dirname(__file__))
    property_file = os.path.join(current_path, 'database_config.ini')
    config = ConfigParser()
    config.read(property_file)
    return config


def get_db():
    config = get_config()
    username = urllib.parse.quote_plus(config['user']['username'])
    password = config['user']['password']
    cluster_url = config['cluster']['url']
    url = 'mongodb://' + username + ':' + password + cluster_url
    return pymongo.MongoClient(url).get_database(config['database']['name'])


def save_item(item):
    client = get_db()
    items = client.get_collection(get_config()['database']['collection_items'])
    items.insert_one(item.as_dict())


def get_list():
    client = get_db()
    items = client.get_collection(get_config()['database']['collection_items'])
    all_items = items.find()
    item_response = []
    for item in all_items:
        item_dict = dict()
        item_dict['product_sku'] = item['product_sku']
        item_dict['product_name'] = item['product_name']
        item_response.append(item_dict)
    return item_response
