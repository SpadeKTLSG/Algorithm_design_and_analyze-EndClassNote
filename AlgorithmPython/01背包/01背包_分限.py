# -*- coding: utf-8 -*-
# 介绍同回溯法, 这个大概不考

# ! 有问题, 无法运行

# 定义物品数量、重量、价值和背包容量
n = 3  # 物品数量
w = [20, 15, 10]  # 物品重量
v = [20, 30, 25]  # 物品价值
c = 30  # 背包容量

# 定义一个优先队列来存储活结点
import heapq
queue = []

class Node:
    def __init__(self, weight, value, level, parent, isleft):
        self.weight = weight  # 当前重量
        self.value = value  # 当前价值
        self.level = level  # 当前层数
        self.parent = parent  # 父结点
        self.isleft = isleft  # 是否选择
        self.upbound = self.get_upbound()  # 目标函数上界

    def __lt__(self, other):  # 比较运算符重载，按照上界从大到小排序
        return self.upbound > other.upbound

    def get_upbound(self):  # 计算目标函数上界
        bound = self.value  # 当前价值
        surplus = c - self.weight  # 剩余容量
        i = self.level + 1  # 下一个物品的索引
        while i < n and w[i] <= surplus:  # 如果下一个物品可以放入背包
            bound += v[i]  # 加上该物品的价值
            surplus -= w[i]  # 减去该物品的重量
            i += 1  # 继续考虑下一个物品
        if i < n:  # 如果下一个物品不能完全放入背包
            bound += v[i] * surplus / w[i]  # 按照单位价值放入部分物品
        return bound  # 返回上界


# 定义一个函数来添加活结点到优先队列中
def add_live_node(weight, value, level, parent, isleft):
    node = Node(weight, value, level, parent, isleft)  # 创建结点对象
    heapq.heappush(queue, node)  # 将结点加入优先队列


def branch_and_bound(w, v, c):
    add_live_node(0, 0, -1, None, False)  # 从根结点开始，将其加入优先队列中
    best_value = 0  # 定义一个变量来记录最优解的价值
    while queue:  # 循环直到优先队列为空或者找到最优解
        
        node = heapq.heappop(queue)  # 取出最大上界的活结点
        
        if node.level == n - 1: # 判断是否为叶子结点
            if node.value > best_value: # 如果当前叶子结点的价值大于当前最优值
                best_value = node.value # 更新最优值
                
        elif node.upbound <= best_value: # 判断是否达到最优解
            print("The best value is:", best_value) # 输出最优解的价值
            break # 结束循环
            
        else:  # 如果不是，则生成左右两个孩子结点
            i = node.level + 1  # 下一个物品的索引
            left_weight = node.weight + w[i]  # 左孩子的重量，表示选择该物品
            left_value = node.value + v[i]  # 左孩子的价值，表示选择该物品
            right_weight = node.weight  # 右孩子的重量，表示不选择该物品
            right_value = node.value  # 右孩子的价值，表示不选择该物品
            
            if left_weight <= c and left_value > best_value:  # 如果左孩子满足约束条件且上界大于当前最优值，则将其加入优先队列中
                add_live_node(left_weight, left_value, i, node, True)
                best_value = max(best_value, left_value)  # 更新当前最优值
                
            if right_value > best_value:  # 如果右孩子满足约束条件且上界大于当前最优值，则将其加入优先队列中
                add_live_node(right_weight, right_value, i, node, False)


if __name__ == '__main__':

    branch_and_bound(w, v, c)  # 测试分支限界法的代码

