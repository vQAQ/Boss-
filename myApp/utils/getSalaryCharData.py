from .getPublicData import *
from myApp.models import JobInfo
import json


def getPageData():
    return list(educations.keys()), workExperience


# 饼图数据
def getBarData(defaultEducation, defaultWorkExperience):
    if defaultEducation == '不限' and defaultWorkExperience == '不限':
        jobs = JobInfo.objects.all()
    elif defaultWorkExperience == '不限':
        jobs = JobInfo.objects.filter(educational=defaultEducation)
    elif defaultEducation == '不限':
        jobs = JobInfo.objects.filter(workExperience=defaultWorkExperience)
    else:
        jobs = JobInfo.objects.filter(educational=defaultEducation, workExperience=defaultWorkExperience)
    jobsType = {}
    for j in jobs:
        # 实习岗位不参与柱状图制作
        if j.pratice == 0:
            if jobsType.get(j.type, -1) == -1:
                jobsType[j.type] = [json.loads(j.salary)[1]]
            else:
                jobsType[j.type].append(json.loads(j.salary)[1])
    # print(jobsType)
    # 图表数据
    barData = {}
    for k, v in jobsType.items():
        if not barData.get(k, 0):
            barData[k] = [0 for x in range(5)]
        for i in v:
            s = i / 1000
            if s < 10:
                barData[k][0] += 1
            elif s >= 10 and s < 20:
                barData[k][1] += 1
            elif s >= 20 and s < 30:
                barData[k][2] += 1
            elif s >= 30 and s < 40:
                barData[k][3] += 1
            else:
                barData[k][4] += 1
    # print(barData)

    lengends = list(barData.keys())
    if len(lengends) == 0:
        lengends = None
    return salaryList, barData, lengends


def averageFn(list):
    total = 0
    for i in list:
        total += i
    return round(total / len(list), 1)


# 饼图数据
def pieData():
    jobs = getAllJobs()
    jobsType = {}
    for j in jobs:
        if j.pratice == 0:
            if jobsType.get(j.type, -1) == -1:
                jobsType[j.type] = [json.loads(j.salary)[1]]
            else:
                jobsType[j.type].append(json.loads(j.salary)[1])
    result = []
    for k, v in jobsType.items():
        result.append({
            'name': k,
            'value': averageFn(v)
        })
    return result


# 漏斗图数据
def getLouDouData():
    jobs = JobInfo.objects.filter(salarMonth__gt=0)
    data = {}
    for j in jobs:
        x = str(j.salarMonth) + '薪'
        if data.get(x, -1) == -1:
            data[x] = 1
        else:
            data[x] += 1
    result = []
    for k, v in data.items():
        result.append({
            'name': k,
            'value': v
        })
    return result
