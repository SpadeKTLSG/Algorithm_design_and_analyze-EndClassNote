# -*- coding: utf-8 -*-
# 

# 问题大概是 将布线区域划分成一格n*m的网格，网格内用-1来标识障碍点，求网格内一点到另一点之间的最短路径
# 就是求最短路径的问题，但是这个网格是有障碍点的，所以不能用最短路径的算法，要用分限法

# 定义一个函数来求解电路布线问题的最短路径
def find_path(start, finish, grid):
    # start是一个元组，表示起始方格的坐标
    # finish是一个元组，表示目标方格的坐标
    # grid是一个二维列表，表示电路板的封锁情况，0表示可通行，1表示不可通行
    # 返回一个整数，表示最短路径的长度
    n = len(grid) - 2  # 行数
    m = len(grid[0]) - 2  # 列数
    # 设置方格围墙，扩充边界
    for j in range(m + 2):
        grid[0][j] = 1  # 第0行全部置1
        grid[n + 1][j] = 1  # 第n+1行全部置1
    for i in range(n + 2):
        grid[i][0] = 1  # 第0列全部置1
        grid[i][m + 1] = 1  # 第m+1列全部置1
    # 初始化相对位移，上下左右
    offset = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    num_of_nbrs = 4  # 可扩展的点为四连通区域
    here = start  # 当前活结点
    grid[start[0]][start[1]] = 2  # 起始节点到起始节点的距离为2-2=0
    queue = []  # 构建活结点表的队列
    while True:
        for i in range(num_of_nbrs):  # 遍历相邻四格
            nbr = (here[0] + offset[i][0], here[1] + offset[i][1])  # 相邻方格坐标
            if grid[nbr[0]][nbr[1]] == 0:  # 如果相邻方格可通行
                grid[nbr[0]][nbr[1]] = grid[here[0]][here[1]] + 1  # 标记距离并加入活结点表
                if nbr == finish:  # 如果到达目标方格，退出循环
                    break
                queue.append(nbr)  # 将新扩展的节点加入队列
        if nbr == finish:  # 如果到达目标方格，退出循环
            break
        if not queue:  # 如果队列为空，表示无解，返回-1
            return -1
        here = queue.pop(0)  # 更新当前活结点为队首元素，并从队列中删除
    return grid[finish[0]][finish[1]] - 2  # 返回目标方格的距离减2


# 测试代码
grid = [
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 0, 0],
]
start = (3, 2)  # 起始方格坐标
finish = (4, 6)  # 目标方格坐标
path_len = find_path(start, finish, grid)  # 调用find_path函数求解最短路径长度
print("电路布线最短路径长度为：", path_len)  # 输出最短路径长度
