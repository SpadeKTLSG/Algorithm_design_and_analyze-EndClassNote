# -*- coding: utf-8 -*-
# 这里的装载是复杂装载, 问题描述: 有一批共n个集装箱要装 上两艘载重量分别为c1和c2的轮船,其中集装箱i的重量为wi ,且w1+++..+wn≤c1+c2
# 那么, 最最基础的递归思路就是: 从第一个集装箱开始, 有两种选择, 装入第一艘轮船或者不装入第一艘轮船, 然后递归处理后续的集装箱

# 抄模板完事.

# 定义物品数量、重量和轮船容量
n = 3  # 物品数量
w = [20, 15, 10]  # 物品重量
c1 = 20  # 轮船1容量
c2 = 25  # 轮船2容量

# 定义全局变量
best_value = 0  # 当前最优解的价值
best_solution = [0] * n  # 当前最优解对应的选择方案
current_value = 0  # 当前子问题的价值
current_solution = [0] * n  # 当前子问题对应的选择方案
c2_value = 0  # 当前子问题中装入第二艘轮船的集装箱的总重量


# 定义递归函数
def backtrack(i):
    global best_value, best_solution, current_value, current_solution, c2_value
    if i == n:  # 基准情形，所有集装箱都已处理完毕
        if current_value > best_value:  # 如果当前价值大于最优价值
            best_value = current_value  # 更新最优价值
            best_solution = current_solution.copy()  # 更新最优方案
            print("The best value is:", best_value)  # 输出最优价值
            print("The first ship has:", current_value, "weight of items")  # 输出第一艘轮船的集装箱重量
            print("The second ship has:", c2_value, "weight of items")  # 输出第二艘轮船的集装箱重量
        return True  # 返回True表示找到了一个可行解或者最优解
    else:  # 非基准情形，处理第i个集装箱的选择问题
        result = False  # 初始化结果为False
        for j in [1, 0]:  # 遍历两种选择，1表示装入第一艘轮船，0表示不装入任何轮船
            if j == 1:  # 如果选择装入第一艘轮船
                if current_value + w[i] <= c1:  # 如果满足约束条件
                    current_value += w[i]  # 更新当前价值
                    current_solution[i] = j  # 更新当前方案
                    result = backtrack(i + 1) or result  # 递归调用并更新结果
                    current_value -= w[i]  # 恢复当前价值
                    current_solution[i] = 0  # 恢复当前方案
            else:  # 如果选择不装入任何轮船，即装入第二艘轮船（假设第二艘轮船只装入剩余无法装入第一艘轮船的集装箱）
                if c2_value + w[i] <= c2:  # 如果满足约束条件
                    c2_value += w[i]  # 更新第二艘轮船的集装箱重量
                    result = backtrack(i + 1) or result  # 递归调用并更新结果
                    c2_value -= w[i]  # 恢复第二艘轮船的集装箱重量
        return result  # 返回结果


backtrack(0)
