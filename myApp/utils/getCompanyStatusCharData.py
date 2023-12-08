# 企业融资页面
from .getPublicData import *
from myApp.models import JobInfo
import json


def getPageData():
    job = []
    jobs = getAllJobs()
    for i in jobs:
        job.append(i.type)
        return list(job)


# 市场技术排行柱状图数据
def getTechnologyData(type):
    if type == '不限':
        jobs = JobInfo.objects.all()
    else:
        jobs = JobInfo.objects.filter(type=type)
    workTagData = {}
    for job in jobs:
        workTag = json.loads(job.workTag)
        for w in workTag:
            if not w:
                break
            if workTagData.get(w, -1) == -1:
                workTagData[w] = 1
            else:
                workTagData[w] += 1
    # 排序
    result = sorted(workTagData.items(), key=lambda x: x[1], reverse=True)[:20]
    # print(result)
    teachnologyRow = []
    teachnologyColumn = []
    for k, v in result:
        teachnologyRow.append(k)
        teachnologyColumn.append(v)
    return teachnologyRow, teachnologyColumn


# 公司融资情况玫瑰图数据
def getCompanyStatuData():
    jobs = getAllJobs()
    statusData = {}
    for job in jobs:
        if statusData.get(job.companyStatus, -1) == -1:
            statusData[job.companyStatus] = 1
        else:
            statusData[job.companyStatus] += 1
    # print(statusData)
    result = []
    for k, v in statusData.items():
        result.append({
            'name': k,
            'value': v
        })
    return result
