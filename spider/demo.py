# 递归找到最大值
def max_fnc(max_list):
    if not max_list:
        return None
    max_list_f = max_fnc(max_list[1:])
    if max_list_f is None or max_list[0] > max_list_f:
        return max_list[0]
    else:
        return max_list_f


# 冒泡排序
def sort(list1):
    for i in range(len(list1) - 1):
        for j in range(len(list1) - 1 - i):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
                return list1


list01 = [1, 5, 88, 81, 56, 15]

print(max_fnc(list01))
print(sort(list01))

h1 ='https://img.bosszhipin.com/beijin/upload/com/workfeel/20230413/7bf6f160950405e9c67df4c0982aa8beb46f4b56f61450fc7c7b61c2f6bd0b01fc267a6eb1d86580.jpg?x-oss-process=image/resize,w_100,limit_0",培训机构,未融资,"[100, 499]",https://www.zhipin.com/job_detail/1a247eb9d04049a51Xd53d-1FVNT.html?lid=91GDL0fDLEA.search.58&securityId=ocBnsqRiNjCkQ-G1750EWPO8w9PiPAn8cghG1TiRiBG-rnCHUb2O-UtWLAQnqEHqcFJPxm-bRR6YznuQmgEO46dds_KXNqOwmhBxcdaEh0b65iUjoJOxeIFkb2QMtOSFKR-QPj8bVEww&sessionId=,https://www.zhipin.com/gongsi/7348508a3adc09941XV829S_FlM~.html'
h2 = '\u5e95\u85aa\u52a0\u63d0\u6210\uff0c\u901a\u8baf\u8865\u8d34\uff0c\u5458\u5de5\u65c5\u6e38\uff0c\u5e26\u85aa\u5e74\u5047\uff0c\u751f\u65e5\u798f\u5229\uff0c\u8865\u5145\u533b\u7597\u4fdd\u9669\uff0c\u5305\u4f4f\uff0c\u4fdd\u5e95\u5de5\u8d44\uff0c\u7ee9\u6548\u5956\u91d1\uff0c\u6709\u65e0\u7ebf\u7f51\uff0c\u5bbf\u820d\u6709\u7a7a\u8c03\uff0c\u96f6\u98df\u4e0b\u5348\u8336\uff0c\u4f4f\u623f\u8865\u8d34\uff0c\u56e2\u5efa\u805a\u9910\uff0c\u5b9a\u671f\u4f53\u68c0\uff0c\u8282\u65e5\u798f\u5229'
print(len(h2))