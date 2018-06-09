from bs4 import BeautifulSoup
import json
from enum import Enum
import requests


class ResponseType(Enum):
    json = 0,
    html = 1


def pre_process(data, type=ResponseType.json):
    if isinstance(data, requests.models.Response):
        data = data.text
    if type == ResponseType.json:
        return json.loads(data, encoding='utf-8')
    elif type == ResponseType.html:
        return BeautifulSoup(data, 'lxml')
