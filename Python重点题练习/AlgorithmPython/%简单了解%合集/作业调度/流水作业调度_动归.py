# -*- coding: utf-8 -*-
# 同之前, 用自底向上动态规划+DP, 求解流水作业调度问题; 假设有5个作业，每个作业在两台机器上的加工时间如下

a = [2, 3, 2, 4]  # 在机器M1上的加工时间
b = [3, 1, 5, 3]  # 在机器M2上的加工时间
n = len(a)  # 作业数量

# 定义一个二维数组dp，dp[i][j]表示完成前i个作业在机器M2上的等待时间为j时的最小完成时间
dp = [[float('inf')] * (sum(b) + 1) for _ in range(n + 1)]
dp[0][0] = 0  # 初始化边界条件，当没有作业时，完成时间为0

# 回溯找出最优调度序列
best = 0
bestx = []  # 最优路径 (调度)
all_bestx = []  # 所有的最优路径 (调度)


def waterwork():
    global best
    for i in range(1, n + 1):  # 遍历每个作业
        for j in range(sum(b) + 1):  # 遍历每种等待时间
            if j >= b[i - 1]:  # 如果等待时间大于等于当前作业在M2上的加工时间
                # !则有两种选择：安排当前作业或不安排当前作业: 取两者中的较小值作为最优解
                # ?如果安排当前作业，则完成时间为max(dp[i - 1][j - b[i - 1]] + a[i - 1], j)
                # ?如果不安排当前作业，则完成时间为dp[i - 1][j] + a[i - 1]
                dp[i][j] = min(max(dp[i - 1][j - b[i - 1]] + a[i - 1], j), dp[i - 1][j] + a[i - 1])
            else:
                # 如果等待时间小于当前作业在M2上的加工时间, 则只能选择不安排当前作业(废话!)
                dp[i][j] = dp[i - 1][j] + a[i - 1]

    best = min(dp[n])  # 找出最优值，即dp[n]中的最小值


def backtrack(i, j):
    global bestx, all_bestx, dp, a, b

    if i == 0:  # 到达根节点，保存一条最优路径
        all_bestx.append(bestx[:])

    else:
        if j >= b[i - 1] and dp[i][j] == max(dp[i - 1][j - b[i - 1]] + a[i - 1], j):  # 如果安排了当前作业
            bestx.append(i)  # 将当前作业加入最优路径
            backtrack(i - 1, j - b[i - 1])  # 回溯到上一层节点
            bestx.pop()  # 移除当前作业
        if dp[i][j] == dp[i - 1][j] + a[i - 1]:  # 如果不安排当前作业
            bestx.append(i)  # 将当前作业加入最优路径
            backtrack(i - 1, j)  # 回溯到上一层节点
            bestx.pop()  # 移除当前作业


if __name__ == '__main__':

    waterwork()  # 调用动态规划函数，求解最优值
    backtrack(n, dp[n].index(best))  # 调用回溯函数，找出所有的最优解

    print("最优值：", best, "\n所有的最优解：")
    for x in all_bestx:
        x.reverse()  # 反转最优路径，使其按照顺序排列
        print(x)
