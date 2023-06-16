# -*- coding: utf-8 -*-

# 两个字符串的最长公共子序列（Longest Common Sequence）
# 最长公共子序列问题是寻找两个字符串最长公共子序列的问题。不同于最长公共子串问题(简单难度)，子序列不要求在原字符串中是连续的。
# 参考文章链接 https://zhuanlan.zhihu.com/p/311598413

def lcs(A, B):
    m, n = len(A), len(B)
    # L[i][j]表示A的前i个字符和B的前j个字符的最长公共子序列长度
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):  # 计算L[i][j]
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                # 如果A的第i个字符和B的第j个字符相同，则L[i][j] = L[i-1][j-1] + 1
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                # 如果A的第i个字符和B的第j个字符不同，则L[i][j] = max(L[i-1][j], L[i][j-1])
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # 定义一个函数来打印二维数组
    def print_matrix(matrix):
        for row in matrix:
            print(" ".join(map(str, row)))

    print("长度矩阵L为:")
    print_matrix(L)

    # 回溯L求解最长公共子序列
    lcs = [] # 使用一个列表来存储最长公共子序列
    i, j = m, n
    length = L[m][n] # 使用一个变量来存储最长公共子序列的长度
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            # 如果A的第i个字符和B的第j个字符相同，则可以把它们加入最长公共子序列
            lcs.append(A[i - 1])
            # 移动到L[i-1][j-1]来处理更小的子问题
            i -= 1
            j -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            # 如果L[i-1][j] > L[i][j-1]，则说明最长公共子序列在A的第i-1个字符前面
            i -= 1
        else:
            # 如果L[i-1][j] <= L[i][j-1]，则说明最长公共子序列在B的第j-1个字符前面
            j -= 1

    print("最长公共子序列为:")
    for k in range(length):
        print(lcs[length - k - 1], end="")



if __name__ == '__main__':
    A = "ABCBDAB"
    B = "BDCABA"
    lcs(A, B)
