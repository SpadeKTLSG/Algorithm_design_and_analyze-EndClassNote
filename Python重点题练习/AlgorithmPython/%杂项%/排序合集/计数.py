# -*- coding: utf-8 -*-
def count_sort(arr):
    # 如果数组长度小于 2 则直接返回
    # （小于2则为有序数组）
    if len(arr) < 2:
        return arr

    max_num = max(arr)
    # 开辟一个计数列表（长度为取值范围）
    count = [0 for _ in range(max_num+1)]
    # 循环操作下标位置数+1（等于是记录每个数在数组中出现了多少次）
    for val in arr:
        count[val] += 1
    # 原数组清空，留待下面重新插入
    arr.clear()
    # 遍历计数列表中的值和下标（值的数量），
    # 从0开始，所以最终是从小到大排序
    for ind, val in enumerate(count):
        # 下面按照值中的数量进行循环
        # （通过上面累计加1我们知道：值中数量就是下标数字出现的次数）
        for i in range(val):
            # 有多少，则会追加多少次
            arr.append(ind)
    return arr