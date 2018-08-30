import logging


def get_logger(filename='STD_LOG.log', logger_name='STD_LOG', level=logging.DEBUG, file_level=logging.INFO,
               fstr='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
    # 创建一个logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    # 定义handler的输出格式
    formatter = logging.Formatter(fstr)

    if filename is not None:
        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(filename)
        fh.setLevel(file_level)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    # 给logger添加handler
    logger.addHandler(ch)
    return logger
