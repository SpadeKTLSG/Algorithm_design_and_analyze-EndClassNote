# -*- coding: utf-8 -*-
def heapSort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):   # 初始化大顶堆
        heapAdjust(arr, i, n)
    for i in range(n-1, 0, -1):    # 从后向前遍历数组，每次将堆顶最大值放置于位置i处
        arr[i], arr[0] = arr[0], arr[i] # 交换堆顶与待排序数组末尾位置i处
        heapAdjust(arr, 0, i) # 调整堆使其满足大顶堆
    return arr

# 调整堆为大顶堆
def heapAdjust(arr, s, m):
    t = arr[s] # 记录当前节点的值
    j = 2 * s + 1 # 节点s的左孩子
    while j < m: # 循环直到节点s没有孩子
        if j < m-1 and arr[j] < arr[j+1]: # 如果右孩子存在且比左孩子大，将j指向右孩子
            j += 1
        if t >= arr[j]: # 如果节点s的值大于等于左右孩子，则跳出循环
            break
        arr[s] = arr[j] # 将孩子节点的值赋给当前节点
        s = j # 将s指向孩子节点
        j = j * 2 + 1 # 继续递归迭代
    arr[s] = t # 将最初节点的值赋给最后得到的节点s