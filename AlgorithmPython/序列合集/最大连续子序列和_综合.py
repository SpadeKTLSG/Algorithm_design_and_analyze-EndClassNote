# -*- coding: utf-8 -*-
# 在力扣写过不止一遍, 官解可以看看 https://leetcode.cn/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/
# 这里记录一些方法

# 动归
def maxSubArray1(nums):
    pre = 0  # 以某个数结尾的最大数组和
    max_nums = nums[0]  # 当前数组的最大子序和
    for num in nums:
        pre = max(pre + num, num)  # 不断迭代 pre
        max_nums = max(max_nums, pre)
    return max_nums


# 贪心
def maxSubArray2(nums):
    max_nums = nums[0]
    temp_sum = 0
    for num in nums:
        temp_sum = temp_sum + num if temp_sum > 0 else num
        #  如果 temp_sum > 0，则说明 temp_sum 对结果有增益效果，则 temp_sum 保留并加上当前遍历数字
        #  如果 temp_sum <= 0，则说明 temp_sum 对结果无增益效果，需要舍弃，则 temp_sum 直接更新为当前遍历数字
        max_nums = max(max_nums, temp_sum)
    return max_nums

# 测试:
print(maxSubArray1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))