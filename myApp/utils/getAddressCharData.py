# 城市类型页面
from .getPublicData import *
from myApp.models import JobInfo
import json


def getPageData():
    return hotCity


# 城市类型左上折线图
def getSalaryData(city):
    jobs = JobInfo.objects.filter(address=city)
    salaries = []
    for i in jobs:
        if i.pratice == 0:
            salaries.append(json.loads(i.salary)[1])
    salaryColumn = [0 for x in range(len(salaryList))]
    for i in salaries:
        s = i / 1000
        if s < 10:
            salaryColumn[0] += 1
        elif s < 20:
            salaryColumn[1] += 1
        elif s < 30:
            salaryColumn[2] += 1
        elif s < 40:
            salaryColumn[3] += 1
        else:
            salaryColumn[4] += 1
    return salaryList, salaryColumn


# 城市类型右上饼图
def companyPeopleData(city):
    jobs = JobInfo.objects.filter(address=city)
    peoples = []
    for i in jobs:
        peoples.append(json.loads(i.companyPeople)[1])
    peopleColumn = [0 for x in range(len(companyPeople))]
    for p in peoples:
        if p <= 20:
            peopleColumn[0] += 1
        elif p < 100:
            peopleColumn[1] += 1
        elif p < 500:
            peopleColumn[2] += 1
        elif p < 1000:
            peopleColumn[3] += 1
        elif p < 10000:
            peopleColumn[4] += 1
        else:
            peopleColumn[5] += 1
    result = []
    for index, item in enumerate(peopleColumn):
        result.append({
            'name': companyPeople[index],
            'value': item
        })
    return result


# 漏斗图数据
def getEducationData(city):
    jobs = JobInfo.objects.filter(address=city)
    educationData = {}
    for job in jobs:
        if educationData.get(job.educational, -1) == -1:
            educationData[job.educational] = 1
        else:
            educationData[job.educational] += 1
    result = []
    for k, v in educationData.items():
        result.append({
            'name': k,
            'value': v
        })
    return result


# 饼图数据
def getDistData(city):
    jobs = JobInfo.objects.filter(address=city)
    distData = {}
    for job in jobs:
        if job.dist != '':  # 判断行政区是否为空
            if distData.get(job.dist, -1) == -1:
                distData[job.dist] = 1
            else:
                distData[job.dist] += 1
    result = []
    for k, v in distData.items():
        result.append({
            'name': k,
            'value': v
        })
    return result


# 福利词云数据
def getCiyunData(city):
    jobs = JobInfo.objects.filter(address=city)
    distData = {}
    for job in jobs:
        if job.dist != '':  # 判断行政区是否为空
            if distData.get(job.dist, -1) == -1:
                distData[job.dist] = 1
            else:
                distData[job.dist] += 1
    result = []
    for k, v in distData.items():
        result.append({
            'name': k,
            'size': v
        })
    print(result[:30])
    return result
