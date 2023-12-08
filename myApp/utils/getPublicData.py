from myApp.models import *

monthList = ['January', 'Februry', 'Marth', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December']
educations = {'博士': 1, '硕士': 2, '本科': 3, '大专': 4, '高中': 5, '中专/中技': 6,
              '初中及以下': 7, '学历不限': 8}
workExperience = ['在校/应届生', '经验不限', '1-3年', '3-5年', '5-10年', '10年以上']
salaryList = ['0-10K', '10-20K', '20-30K', '30-40K', '40K以上']
companyPeople = ['20人以下', '100人以下', '500人以下', '1000人以下', '1万人以下', '1万人以上']
hotCity = ['北京', '上海', '深圳', '成都', '重庆', '武汉', '广州', '长沙', '衡阳']


def getAllUsers():
    return User.objects.all()


def getAllJobs():
    return JobInfo.objects.all()
