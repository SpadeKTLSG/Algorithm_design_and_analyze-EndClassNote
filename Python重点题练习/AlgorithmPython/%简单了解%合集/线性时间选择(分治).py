# -*- coding: utf-8 -*-
# 给定线性序集中n个元素和一个正数k, 要求找出这n个元素中第k小的元素
import random


def linear_time_select(arr, k):
    # arr是一个无序的数组
    # k是一个整数，表示要找的排名
    # 如果数组为空或k超出范围，返回None
    if not arr or k < 1 or k > len(arr):
        return None
    # 否则，调用辅助函数进行递归查找
    return select(arr, 0, len(arr) - 1, k)

def select(arr, left, right, k):
    # arr是一个无序的数组
    # left和right是数组的左右边界
    # k是一个整数，表示要找的排名
    
    if left == right: # 如果数组只有一个元素，直接返回该元素
        return arr[left]
    
    pivot_index = partition(arr, left, right) # 否则，调用partition函数进行划分，并得到划分点的位置
    
    rank = pivot_index - left + 1# 计算划分点的排名
    
    if rank == k: # 如果划分点的排名等于k，返回划分点的元素
        return arr[pivot_index]
    
    elif rank > k: # 如果划分点的排名大于k，递归地在左半部分查找第k小的元素
        return select(arr, left, pivot_index - 1, k)
    
    else: # 如果划分点的排名小于k，递归地在右半部分查找第k-rank小的元素
        return select(arr, pivot_index + 1, right, k - rank)

def partition(arr, left, right): # 将子数组划分成两部分，以一个随机选择的主元为界。函数然后比较主元的排名和k，并决定在哪一部分递归查找。
    # arr是一个无序的数组
    # left和right是数组的左右边界
    # 随机选择一个元素作为主元，并将其交换到右边界 (随机思想)
    pivot_index = random.randint(left, right)
    pivot = arr[pivot_index]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    # 定义一个指针i，指向左边界-1的位置
    i = left - 1
    # 遍历数组，从左边界到右边界-1的位置
    for j in range(left, right):
        # 如果当前元素小于等于主元，将其交换到i+1的位置，并将i向右移动一位
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # 最后，将主元交换到i+1的位置，并返回该位置作为划分点
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i + 1

# 测试代码
arr = [5,3,8,2,6,9,4,7,1] # 给定一个无序的数组
k = 3 # 给定一个整数k
result = linear_time_select(arr, k) # 调用函数进行线性时间选择
if result is None: # 如果返回None，表示输入无效
    print(f"输入无效")
else: # 否则，打印第k小的元素
    print(f"第{k}小的元素是：{result}")

#最坏情况下的时间复杂度是O(n^2)，但是一个期望的时间复杂度是O(n)，其中n是数组的大小。这是因为算法的性能取决于主元如何将子数组划分成两个平衡的部分。
# 如果我们每次都能够选择一个好的主元，我们可以在每一步将问题规模减半，并达到线性时间复杂度。