# Generated by Django 3.2.23 on 2023-11-25 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('title', models.CharField(default='', max_length=1000, verbose_name='岗位名字')),
                ('address', models.CharField(default='', max_length=1000, verbose_name='省会')),
                ('type', models.CharField(default='', max_length=1000, verbose_name='职业')),
                ('educational', models.CharField(default='', max_length=1000, verbose_name='学历')),
                ('workExperience', models.CharField(default='', max_length=1000, verbose_name='工作经验')),
                ('workTag', models.CharField(default='', max_length=1000, verbose_name='工作标签')),
                ('salary', models.CharField(default='', max_length=1000, verbose_name='薪资')),
                ('salarMonth', models.CharField(default='', max_length=1000, verbose_name='年终奖')),
                ('companyTags', models.CharField(default='', max_length=1000, verbose_name='公司福利')),
                ('hrWork', models.CharField(default='', max_length=1000, verbose_name='人事职位')),
                ('hrName', models.CharField(default='', max_length=1000, verbose_name='人事名字')),
                ('pratice', models.BooleanField(default='', max_length=1000, verbose_name='是否为实习单位')),
                ('companyTitle', models.CharField(default='', max_length=1000, verbose_name='公司名称')),
                ('companyAvatar', models.CharField(default='', max_length=1000, verbose_name='公司头像')),
                ('companyNature', models.CharField(default='', max_length=1000, verbose_name='公司性质')),
                ('companyStatus', models.CharField(default='', max_length=1000, verbose_name='公司状态')),
                ('companyPeople', models.CharField(default='', max_length=1000, verbose_name='公司人数')),
                ('detailUrl', models.CharField(default='', max_length=1000, verbose_name='详细地址')),
                ('companyUrl', models.CharField(default='', max_length=1000, verbose_name='公司详细地址')),
                ('createTime', models.DateField(auto_now_add=True, verbose_name='创建时间')),
                ('dist', models.CharField(default='', max_length=1000, verbose_name='行政区')),
            ],
            options={
                'db_table': 'jobInfo',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('username', models.CharField(default='', max_length=1000, verbose_name='用户名')),
                ('password', models.CharField(default='', max_length=1000, verbose_name='密码')),
                ('educational', models.CharField(default='', max_length=1000, verbose_name='学历')),
                ('workExperience', models.CharField(default='', max_length=1000, verbose_name='工作经验')),
                ('address', models.CharField(default='', max_length=1000, verbose_name='意向城市')),
                ('word', models.CharField(default='', max_length=1000, verbose_name='意向岗位')),
                ('avatar', models.FileField(default='avatar/default.png', upload_to='avatar', verbose_name='用户头像')),
                ('createTime', models.DateField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('count', models.IntegerField(default=1, verbose_name='点击次数')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.jobinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.user')),
            ],
            options={
                'db_table': 'histroy',
            },
        ),
    ]
