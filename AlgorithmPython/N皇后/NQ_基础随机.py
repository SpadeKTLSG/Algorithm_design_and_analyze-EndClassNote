# -*- coding: utf-8 -*-
# 模拟退火和遗传是高级的随机算法，这里不做介绍, 展示最最初级的乱放方法, 在棋盘上随机放置皇后, 然后判断是否冲突, 如果冲突就重新放置, 直到不冲突为止
# 乱放的方法是最简单的, 但是效率很低, 一般用于验证其他算法的正确性, 也可以用于求解小规模的问题

# 同样很容易想到优化的乱放方法, 一行很明显只能放一个, 这样记录每个皇后的列号,然后修改冲突判定函数, 使其只判断列冲突即可, 这样就可以大大减少判断的次数
# 关于输出可以参考国际象棋网站的编辑器, 连皇后都给你准备好了. 
import random

# 定义一个函数，判断一个棋盘是否有冲突
def is_conflict(board):
    n = len(board) # 棋盘的大小
    for i in range(n):
        for j in range(i+1, n):
            # 如果两个皇后在同一行、同一列或同一对角线上，就有冲突
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                return True
    return False

# 定义一个函数，随机在棋盘上放置一个皇后
def place_queen(board):
    n = len(board) # 棋盘的大小
    row = random.randint(0, n-1) # 随机选择一个行号
    board[row] = random.randint(0, n-1) # 随机选择一个列号
    return board

# 定义一个函数，用随机算法解决N皇后问题
def solve_n_queens(n):
    board = [-1] * n # 初始化一个空棋盘，-1表示没有放置皇后
    while is_conflict(board): # 如果有冲突，就继续尝试
        board = place_queen(board) # 随机放置一个皇后
    return board

if __name__ == '__main__':
    print(solve_n_queens(8))
    # https://lichess.org/editor/3Q4/1Q6/7Q/5Q2/Q7/2Q5/4Q3/6Q1_w_-_-_0_1?color=white
