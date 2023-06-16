# -*- coding: utf-8 -*-
# 介绍同回溯法

# ! 也挺重要

# 01背包问题-动态规划 过程:
# 定义一个二维数组dp[i][j]来表示前i个物品在背包容量为j时的最大价值，初始化为0。
# 遍历每个物品和每个容量，根据状态转移方程更新dp[i][j]的值。
# 状态转移方程有两种情况：
# 如果第i个物品的重量wi大于当前容量j，说明无法放入，那么dp[i][j]等于dp[i-1][j]，即不放入第i个物品时的最大价值。
# 如果第i个物品的重量wi小于等于当前容量j，说明可以放入，那么dp[i][j]等于max(dp[i-1][j], dp[i-1][j-wi]+vi)，即在放入和不放入第i个物品中选择一个最大价值


n = 3 # 物品数量
w = [20, 15, 10] # 物品重量
v = [20, 30, 25] # 物品价值
c = 25 # 背包容量
dp = [[0 for j in range(c+1)] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, c+1):
        if w[i-1] > j: # 如果第i个物品重量大于当前容量
            dp[i][j] = dp[i-1][j] # 不放入第i个物品
        else: # 如果第i个物品重量小于等于当前容量
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1]) # 在放入和不放入中选择最大价值


print("The best value is:", dp[n][c])

# 回溯选择了哪些物品
def backtrack(i, j):
    if i == 0 or j == 0: # 如果没有物品或者没有容量，结束回溯
        return
    if dp[i][j] == dp[i-1][j]: # 如果第i个物品没有放入，回溯到上一个物品
        backtrack(i-1, j)
    else: # 如果第i个物品放入，输出该物品的序号，并回溯到剩余容量的状态
        print("物品", i, "选中.")
        backtrack(i-1, j-w[i-1])

# 调用回溯函数
backtrack(n, c)