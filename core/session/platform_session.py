import requests


class IMP_Session(object):
    DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:17.0) Gecko/20100101 Firefox/17.0'

    def __init__(self, user_agent=DEFAULT_USER_AGENT):
        self.session = requests.session()
        self.headers = self.session.headers
        self.headers['User-Agent'] = user_agent
        self.data = []
        pass

    def get(self, url, **kwargs):
        if 'params' in kwargs:
            self.session.get(url=url, **kwargs)
        return self.session.get(url=url, params=self.__generate_data(), **kwargs)

    def post(self, url, json=None, **kwargs):
        if 'data' in kwargs:
            self.session.post(url, json=json, **kwargs)
        return self.session.post(url, data=self.__generate_data(), json=json, **kwargs)

    def add_value(self, key, value):
        self.data[key] = value

    def __generate_data(self):
        data = self.data
        self.data = []
        return data
