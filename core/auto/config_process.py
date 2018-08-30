from core.util import log_util
from core.util import config_util
import json


class RequestConfigUtil():

    def __init__(self, config_file):
        json_util = config_util.JsonConfigUtil(config_file)
        self.json_util = json_util
        self.request_list = json_util.get('request_list')
        main_request_tag = 'main'
        if json_util.get('main_request_tag') is not None:
            main_request_tag = json_util.get('main_request_tag')

    def get_request(self, tag):
        for request in self.request_list:
            if tag is not None and 'request_tag' in request and request['request_tag'] == tag:
                return request
        return None

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
