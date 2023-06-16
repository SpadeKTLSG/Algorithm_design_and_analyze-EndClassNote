# -*- coding: utf-8 -*-
def Insertion_Sort(unsorted_list: list):
    length = len(unsorted_list)
    # 从头开始排序
    for i in range(1, length):
        # 当前值的前一个值
        j = i - 1
        # 当前值
        key = unsorted_list[i]
        # 如果当前值小于前一个值，则交换位置，直到不需要交换为止
        while j >= 0 and key < unsorted_list[j]:
            unsorted_list[j + 1] = unsorted_list[j]
            unsorted_list[j] = key
            j -= 1
    return unsorted_list