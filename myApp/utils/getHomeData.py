from .getPublicData import *
import time


def getNowTime():
    timeFormat = time.localtime()
    yer = timeFormat.tm_year
    mon = timeFormat.tm_mon
    day = timeFormat.tm_mday
    return yer, monthList[mon - 1], day


def getUserCreateTime():
    users = getAllUsers()
    data = {}
    for u in users:
        if data.get(str(u.createTime), -1) == -1:
            data[str(u.createTime)] = 1
        else:
            data[str(u.createTime)] += 1
    result = []
    for k, v in data.items():
        result.append({
            'name': k,
            'value': v
        })
    return result
