# -*- coding: utf-8 -*-
# 流水作业调度的最终目标是要求完成所有任务的时间最短，所以把最后一个任务的完成时间作为标准；
# 而批处理作业调度的目的是要让每一个作业都尽快得到处理，所以要把每个作业的完成时间之和作为标准
# 这内容差不多, 就放一块
#
# 假设有4个作业，每个作业在两台机器上的加工时间如下
a = [2, 3, 2, 4]  # 在机器M1上的加工时间
b = [3, 1, 5, 3]  # 在机器M2上的加工时间
n = len(a)  # 作业数量

best = float('inf')  # 最优值 (完成全部任务的最早时间)
bestx = [0] * n  # 最优路径 (调度)
x = []  # 当前路径 (调度)
used = [False] * n  # 记录当前枝条已走过哪些点


# 计算任务完成的时间
def comp():
    f1 = 0  # M1上的累计时间
    f2 = 0  # M2上的累计时间
    for i in x:
        f1 += a[i]
        f2 = max(f1, f2) + b[i]
    return f2


# 以深度优先遍历方式遍历解空间树
def search(depth):
    global best, bestx, x, used
    if depth == n:  # 到达叶节点
        tmp = comp()  # 计算当前路径的完成时间
        if tmp < best:  # 更新最优值和最优路径
            best = tmp
            bestx = x[:]
    else:
        for i in range(n):
            if not used[i]:  # 如果作业i还没有被安排
                used[i] = True  # 标记作业i已被安排
                x.append(i)  # 将作业i加入当前路径
                if comp() < best:  # 简单剪枝函数，如果当前路径的完成时间小于最优值，继续搜索
                    search(depth + 1)  # dive into the next level
                x.pop()  # 回溯，将作业i从当前路径中移除
                used[i] = False  # 取消标记作业i已被安排


if __name__ == '__main__':
    search(0)
    print("最优值：", best)
    print("最优解：", [i + 1 for i in bestx])
