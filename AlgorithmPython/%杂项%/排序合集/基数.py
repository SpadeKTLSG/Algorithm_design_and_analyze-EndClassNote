# -*- coding: utf-8 -*-
def radix_sort(arr):
    # 获取数组中最大值的位数
    max_digit = len(str(max(arr)))
    buckets = [[] for _ in range(10)]  # 创建10个桶，每个桶是一个空列表

    for i in range(max_digit):    # 从个位开始，对每一位进行排序
        # 将数组中的元素按照该位上的数字分配到对应的桶中
        for num in arr:
            digit = (num // 10**i) % 10
            buckets[digit].append(num)
        # 将桶中的元素按照顺序收集到数组中
        arr.clear()
        for bucket in buckets:
            arr.extend(bucket)
            bucket.clear()
    return arr
