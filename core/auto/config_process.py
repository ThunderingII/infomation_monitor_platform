from core.util import log_util
from core.util import config_util
from core.exception import exceptions
import json


class RequestConfigUtil():

    def __init__(self, config_file):
        json_util = config_util.JsonConfigUtil(config_file)
        self.ju = json_util
        self.request_list = json_util.get('request_list')
        self.operation_list = json_util.get('operation_list')
        if json_util.get('main_request_name') is not None:
            self.mrn = json_util.get('main_request_name')
        if self.mrn == None:
            raise exceptions.ConfigError(f'cannot find main request name')

    def get_request(self, name):
        for request in self.request_list:
            if name is not None and 'name' in request and request['name'] == name:
                # todo should write a cache
                return config_util.DictWrapper(request)
        raise exceptions.ConfigError(f'cannot find a request named "{name}"')

    def get_operation(self, name):
        for operation in self.operation_list:
            if name is not None and 'name' in operation and operation['name'] == name:
                return config_util.DictWrapper(operation)
        raise exceptions.ConfigError(f'cannot find a operation named "{name}"')

    def config_check(config_file: object) -> object:
        code = 0
        msg = ''
        # todo 完成config检查，有误可以raise Exception
        return code, msg
        # with open(config_file, encoding='utf-8') as cf:
        #     config = json.load(cf)
        #
        #     print(config.keys())
        #     if config.request_list != None:
        #         print(config.request_list)

    def request_check(request_list, main_request_name):
        # for request in request_list:
        pass
