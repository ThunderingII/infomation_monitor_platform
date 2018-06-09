from core.util import time_util


def write(data, file_name=None, mode='w', encoding='utf-8'):
    if file_name is None:
        file_name = time_util.get_time_str().replace(' ', '-').replace(':', '-')
    file = open(file_name, mode=mode, encoding=encoding)
    file.write(data)
    file.close()
