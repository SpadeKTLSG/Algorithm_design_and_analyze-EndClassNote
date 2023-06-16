# -*- coding: utf-8 -*-
#回溯法求解0-1背包问题, 最最基础的方法了(大概), 很大概率考, 但是用起来消耗太大, 正经设计算法的时候不会用
# 0-1背包问题: 有n个物品, 每个物品重量为w[i], 价值为v[i], 现在有一个容量为c的背包, 问如何选取物品放入背包, 使得背包内物品的总价值最大


# ! 多看几遍, 大概率是大题

# 定义物品数量、重量、价值和背包容量
n = 3  # 物品数量
w = [20, 15, 10]  # 物品重量
v = [20, 30, 25]  # 物品价值
c = 25  # 背包容量

# 定义一个数组x来记录物品是否放入背包
x = [False] * n

# 定义当前重量、价值和最优解
cur_w = 0  # 当前重量
cur_v = 0  # 当前价值
best_v = 0  # 最优解
best_x = 0  # 最优解对应的x值


# 定义一个回溯函数
def backtrack(i):
    global cur_w, cur_v, best_v, x, best_x
    if i == n:  # 如果已经考虑完所有物品
        if cur_v > best_v:  # 如果当前价值大于最优解
            best_v = cur_v  # 更新最优解
            best_x = x.copy()  # 保存最优解对应的x值
    else:
        if cur_w + w[i] <= c:  # 如果放入第i个物品后不超过背包容量
            x[i] = True  # 将x[i]设为True
            cur_w += w[i]  # 更新当前重量
            cur_v += v[i]  # 更新当前价值
            backtrack(i + 1)  # 考虑下一个物品
            x[i] = False  # 回溯，将x[i]设为False
            cur_w -= w[i]  # 恢复当前重量
            cur_v -= v[i]  # 恢复当前价值
        backtrack(i + 1)  # 不放入第i个物品，考虑下一个物品


# 调用回溯函数求解
backtrack(0)

# 输出结果
print("The best value is:", best_v)
print("The solution is:", best_x)
