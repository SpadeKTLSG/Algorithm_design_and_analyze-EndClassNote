# -*- coding: utf-8 -*-
# 给定长度为n的整数序列，a[1…n], 求[1,n]某个子区间[i , j]，使得a[i]+…+a[j]和最大.
# 例如(-2,11,-4,13,-5,2)的最大子段和为20,所求子区间为[2,4]

# 看了看还是bing写的好, 天气太热我直接拿来主义

# 动态规划思想的体现
# 
# 确定状态：将数组的前k个元素的最大子段和表示为max_sum[k]。这样原问题就转化为求max_sum[n - 1]，其中n是数组的长度。
# 确定状态转移方程：对于任意的数组元素array[k]，有以下两种选择：（1）array[k]接着前面的子段构成最大和。（2）array[k]自己单独构成子段。
#    则，动态规划状态转移方程为max_sum[k] = max(max_sum[k - 1] + array[k], array[k])。
# 确定边界状态：当k = 0时，max_sum[0] = array[0]。
# 确定解：max(max_sum)，即max_sum中的最大值。

def max_subarray_sum(array):
    n = len(array)
    
    max_sum = [0] * n# 创建一个一维数组来存储每个子问题的解，max_sum[i]表示以array[i]结尾的最大子段和
    max_sum[0] = array[0]
    
    for i in range(1, n):
        
        max_sum[i] = max(max_sum[i - 1] + array[i], array[i])# 如果前一个元素的最大子段和为正，则加上当前元素，否则只取当前元素
    return max(max_sum)


if __name__ == '__main__':
    array = [-2, 11, -4, 13, -5, 2]
    print(max_subarray_sum(array))

