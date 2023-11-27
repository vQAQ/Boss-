from django.db import models


# Create your models here.
class JobInfo(models.Model):
    id = models.AutoField('id', primary_key=True)
    title = models.CharField('岗位名字', max_length=1000, default='')
    address = models.CharField('省会', max_length=1000, default='')
    type = models.CharField('职业', max_length=1000, default='')
    educational = models.CharField('学历', max_length=1000, default='')
    workExperience = models.CharField('工作经验', max_length=1000, default='')
    workTag = models.CharField('工作标签', max_length=1000, default='')
    salary = models.CharField('薪资', max_length=1000, default='')
    salarMonth = models.CharField('年终奖', max_length=1000, default='')
    companyTags = models.CharField('公司福利', max_length=1000, default='')
    hrWork = models.CharField('人事职位', max_length=1000, default='')
    hrName = models.CharField('人事名字', max_length=1000, default='')
    pratice = models.BooleanField('是否为实习单位', max_length=1000, default='')
    companyTitle = models.CharField('公司名称', max_length=1000, default='')
    companyAvatar = models.CharField('公司头像', max_length=1000, default='')
    companyNature = models.CharField('公司性质', max_length=1000, default='')
    companyStatus = models.CharField('公司状态', max_length=1000, default='')
    companyPeople = models.CharField('公司人数', max_length=1000, default='')
    detailUrl = models.CharField('详细地址', max_length=1000, default='')
    companyUrl = models.CharField('公司详细地址', max_length=1000, default='')
    createTime = models.DateField('创建时间', auto_now_add=True)
    dist = models.CharField('行政区', max_length=1000, default='')

    class Meta:
        db_table = 'jobInfo'


# 个人信息
class User(models.Model):
    id = models.AutoField('id', primary_key=True)
    username = models.CharField('用户名', max_length=1000, default='')
    password = models.CharField('密码', max_length=1000, default='')
    educational = models.CharField('学历', max_length=1000, default='')
    workExperience = models.CharField('工作经验', max_length=1000, default='')
    address = models.CharField('意向城市', max_length=1000, default='')
    word = models.CharField('意向岗位', max_length=1000, default='')
    avatar = models.FileField('用户头像', upload_to='avatar', default='avatar/default.png')
    createTime = models.DateField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'user'


# 历史查阅页面
class History(models.Model):
    id = models.AutoField('id', primary_key=True)
    job = models.ForeignKey(JobInfo, on_delete=models.CASCADE)  # 两个关联外键，删除一个，另一个跟着删除
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 外键
    count = models.IntegerField('点击次数', default=1)

    class Meta:
        db_table = 'histroy'
