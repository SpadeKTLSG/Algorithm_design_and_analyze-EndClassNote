# -*- coding: utf-8 -*-

# 矩阵连乘问题的动态规划算法解决
# 假设有n个矩阵相乘，矩阵i的维度为p[i-1] x p[i],目标是找到最少的标量乘法次数

# 使用两个二维数组m和s来存储最优解:
# m[i][j]表示矩阵i到j相乘的最少乘法次数
# s[i][j]表示矩阵i到j相乘时的最优分割点

def matrix_chain_order(p):
    # p是一个一维数组，存储每个矩阵的行数和列数
    # p的长度应该是n+1，其中n是矩阵的个数
    n = len(p) - 1 # 矩阵的个数
    m = [[0 for _ in range(n+1)] for _ in range(n+1)] # 初始化m为全零矩阵
    s = [[0 for _ in range(n+1)] for _ in range(n+1)] # 初始化s为全零矩阵
    for l in range(2, n+1): # l表示子问题的规模，从2到n
        for i in range(1, n-l+2): # i表示子问题的起始矩阵，从1到n-l+1
            j = i + l - 1 # j表示子问题的终止矩阵，等于i+l-1
            m[i][j] = float('inf') # 将m[i][j]设为无穷大，表示还没有找到最优解
            for k in range(i, j): # k表示分割点，从i到j-1
                # 计算以k为分割点的乘法次数
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]: # 如果比当前最优解小，更新最优解和分割点
                    m[i][j] = q
                    s[i][j] = k
    return m, s

def print_optimal_parens(s, i, j):
    # s是一个二维数组，存储每个子问题的最优分割点
    # i和j表示要打印的子问题的起始和终止矩阵
    if i == j: # 如果只有一个矩阵，直接打印其编号
        print(f"A{i}", end="")
    else: # 否则，按照分割点递归地打印左右两部分，并加上括号
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j]+1, j)
        print(")", end="")

# 测试代码
p = [30, 35, 15, 5, 10, 20, 25] # 给定7个矩阵的维度
m, s = matrix_chain_order(p) # 调用函数求解最优解
print(f"最少的标量乘法次数是：{m[1][6]}") # 打印最少的标量乘法次数
print("最优的加括号方式是：", end="")
print_optimal_parens(s, 1, 6) # 打印最优的加括号方式
