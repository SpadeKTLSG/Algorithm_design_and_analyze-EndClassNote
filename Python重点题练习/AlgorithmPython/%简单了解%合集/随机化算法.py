# -*- coding: utf-8 -*-
import random
#Monte Carlo算法的应用: 计算pi
def pi():
    inside = 0
    for i in range(100): #从100次到1000000次，结果越来越接近pi
        x = random.random()
        y = random.random()
        if x*x + y*y < 1:
            inside += 1
    return 4 * inside / 100

print(pi())