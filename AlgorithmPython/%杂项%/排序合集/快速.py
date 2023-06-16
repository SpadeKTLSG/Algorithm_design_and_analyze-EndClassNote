# -*- coding: utf-8 -*-
#快速排序
def quicksort(nums, left, right):
    if left < right:
        index = partition(nums, left, right)
        quicksort(nums, left, index-1)
        quicksort(nums, index+1, right)

#划分函数
def partition(nums, left, right):
    pivot = nums[left] #选择第一个元素作为基准
    while left < right: #循环直到左右指针相遇
        while left < right and nums[right] >= pivot: #从右向左找到第一个小于基准的元素
            right -= 1
        nums[left] = nums[right] #将该元素放到基准位置
        while left < right and nums[left] <= pivot: #从左向右找到第一个大于基准的元素
            left += 1
        nums[right] = nums[left] #将该元素放到右边空位上
    nums[left] = pivot #将基准放到最终位置上
    return left #返回基准位置