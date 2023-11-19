import configuration
import data
import requests


def create_order():
    respond = requests.post(configuration.URL_SERVICE+configuration.CREATE_ORDER,json=data.body)
    track = respond.json()["track"]
    return track

def get_order(param):
    respond = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,params={'t': param})
    return respond.status_code