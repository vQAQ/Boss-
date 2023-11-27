from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import os
import time
import json
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boss直聘可视化数据分析.settings')
django.setup()
from myApp.models import JobInfo


class spider(object):
    def __init__(self, type, page):
        self.type = type  # 岗位关键字
        self.page = page  # 页码数
        self.spiderUrl = 'https://www.zhipin.com/web/geek/job?query=%s&city=100010000&page=%s'

    def startBrower(self):
        service = Service('D:/chromedriver.exe')
        options = webdriver.ChromeOptions()
        # 去除打开浏览器时的受到控制的提示标签
        # options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 浏览器复用
        options.add_experimental_option('debuggerAddress', 'localhost:9222')
        broweer = webdriver.Chrome(service=service, options=options)
        return broweer

    def main(self, page):
        if self.page > page:
            return
        brower = self.startBrower()
        print("正在爬取的页面的路径：" + self.spiderUrl % (self.type, self.page))
        brower.get(self.spiderUrl % (self.type, self.page))
        time.sleep(13)
        job_list = brower.find_elements(by=By.XPATH, value='//ul[@class="job-list-box"]/li')  # 30个li
        for index, job in enumerate(job_list):
            try:
                jobData = []
                print('正在爬取第%d个数据：' % (index + 1))
                # title 标题
                title = job.find_element(by=By.XPATH, value='.//span[@class="job-name"]').text
                # address 省份地址 深圳·南山区·前海
                addresses = job.find_element(by=By.XPATH, value='.//span[@class="job-area"]').text.split('·')
                address = addresses[0]
                # dist 区域
                if addresses != 1:
                    dist = addresses[1]
                else:
                    dist = ''
                # type 岗位
                type = self.type
                # educational 学历
                tag_list = job.find_elements(by=By.XPATH,
                                             value='.//a[@class="job-card-left"]/div[contains(@class,"job-info")]/ul[@class="tag-list"]/li')
                if len(tag_list) == 2:
                    # 学历
                    educational = tag_list[1].text
                    # 经验
                    workExperience = tag_list[0].text
                else:
                    educational = tag_list[2].text
                    workExperience = tag_list[1].text

                # hrName
                hrName = job.find_element(by=By.XPATH,
                                          value='.//a[@class="job-card-left"]/div[contains(@class,"job-info")]/div[@class="info-public"]').text
                # hrWork
                hrWork = job.find_element(by=By.XPATH,
                                          value='.//a[@class="job-card-left"]/div[contains(@class,"job-info")]/div[@class="info-public"]/em').text
                # 工作技能标签
                workTag = job.find_elements(by=By.XPATH,
                                            value='./div[contains(@class,"job-card-footer")]/ul[@class="tag-list"]/li')
                workTag = json.dumps(list(map(lambda x: x.text, workTag)))  # 转换为json格式
                # salary 薪资
                pratice = 0  # 是否是实习
                salaries = job.find_element(by=By.XPATH,
                                            value='.//a[@class="job-card-left"]/div[contains(@class,"job-info")]/span[@class="salary"]').text
                # 非实习单位
                if salaries.find('K') != -1:
                    salaries = salaries.split('·')
                    if len(salaries) == 1:  # 无年薪情况
                        salary = list(map(lambda x: int(x) * 1000, salaries[0].replace('K', '').split('-')))
                        # salaryMonth # 年薪情况
                        salarMonth = '0薪'
                    else:
                        salary = list(map(lambda x: int(x) * 1000, salaries[0].replace('K', '').split('-')))
                        # salaryMonth
                        salarMonth = salaries[1]
                # 实习单位
                else:
                    salary = list(map(lambda x: int(x), salaries.replace('元/天', '').split('-')))
                    # salaryMonth
                    salarMonth = '0薪'
                    pratice = 1
                # companyTitle 公司名字
                companyTitle = job.find_element(by=By.XPATH,
                                                value='.//div[@class="job-card-right"]/div[@class="company-info"]/h3/a').text
                # companyAvatar 公司头像
                companyAvatar = job.find_element(by=By.XPATH,
                                                 value='.//div[@class="job-card-right"]/div[@class="company-logo"]/a/img').get_attribute(
                    "src")
                companyInfos = job.find_elements(by=By.XPATH,
                                                 value='.//div[@class="job-card-right"]/div[@class="company-info"]/ul[@class="company-tag-list"]/li')
                if len(companyInfos) == 3:  # 有融资
                    # companyNature 公司性质
                    companyNature = companyInfos[0].text
                    # companyStatus 公司状态
                    companyStatus = companyInfos[1].text
                    # companyPeople 公司人员
                    companyPeoples = companyInfos[2].text
                    if companyPeoples != '10000人以上':
                        companyPeople = list(map(lambda x: int(x), companyInfos[2].text.replace('人', '').split('-')))
                    else:
                        companyPeople = [0, 10000]
                else:  # 无融资
                    companyNature = companyInfos[0].text
                    companyStatus = '未融资'
                    companyPeoples = companyInfos[1].text
                    if companyPeoples != '10000人以上':
                        companyPeople = list(map(lambda x: int(x), companyInfos[1].text.replace('人', '').split('-')))
                    else:
                        companyPeople = [0, 10000]
                # companyTags
                companyTags = job.find_element(by=By.XPATH,
                                               value='.//div[contains(@class,"job-card-footer")]/div[@class="info-desc"]').text
                if not companyTags:
                    companyTags = '无'
                else:
                    companyTags = json.dumps(companyTags.split(','))
                # detailUrl 招聘详情链接
                detailUrl = job.find_element(by=By.XPATH,
                                             value='.//a[@class="job-card-left"]').get_attribute('href')
                # companyUrl 公司链接
                companyUrl = job.find_element(by=By.XPATH,
                                              value='.//div[@class="job-card-right"]/div[@class="company-info"]/h3/a').get_attribute(
                    'href')

                jobData.append(title)
                jobData.append(address)
                jobData.append(type)
                jobData.append(educational)
                jobData.append(workExperience)
                jobData.append(workTag)
                jobData.append(salary)
                jobData.append(salarMonth)
                jobData.append(companyTags)
                jobData.append(hrWork)
                jobData.append(hrName)
                jobData.append(pratice)
                jobData.append(companyTitle)
                jobData.append(companyAvatar)
                jobData.append(companyNature)
                jobData.append(companyStatus)
                jobData.append(companyPeople)
                jobData.append(detailUrl)
                jobData.append(companyUrl)
                jobData.append(dist)

                self.save_to_scv(jobData)
            except:
                pass

        self.page += 1
        self.main(page)

    # 数据清洗
    def clear_csv(self):
        df = pd.read_csv('./temp.csv')
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        df['salaryMonth'] = df['salaryMonth'].map(lambda x: x.replace('薪', ''))
        print('总数据为%d' % df.shape[0])
        return df.values

    def save_to_sql(self):
        data = self.clear_csv()
        for job in data:
            # print(job)
            JobInfo.objects.create(
                title=job[0],
                address=job[1],
                type=job[2],
                educational=job[3],
                workExperience=job[4],
                workTag=job[5],
                salary=job[6],
                salarMonth=job[7],
                companyTags=job[8],
                hrWork=job[9],
                hrName=job[10],
                pratice=job[11],
                companyTitle=job[12],
                companyAvatar=job[13],
                companyNature=job[14],
                companyStatus=job[15],
                companyPeople=job[16],
                detailUrl=job[17],
                companyUrl=job[18],
                dist=job[19]
            )

    def save_to_scv(self, rowData):
        with open('./temp.csv', 'a', newline='', encoding='utf-8') as wf:
            writer = csv.writer(wf)
            writer.writerow(rowData)

    def init(self):
        if not os.path.exists('./temp.csv'):
            with open('./temp.csv', 'a', newline='', encoding='utf-8') as wf:
                writer = csv.writer(wf)
                writer.writerow(
                    ["title", "address", "type", "educational", "workExperience", "workTag", "salary", "salaryMonth",
                     "companyTags", "hrWork", "hrName", "pratice", "companyTitle", "companyAvatar", "companyNature",
                     "companyStatus", "companyPeople", "detailUrl", "companyUrl", "dist"]
                )


if __name__ == "__main__":
    spiderObj = spider('Java', 1)
    # spiderObj.init()
    # spiderObj.main(10)
    spiderObj.save_to_sql()
    # JobInfo.objects.all() # 导入模型测试
