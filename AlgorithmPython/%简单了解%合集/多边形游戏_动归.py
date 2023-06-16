# -*- coding: utf-8 -*-

# 了解多边形游戏的动态规划解法即可, 复制文章来源链接: https://blog.csdn.net/mirocky/article/details/104282039
# 原作者: 连人, CSDN

# 问题描述: 已知一个n边的多边形，在n个顶点上都有一个整数，在n条边上都存在‘+’或‘*’号, 开始时，撤掉一条边。剩下的就会变成由n个顶点，n-1条边所组成的链条;
# 将其中两个相邻的顶点按之间的运算符进行运算，这两个顶点和这条边被替换为运算结果，链条被削减为n-1个顶点，n-2条边。如此反复直到最后只剩下一个点
# 多边形游戏的目的是找到最大的最后一个点。

#大佬采用了更加易懂的方法
def min_max(i, s, j, m, edge):
    
    a = m[i][s][0]
    b = m[i][s][1]
    c = m[s + 1][j][0]
    d = m[s + 1][j][1]
    if edge == '+':
        return a + c, b + d
    else:
        e = [a * c, a * d, b * c, b * d]
        minf = e[0]
        maxf = e[0]
        for k in range(1, 4):
            if minf > e[k]:
                minf = e[k]
            if maxf < e[k]:
                maxf = e[k]
        return minf, maxf


def poly_max(n, m, edge):
    for r in range(1, n):
        for i in range(0, n - r):
            j = i + r
            for s in range(i, j):
                minf, maxf = min_max(i, s, j, m, edge[s])
                if m[i][j][0] > minf:
                    m[i][j][0] = minf
                if m[i][j][1] < maxf:
                    m[i][j][1] = maxf
    return m[0][n - 1][1]


if __name__ == '__main__':
    n = int(input("一共有几条边："))

    edge = []
    vertex = []
    for i in range(0, n):
        v = int(input("第" + str(i) + "个点值为："))
        vertex.append(v)
        e = input("第" + str(i) + "个运算符为：")
        edge.append(e)

    interrupt = int(input("删掉边的序号："))
    new_vertex = vertex[interrupt + 1:n] + vertex[0:interrupt + 1]
    new_edge = edge[interrupt + 1:n] + edge[0:interrupt]

    m = []
    for i in range(0, n):
        m.append([])
        for j in range(0, n):
            if i == j:
                m[i].append([new_vertex[i], new_vertex[i]])
            else:
                m[i].append([0, 0])

    print(poly_max(n, m, new_edge))

    print(vertex)
    print(new_vertex)
    print(edge)
    print(new_edge)
    for i in range(0, n):
        for j in range(0, n):
            print(m[i][j][0], end='\t')
        print()

    print()

    for i in range(0, n):
        for j in range(0, n):
            print(m[i][j][1], end='\t')
        print()
