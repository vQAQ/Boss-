# 词云图绘制
import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
from pymysql import connect
import json


# plt.rcParams['font.family'] = 'sans-serif'
# plt.rcParams['font.sans-serif'] = ['Arial']

def get_img(field, targetImageSrc, resImageSrc):
    con = connect(host='localhost', user='root', password='liujing',
                  database='bossinfo', port=3306, charset='utf8')
    cursor = con.cursor()
    sql = f"select {field} from jobinfo"
    cursor.execute(sql)
    data = cursor.fetchall()
    text = ''
    for i in data:
        if i[0] != '无':
            # 名字
            text += i[0]
            # 福利
            # companyTagsArr = json.loads(i[0])[0].split('，')
            # for j in companyTagsArr:
            #     text += j
    cursor.close()
    con.close()
    data_cut = jieba.cut(text, cut_all=False)
    stop_words = []
    with open('./stopwords.txt', 'r', encoding='gbk') as rf:
        for line in rf:
            if len(line) > 0:
                stop_words.append(line.strip())
    data_result = [x for x in data_cut if x not in stop_words]
    string = ' '.join(data_result)
    # print(string)

    # 图片
    img = Image.open(targetImageSrc)
    img_arr = np.array(img)
    wc = WordCloud(
        background_color='white',
        mask=img_arr,
        font_path='STHUPO.TTF'
    )
    wc.generate_from_text(string)

    # 绘制图片
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')
    plt.savefig(resImageSrc, dpi=800)


get_img('title', '../static/1.png',
        '../static/title_cloud.png')
