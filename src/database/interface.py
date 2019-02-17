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
