import datetime
import time
import random
from enum import Enum
import re
from core.exception.exceptions import *


class UTC(datetime.tzinfo):
    """UTC"""

    def __init__(self, offset=0):
        self._offset = offset

    def utcoffset(self, dt):
        return datetime.timedelta(hours=self._offset)

    def tzname(self, dt):
        return "UTC +%s" % self._offset

    def dst(self, dt):
        return datetime.timedelta(hours=self._offset)


class Mul_type(Enum):
    linear = 0,
    exponential = 1


class ExponentialSleep(object):
    def __init__(self, aim_str, m=0.7, r=0.3, mul_type=Mul_type.exponential, base_mum=2):
        self.continue_num = 0
        self.aim_str = aim_str
        self.m = m
        self.r = r
        self.base_num = base_mum
        self.mul_type = mul_type

    def judge_sleep(self, e):
        if self.aim_str in str(e):
            self.continue_num += 1
        else:
            self.continue_num = 0

        if self.mul_type == Mul_type.exponential:
            random_sleep(self.m, self.r, self.base_num ** self.continue_num)
        else:
            random_sleep(self.m, self.r, self.base_num * self.continue_num)


def random_sleep(m=0.7, r=0.3, mul=1):
    # 随机休眠时间
    time.sleep(mul * random.randint((m - r) * 100, (m + r) * 100) / 100)


def get_timestamp(time_str, tzinfo_num=8):
    p = re.compile('\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    if p.fullmatch(time_str) is not None:
        dd = time_str.split(' ')
        dds = dd[0].split('-')
        ts = dd[1].split(':')
        return datetime.datetime(int(dds[0]), int(dds[1]), int(dds[2]), int(ts[0]),
                                 int(ts[1]), int(ts[2]), 0,
                                 tzinfo=UTC(tzinfo_num)).timestamp()
    else:
        raise FormatInvalidException('格式必须为：xxxx-xx-xx HH:mm:ss')


def timer(start_time, login_operation, operation):
    times = 0
    while 1:
        timeDelay = start_time - time.time()
        if timeDelay > 0:
            print('操作时间未到:%d,还有%d小时%d分钟%d秒' % (times, timeDelay / 3600, timeDelay / 60 % 60, timeDelay % 60))
            if timeDelay > 10 * 60:
                timeSleep = 5 * 60
            elif timeDelay > 2 * 60:
                if timeDelay > 4 * 60:
                    login_operation()
                timeSleep = 60
            elif timeDelay > 13:
                timeSleep = 10
            else:
                timeSleep = 1
            print("休眠%d秒" % timeSleep)
            time.sleep(timeSleep)
        else:
            operation()
            break
