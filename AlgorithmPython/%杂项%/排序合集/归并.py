# -*- coding: utf-8 -*-
def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist

    num = len(alist)//2    # 二分分解
    left = merge_sort(alist[:num])    # left 采用归并排序后形成的有序的新的列表
    right = merge_sort(alist[num:])    # right 采用归并排序后形成的有序的新的列表
    # 将两个有序的子序列合并为一个新的整体 merge(left, right)
    left_point, right_point = 0, 0
    result = []
    while left_point < len(left) and right_point < len(right):
        if left[left_point] <= right[right_point]:
            result.append(left[left_point])
            left_point += 1
        else:
            result.append(right[right_point])
            right_point += 1
    result += left[left_point:]
    result += right[right_point:]
    return result