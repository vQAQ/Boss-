from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from myApp.models import User
from .utils.error import *
import hashlib
from .utils import getHomeData
from .utils import getSelfInfo
from .utils import getChangePasswordData
from .utils import getTableData
from .utils import getSalaryCharData
from .utils import getCompanyCharData
from .utils import getEducationalCharData
from .utils import getCompanyStatusCharData
from .utils import getAddressCharData
# from . import word_cloud_picture
from .utils.error import *
# import random


# Create your views here.
# 视图模块
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        md5 = hashlib.md5()
        md5.update(pwd.encode())
        pwd = md5.hexdigest()
        try:
            user = User.objects.get(username=uname, password=pwd)
            request.session['username'] = user.username
            return redirect('/myApp/home')
        except:
            return errorResponse(request, '用户名或密码出错')


def registry(request):
    if request.method == 'GET':
        return render(request, 'registry.html')
    else:
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        checkPwd = request.POST.get('checkPassword')
        try:
            User.objects.get(username=uname)
        except:
            if not uname or not pwd or not checkPwd:
                return errorResponse(request, '不允许为空！')
            if pwd != checkPwd:
                return errorResponse(request, '两次密码不符合！')
            # 加密
            md5 = hashlib.md5()
            md5.update(pwd.encode())
            pwd = md5.hexdigest()
            User.objects.create(username=uname, password=pwd)
            return redirect('/myApp/login')
        return errorResponse(request, '该用户名已被注册')


def logOut(request):
    request.session.clear()
    return redirect('login')


def home(request):
    uname = request.session.get('username')
    userInfo = User.objects.get(username=uname)
    yea, month, day = getHomeData.getNowTime()
    userCreateData = getHomeData.getUserCreateTime()

    return render(request, 'home.html', {
        'userInfo': userInfo,
        'dateInfo': {
            'year': yea,
            'month': month,
            'day': day
        },
        'userCreateData': userCreateData
    })


def selfInfo(request):
    uname = request.session.get('username')
    userInfo = User.objects.get(username=uname)
    educations, workExperience, jobList = getSelfInfo.getPageData()
    if request.method == 'POST':
        getSelfInfo.changeSelfInfo(request.POST, request.FILES)
        userInfo = User.objects.get(username=uname)
    return render(request, 'selfInfo.html', {
        'userInfo': userInfo,
        'pageData': {
            'educations': educations,
            'workExperience': workExperience,
            'jobList': jobList
        }
    })


def changePassword(request):
    uname = request.session.get('username')
    userInfo = User.objects.get(username=uname)
    if request.method == 'POST':
        res = getChangePasswordData.changePassword(userInfo, request.POST)
        if res != None:
            return errorResponse(request, res)
        userInfo = User.objects.get(username=uname)
    return render(request, 'changePassword.html', {
        'userInfo': userInfo
    })


def tableData(request):
    uname = request.session.get('username')
    userInfo = User.objects.get(username=uname)
    tableData = getTableData.getTableData()  # 数据统计的数据总览页面
    paginator = Paginator(tableData, 10)
    cur_page = 1
    if request.GET.get('page'):
        cur_page = int(request.GET.get('page'))
    c_page = paginator.page(cur_page)

    page_range = []
    visibleNumber = 10
    min = int(cur_page - visibleNumber / 10)
    if min < 1:
        min = 1
    max = min + visibleNumber
    if max > paginator.page_range[-1]:
        max = paginator.page_range[-1]
    for i in range(min, max):
        page_range.append(i)

    return render(request, 'tableData.html', {
        'userInfo': userInfo,
        'c_page': c_page,
        'page_range': page_range,
        'paginator': paginator
    })


def historyTableData(request):
    uname = request.session.get('username')
    userInfo = User.objects.get(username=uname)
    return render(request, 'historyTableData.html', {
        'userInfo': userInfo
    })


# 薪资情况页面
def salary(request):
    uname = request.session.get('username')
    userInfo = User.objects.get(username=uname)
    educations, workExperiences = getSalaryCharData.getPageData()
    defaultEducation = '不限'
    defaultWorkExperience = '不限'
    if request.GET.get('educational'):
        defaultEducation = request.GET.get('educational')
    if request.GET.get('workExperience'):
        defaultWorkExperience = request.GET.get('workExperience')
    # print(defaultEducation, defaultWorkExperience)
    # 图表数据
    salaryList, barData, lengends = getSalaryCharData.getBarData(defaultEducation, defaultWorkExperience)
    pieData = getSalaryCharData.pieData()
    louDouData = getSalaryCharData.getLouDouData()
    return render(request, 'salaryChar.html', {
        'userInfo': userInfo,
        'educations': educations,
        'workExperiences': workExperiences,
        'defaultEducation': defaultEducation,
        'defaultWorkExperience': defaultWorkExperience,
        'barData': barData,
        'salaryList': salaryList,
        'lengends': lengends,
        'pieData': pieData,
        'louDouData': louDouData,
    })


