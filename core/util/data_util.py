from bs4 import BeautifulSoup
import json
from enum import Enum
import requests
from core.util.config_util import DictWrapper


class ResponseType(Enum):
    json = 0,
    html = 1


def pre_process(data, type=ResponseType.json, return_dw=True):
    if isinstance(data, requests.models.Response):
        data = data.text
    if type == ResponseType.json:
        if return_dw:
            return DictWrapper(json.loads(data, encoding='utf-8'))
        else:
            return json.loads(data, encoding='utf-8')
    elif type == ResponseType.html:
        return BeautifulSoup(data, 'lxml')
