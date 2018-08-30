from core.auto import config_process


def test_config_check(config_file):
    # 做配置文件的检查
    code, msg = config_process.config_check(config_file)
    if code != 0:
        return msg


