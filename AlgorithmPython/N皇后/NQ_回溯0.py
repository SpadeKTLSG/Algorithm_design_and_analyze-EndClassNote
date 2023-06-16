# -*- coding: utf-8 -*-
# 比较基础的递归+简单回溯NQ算法, 在一行里遍历查找左上方和右上方的皇后, 用于判断是否可以放置皇后

# 定义一个函数，判断当前位置是否可以放置皇后
def is_valid(row, col, board):
    n = len(board) # 棋盘的大小
    # 检查同一列是否有冲突
    for i in range(row):
        if board[i] == col:
            return False
    # 检查左上对角线是否有冲突
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1
    # 检查右上对角线是否有冲突
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1
    # 如果没有冲突，返回True
    return True

# 定义一个函数，用递归算法解决N皇后问题
def solve_n_queens(n, board, row, solutions):
    # 如果当前行等于棋盘大小，说明已经找到一个解法，添加到解法列表中
    if row == n:
        solutions.append(board[:]) # 注意要用切片复制一份board，否则会被修改
        return
    # 遍历当前行的每一列，尝试放置皇后
    for col in range(n):
        # 如果当前位置可以放置皇后，就放置并递归到下一行
        if is_valid(row, col, board):
            board[row] = col # 放置皇后
            solve_n_queens(n, board, row + 1, solutions) # 递归到下一行
            board[row] = -1 # 回溯，撤销皇后

# 定义一个主函数，调用递归函数并打印结果
def main():
    n = int(input("请输入皇后的数量：")) # 输入皇后的数量
    board = [-1] * n # 初始化一个空棋盘，-1表示没有放置皇后
    solutions = [] # 初始化一个空列表，用来存储解法
    solve_n_queens(n, board, 0, solutions) # 调用递归函数求解
    print("共有%d种解法：" % len(solutions)) # 打印解法的数量
    for solution in solutions: # 遍历每一种解法
        print(solution,'\n') # 打印解法

main() # 调用主函数

