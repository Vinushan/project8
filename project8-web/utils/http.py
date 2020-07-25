import os
import importlib
import requests
import json

settings = importlib.import_module(os.environ.get("DJANGO_SETTINGS_MODULE"))

def __get_base_url():
    return "http://" + settings.API_HOST + ":" + settings.API_PORT


def post(url, payload, files=None):
    header = None
    response = requests.post(url=__get_base_url()+url, 
                             data=json.dumps(payload))
    return response


def get(url):
    header = None
    response = requests.get(url=__get_base_url()+url)
    return response