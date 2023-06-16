# -*- coding: utf-8 -*-
# 介绍见递归

# 流程
# 定义一个节点类Node，表示解空间树中的每个节点。每个节点包含以下属性：父节点、左右子节点、当前重量、当前剩余重量、当前层次。
# 定义一个优先队列priority_queue，按照节点的当前重量从大到小排序。优先队列可以保证每次取出最大重量的节点作为扩展节点。
# 定义一个分支限界函数branch_and_bound(i)，表示处理第i个集装箱的选择问题，其中i从0开始计数。
# 在函数中，首先判断是否达到基准情形，即i等于n，表示所有集装箱都已处理完毕。如果是，则比较current_value和best_value，如果前者大于后者，则更新best_value和best_solution，并输出结果；否则返回。
# 如果不是基准情形，则对第i个集装箱进行两种选择：装入第一艘轮船或者不装入任何轮船。对于每种选择，首先判断是否满足约束条件，即current_value加上第i个集装箱的重量是否小于等于c1。如果是，则创建一个新节点，并设置其属性为：父节点为当前节点、左右子节点为空、当前重量为current_value加上第i个集装箱的重量、当前剩余重量为remain_value减去第i个集装箱的重量、当前层次为i+1。然后将新节点加入到优先队列中。
# 在每次创建新节点前后，还需要判断是否满足限界条件，即current_value加上remain_value是否大于best_value。如果不是，则表示当前子树中不可能存在更优解，可以剪枝返回。
# 在优先队列不为空的情况下，重复以上步骤，直到找到一个可行解或者最优解

# 两条船, 也就是分支限界判断的情况多了些

# 定义物品数量、重量和轮船容量
# ? 是不是有点对箭画靶 ? 后面需要优化输出方法.
n = 3 # 物品数量
w = [20, 15, 10] # 物品重量
c1 = 20 # 轮船1容量
c2 = 15 # 轮船2容量

# 定义全局变量
best_value = 0 # 当前最优解的价值
best_solution = [0] * n # 当前最优解对应的选择方案
current_value = 0 # 当前子问题的价值
current_solution = [0] * n # 当前子问题对应的选择方案
c2_value = 0 # 当前子问题中装入第二艘轮船的集装箱的总重量
remain_value = sum(w) # 剩余未处理集装箱的总重量

# 定义节点类
class Node:
    def __init__(self, parent, left, right, weight, remain, level):
        self.parent = parent # 父节点
        self.left = left # 左子节点
        self.right = right # 右子节点
        self.weight = weight # 当前重量
        self.remain = remain # 当前剩余重量
        self.level = level # 当前层次

    def __lt__(self, other): # 定义比较规则，按照当前重量从大到小排序
        return self.weight > other.weight

# 定义优先队列
import heapq
priority_queue = []

# 定义分支限界函数
def branch_and_bound(i):
    global best_value, best_solution, current_value, current_solution, c2_value, remain_value
    if i == n: # 基准情形，所有集装箱都已处理完毕
        if current_value > best_value: # 如果当前价值大于最优价值
            best_value = current_value # 更新最优价值
            best_solution = current_solution.copy() # 更新最优方案
            print("\n最优价值是", best_value) # 输出最优价值
            print("The first ship has:", current_value, "weight of items") # 输出第一艘轮船的集装箱重量
            print("The second ship has:", c2_value, "weight of items") # 输出第二艘轮船的集装箱重量
            print("The best solution is:", best_solution) # 输出最优方案
            for j in range(n): # 输出每个集装箱对应的选择
                if best_solution[j] == 1:
                    print("物品", j+1, "装第一条里了")
                elif best_solution[j] == 2:
                    print("物品", j+1, "装第二条里了")
                else:
                    print("物品", j+1, "倒海里了")
            print('\n')
        return True # 返回True表示找到了一个可行解或者最优解
    else: # 非基准情形，处理第i个集装箱的选择问题
        result = False # 初始化结果为False

        if c2_value + w[i] <= c2: # 如果选择装入第二艘轮船，满足约束条件

            if current_value + remain_value > best_value: # 如果满足限界条件

                new_node = Node(None, None, None, current_value, remain_value - w[i], i+1) # 创建一个新节点

                heapq.heappush(priority_queue, new_node) # 将新节点加入到优先队列中

                c2_value += w[i] # 更新第二艘轮船的集装箱重量

                current_solution[i] = 2 # 更新当前方案

                remain_value -= w[i] # 更新剩余集装箱重量

                result = branch_and_bound(i+1) or result # 递归调用并更新结果

                c2_value -= w[i] # 恢复第二艘轮船的集装箱重量

                current_solution[i] = 0 # 恢复当前方案

                remain_value += w[i] # 恢复剩余集装箱重量

        if current_value + w[i] <= c1: # 如果选择装入第一艘轮船，满足约束条件

            if current_value + remain_value > best_value: # 如果满足限界条件

                new_node = Node(None, None, None, current_value + w[i], remain_value - w[i], i+1) # 创建一个新节点

                heapq.heappush(priority_queue, new_node) # 将新节点加入到优先队列中

                current_value += w[i] # 更新当前价值

                current_solution[i] = 1 # 更新当前方案

                remain_value -= w[i] # 更新剩余集装箱重量

                result = branch_and_bound(i+1) or result # 递归调用并更新结果

                current_value -= w[i] # 恢复当前价值

                current_solution[i] = 0 # 恢复当前方案

                remain_value += w[i] # 恢复剩余集装箱重量

        if current_value + remain_value > best_value: # 如果选择不装入任何轮船，满足限界条件

            new_node = Node(None, None, None, current_value, remain_value - w[i], i+1) # 创建一个新节点

            heapq.heappush(priority_queue, new_node) # 将新节点加入到优先队列中

            remain_value -= w[i] # 更新剩余集装箱重量

            result = branch_and_bound(i+1) or result # 递归调用并更新结果

            remain_value += w[i] # 恢复剩余集装箱重量

        while priority_queue: # 在优先队列不为空的情况下

            current_node = heapq.heappop(priority_queue) # 取出当前重量最大的节点

            current_value = current_node.weight # 更新当前价值

            remain_value = current_node.remain # 更新剩余集装箱重量

            i = current_node.level # 更新当前层次

            result = branch_and_bound(i) or result # 递归调用并更新结果

        return result # 返回结果

# 调用分支限界函数
branch_and_bound(0)

