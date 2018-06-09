import requests
from core.util import file_util
from core.exception import exceptions
import pickle
import time
import os


class IMP_Session(object):
    DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:17.0) Gecko/20100101 Firefox/17.0'

    def __init__(self, name='%d' % int(time.time()), user_agent=DEFAULT_USER_AGENT):
        self.create_time = time.time()
        self.session = requests.session()
        self.headers = self.session.headers
        self.headers['User-Agent'] = user_agent
        self.data = {}
        self.name = 'IMP_%s' % name
        pass

    def get(self, url, **kwargs):
        if 'params' in kwargs:
            self.session.get(url=url, **kwargs)
        response = self.session.get(url=url, params=self.__generate_data(), **kwargs)
        return response

    def post(self, url, json=None, **kwargs):
        if 'data' in kwargs:
            self.session.post(url, json=json, **kwargs)
        response = self.session.post(url, data=self.__generate_data(), json=json, **kwargs)
        return response

    def add_value(self, key, value):
        self.data[key] = value

    def __generate_data(self):
        data = self.data
        self.data = {}
        return data

    def persistence(self):
        with open(self.name, mode='wb') as psp:
            pickle.dump(self, psp)

    def get_survival_time(self):
        return time.time() - self.create_time


def load_ps(name=None):
    if name is None:
        files = os.listdir('.')
        imps = []
        for file in files:
            if 'IMP_' in file:
                imps.append(file)
        imps.sort(reverse=True)
        if len(imps) > 0:
            name = imps[0]
    if name is not None:
        try:
            with open(name, 'rb') as rpkl:
                return pickle.load(rpkl)
        except Exception as e:
            print('打开名字为%s的会话错误：%s' % (name, str(e)))
            return None
            # raise exceptions.ParameterException('打开名字为%s的会话错误：%s' % (name, str(e)))
    else:
        # raise exceptions.ParameterException('没有找到会话')
        return None
