from django.shortcuts import render, redirect
from myApp.models import User
from .utils.error import *
import hashlib


# Create your views here.
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


def home(request):
    return render(request, 'index.html')
