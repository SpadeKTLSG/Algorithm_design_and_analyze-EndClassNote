# -*- coding: utf-8 -*-
def bucket_sort(arr, bucket_size=10):
    # 如果数组长度小于2则直接返回
    if len(arr) < 2:
        return arr
    # 获取数组中最大值和最小值
    max_num = max(arr)
    min_num = min(arr)
    # 计算桶的数量
    bucket_count = (max_num - min_num) // bucket_size + 1
    # 创建桶列表，每个桶是一个空列表
    buckets = [[] for _ in range(bucket_count)]
    # 将数组中的元素按照映射规则分配到对应的桶中
    for num in arr:
        bucket_index = (num - min_num) // bucket_size
        buckets[bucket_index].append(num)
    # 对每个桶中的元素进行排序，可以使用其他排序算法
    for i in range(bucket_count):
        buckets[i].sort()
    # 将所有桶中的元素依次放入原数组
    arr.clear()
    for bucket in buckets:
        arr.extend(bucket)
    return arr
