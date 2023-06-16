# -*- coding: utf-8 -*-

# 不要求, 这里偷懒了, 没有经过验证! 
# ! 警告, 代码很可能不能运行
def count_n_queens(n):

    # 初始化一个二维数组，dp[i][j]表示在前i行中放置j个皇后的解法个数
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    # 初始化边界条件，dp[0][0] = 1，表示在0行中放置0个皇后有1种解法
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if is_valid(i, j, dp):
                # 则当前位置的解法个数等于上一行放置j-1个皇后的解法个数加上上一行放置j个皇后的解法个数
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                # 否则当前位置的解法个数等于上一行放置j个皇后的解法个数
                dp[i][j] = dp[i - 1][j]
    return dp[n][n]

def is_valid(row, col, dp):

    # 检查当前行的其他列是否有皇后
    for k in range(1, col): # 新增循环
        if dp[row][k] > 0: # 如果有皇后
            return False # 返回False

    for i in range(1, row):
        if dp[i][col] > 0 or (col - (row - i) > 0 and dp[i][col - (row - i)] > 0) or (col + (row - i) <= len(dp) - 1 and dp[i][col + (row - i)] > 0):
            return False
    return True




