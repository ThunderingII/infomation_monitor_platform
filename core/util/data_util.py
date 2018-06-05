from bs4 import BeautifulSoup
import json
from enum import Enum


class ResponseType(Enum):
    json = 0,
    html = 1


def pre_process(data_text, type=ResponseType.json):
    if type == ResponseType.json:
        return json.loads(data_text, encoding='utf-8')
    elif type == ResponseType.html:
        return BeautifulSoup(data_text)
