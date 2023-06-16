# -*- coding: utf-8 -*-
# 问题: 设有n个活动的集合E={1,2,…,n}，其中每个活动都要求使用同一资源，如演讲会场等，而在同一时间内只有一个活动能使用这一资源。每个活动i都有一个要求使用该资源的起始时间si和一个结束时间fi,且si <fi。
# 如果选择了活动i，则它在半开时间区间[si, fi)内占用资源。若区间[si, fi)与区间[sj, fj)不相交,则称活动i与活动j是相容的。也就是说，当si≥fj或sj≥fi时，活动i与活动j相容。活动安排问题就是要在所给的活动集合中选出最大的相容活动子集合。
# 这个算法的思路是，每次选择结束时间最早的活动，然后排除与它冲突的活动，重复这个过程，直到没有活动可选。
# 这样可以保证选择的活动数量最多，也就是最大兼容活动子集。

# 参考文章: https://blog.csdn.net/u013854486/article/details/102845400
# 定义一个活动类，包含开始时间和结束时间
class Activity:
    def __init__(self, start, end):
        self.start = start
        self.end = end

# 定义一个贪心算法函数，输入是一个活动列表，输出是一个最大兼容活动子集
def greedy_activity_selector(activities):

    activities.sort(key=lambda x: x.end)
    result = [activities[0]]
    
    current_end = activities[0].end # 初始化当前活动的结束时间

    for i in range(1, len(activities)):
        # 如果当前活动的开始时间大于等于当前结束时间，说明兼容，贪心就直接给我加入结果列表，并更新当前结束时间
        if activities[i].start >= current_end:
            result.append(activities[i])
            current_end = activities[i].end

    return result

# 测试
activities = [Activity(1, 4), Activity(3, 5), Activity(0, 6), Activity(5, 7), Activity(3, 9), Activity(5, 9), Activity(6, 10), Activity(8, 11), Activity(8, 12), Activity(2, 14), Activity(12, 16)]
result = greedy_activity_selector(activities)
for i in result:
    print(i.start, i.end)