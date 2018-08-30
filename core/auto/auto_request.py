from core.auto import config_process
from core.util import log_util
from core.util import config_util


def main_process(main_config_file):
    log = log_util.get_logger()
    json_util = config_util.JsonConfigUtil(main_config_file)
    config_process.config_check('../../app/config_douban.json')
