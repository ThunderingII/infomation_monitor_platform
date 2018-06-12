import configparser
import os
import json
from core.exception.exceptions import *


class ConfigUtil(object):
    __DEFAULT_SECTION = 'CONFIG'
    __DEFAULT_FILE = 'config.ini'

    def __init__(self, config_file_path=__DEFAULT_FILE):
        self.cp = configparser.ConfigParser()
        self.config_file_path = config_file_path
        if os.path.exists(config_file_path):
            self.cp.read(config_file_path, 'utf-8')

    def put(self, key, value, section=__DEFAULT_SECTION):
        if not self.cp.has_section(section):
            self.cp.add_section(section)
        self.cp.set(section, key, value)
        self.cp.write(open(self.config_file_path, mode='w', encoding='utf-8'))

    def get(self, key, section=__DEFAULT_SECTION):
        if self.cp.has_option(section, key):
            return self.cp.get(section, key)
        return None


class JsonConfigUtil(object):
    __DEFAULT_FILE = 'config.json'

    def __init__(self, config_file_path=__DEFAULT_FILE):
        self.config_file_path = config_file_path
        if os.path.exists(config_file_path):
            with open(config_file_path, encoding='utf-8') as cf:
                self.data = json.load(cf)
        else:
            self.data = {}

    def put(self, key, value):
        if value == self.get(key):
            return
        data = self.data
        if isinstance(key, str):
            ks = key.split('.')
            for i in range(len(ks) - 1):
                if isinstance(data, dict):
                    if ks[i] not in data:
                        data[ks[i]] = {}
                    data = data[ks[i]]
                else:
                    raise ParameterException('key: %s is not a dict' % ks[i - 1])
            data[ks[len(ks) - 1]] = value
        with open(self.config_file_path, mode='w', encoding='utf-8') as cf:
            json.dump(self.data, cf, indent=4)

    def get(self, key):
        data = self.data
        if isinstance(key, str):
            ks = key.split('.')
            for i in range(len(ks)):
                if ks[i] in data:
                    data = data[ks[i]]
                else:
                    return None
            return data
        return None
