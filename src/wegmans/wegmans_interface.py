from configparser import ConfigParser
import os
import requests
from models.Item import Item


def get_config():
    current_path = os.path.abspath(os.path.dirname(__file__))
    property_file = os.path.join(current_path, 'wegmans.ini')
    config = ConfigParser()
    config.read(property_file)
    return config


def get_by_keyword(keyword):
    config = get_config()
    request_url = config['api']['product_url'] + '/search?query=' + keyword + '&' + config['api']['api_version'] + '&' + config['api']['product_key']
    response = requests.get(request_url)
    item_sku = int(response.json()['results'][0]['sku'])
    item_name = response.json()['results'][0]['name']
    return Item(item_sku, item_name)
