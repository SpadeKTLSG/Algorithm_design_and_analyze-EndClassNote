# -*- coding: utf-8 -*-
def shell_sort(arr):
    d = len(arr) // 2 # 整除
    while d > 0:
        for i in range(d, len(arr)):
            temp = arr[i]
            j = i - d
            while j >= 0 and temp < arr[j]:
                arr[j + d] = arr[j]
                j -= d
            arr[j + d] = temp
        d //= 2 # 更新间隔
    return arr