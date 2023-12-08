from django.urls import path, re_path
from myApp import views

# 定义各个模块的路由
urlpatterns = [
    path('login/', views.login, name='login'),
    path('registry/', views.registry, name='registry'),
    path('home/', views.home, name='home'),
    path('logOut', views.logOut, name='logOut'),
    path('selfInfo', views.selfInfo, name='selfInfo'),
    path('changePassword', views.changePassword, name='changePassword'),
    path('tableData/', views.tableData, name='tableData'),
    path('historyTableData/', views.historyTableData, name='historyTableData'),

    # 薪资情况页面
    path('salary/', views.salary, name='salary'),
    # 企业情况页面
    path('company/', views.company, name='company'),
    # 福利词云页面
    path('companyTags/', views.companTags, name='companTags'),
    # 学历分布页面
    path('educational/', views.educational, name='educational'),
    # 企业融资页面
    path('companyStatus/', views.companyStatus, name='companyStatus'),
    # 城市类型页面
    path('address/', views.address, name='address'),
]
