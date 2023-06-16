# -*- coding: utf-8 -*-
# 二分查找的Python示例-bing
# 假设有一个已经排序的数组arr和一个目标值x
# 目标是找到x在arr中的位置，如果不存在则返回-1

def binary_search(arr, x):
    # arr是一个已经排序的数组
    # x是一个目标值
    # 定义左右两个指针，分别指向数组的首尾
    left = 0
    right = len(arr) - 1
    # 当左指针小于等于右指针时，循环执行
    while left <= right:
        # 计算中间位置
        mid = (left + right) // 2
        # 如果中间位置的元素等于目标值，返回中间位置
        if arr[mid] == x:
            return mid
        # 如果中间位置的元素小于目标值，将左指针移动到中间位置的右边
        elif arr[mid] < x:
            left = mid + 1
        # 如果中间位置的元素大于目标值，将右指针移动到中间位置的左边
        else:
            right = mid - 1
    # 如果循环结束还没有找到目标值，返回-1
    return -1

# 测试代码
arr = [1, 3, 5, 7, 9, 11, 13, 15] # 给定一个已经排序的数组
x = 9 # 给定一个目标值
result = binary_search(arr, x) # 调用函数进行二分查找
if result == -1: # 如果返回-1，表示没有找到目标值
    print(f"{x}不在数组中")
else: # 否则，打印目标值在数组中的位置
    print(f"{x}在数组中的位置是：{result}")
