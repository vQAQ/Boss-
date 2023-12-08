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

# print(max_fnc(list01))
# print(sort(list01))