# 企业情况页面
def company(request):
    uname = request.session.get('username')
    userInfo = User.objects.get(username=uname)
    typeList = getCompanyCharData.getPageData()
    type = 'all'
    if request.GET.get('type'):
        type = request.GET.get('type')
    rowBarData, columnBarData = getCompanyCharData.getCompanyBar(type)
    pieData = getCompanyCharData.getCompanyPie(type)
    companyPeople, lineData = getCompanyCharData.getCompanPeople(type)
    return render(request, 'companyChar.html', {
        'userInfo': userInfo,
        'typeList': typeList,
        'type': type,
        'rowBarData': rowBarData,
        'columnBarData': columnBarData,
        'pieData': pieData,
        'companyPeople': companyPeople,
        'lineData': lineData
    })


# 福利词云页面
def companTags(request):
    uname = request.session.get('username')
    userInfo = User.objects.get(username=uname)
    return render(request, 'companyTags.html', {
        'userInfo': userInfo
    })


# 学历分布页面
def educational(request):
    uname = request.session.get('username')
    userInfo = User.objects.get(username=uname)
    defaultEducation = '不限'
    if request.GET.get('educational'):
        defaultEducation = request.GET.get('educational')
    educations = getEducationalCharData.getPageData()
    workExperiences, charDataColumnOne, charDataColumnTwo, hasEmpty = getEducationalCharData.getExpirenceData(
        defaultEducation)
    barDataRow, barDataColumn = getEducationalCharData.getPeopleData()
    return render(request, 'educationalChar.html', {
        'userInfo': userInfo,
        'educations': educations,
        'defaultEducation': defaultEducation,
        'workExperiences': workExperiences,
        'charDataColumnOne': charDataColumnOne,
        'charDataColumnTwo': charDataColumnTwo,
        'hasEmpty': hasEmpty,
        'barDataRow': barDataRow,
        'barDataColumn': barDataColumn
    })


# 企业融资页面
def companyStatus(request):
    uname = request.session.get('username')
    userInfo = User.objects.get(username=uname)
    defaultType = '不限'
    if request.GET.get('type'):
        defaultType = request.GET.get('type')
    typeList = getCompanyStatusCharData.getPageData()
    teachnologyRow, teachnologyColumn = getCompanyStatusCharData.getTechnologyData(defaultType)
    companyStatusData = getCompanyStatusCharData.getCompanyStatuData()
    return render(request, 'companyStatusChar.html', {
        'userInfo': userInfo,
        'typeList': typeList,
        'defaultType': defaultType,
        'teachnologyRow': teachnologyRow,
        'teachnologyColumn': teachnologyColumn,
        'companyStatusData': companyStatusData
    })


# 城市类型页面
def address(request):
    uname = request.session.get('username')
    userInfo = User.objects.get(username=uname)
    defaultCity = '北京'
    if request.GET.get('city'):
        defaultCity = request.GET.get('city')
    hotCities = getAddressCharData.getPageData()
    salaryRows, salaryColumns = getAddressCharData.getSalaryData(defaultCity)
    companyPeopleData = getAddressCharData.companyPeopleData(defaultCity)
    educationData = getAddressCharData.getEducationData(defaultCity)
    distData = getAddressCharData.getDistData(defaultCity)
    # 徽章城市类型页面词云图
    # randomPicture = random.randint(1, 1000000)
    # word_cloud_picture.get_img('companyTags', './static/1.png', './static/' + str(randomPicture) + '.png')
    ciyunData = getAddressCharData.getDistData(defaultCity)
    return render(request, 'addressChar.html', {
        'userInfo': userInfo,
        'hotCities': hotCities,
        'defaultCity': defaultCity,
        'salaryRows': salaryRows,
        'salaryColumns': salaryColumns,
        'companyPeopleData': companyPeopleData,
        'educationData': educationData,
        'distData': distData,
        # 'url': randomPicture,
        'ciyunData': ciyunData
    })
