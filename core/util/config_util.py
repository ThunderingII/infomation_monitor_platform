import configparser
import os


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
