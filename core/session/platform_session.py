import requests
from core.util import file_util
from core.exception import exceptions
import pickle
import time
import os
import sys


class IMP_Session(object):
    DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:17.0) Gecko/20100101 Firefox/17.0'

    def __init__(self, name='%d' % int(time.time()), user_agent=DEFAULT_USER_AGENT):
        self.create_time = time.time()
        self.session = requests.session()
        self.headers = self.session.headers
        self.headers['User-Agent'] = user_agent
        self.preserve_data = {}
        self.preserve_data_times = {}
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

    def add_value(self, key, value, preserve_times=1):
        '''
        :param key:数据的key
        :param value:数据值
        :param preserve_times:这个数据是否需要多次用到，这里就是用大的次数，-1表示永久用到，默认是1
        :return:无
        '''
        if preserve_times == -1:
            preserve_times = sys.maxsize
        self.preserve_data[key] = value
        self.preserve_data_times[key] = preserve_times

    def __generate_data(self):
        data = {}
        delete_list = []
        for key in self.preserve_data_times:
            if self.preserve_data_times[key] > 1:
                self.preserve_data_times[key] -= 1
                data[key] = self.preserve_data[key]
            elif self.preserve_data_times[key] == 1:
                data[key] = self.preserve_data[key]
                delete_list.append(key)
        for key in delete_list:
            del self.preserve_data[key]
            del self.preserve_data_times[key]
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
