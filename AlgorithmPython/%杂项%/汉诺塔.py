# -*- coding: utf-8 -*-
def fun(n,a,b,c):  #左边是边界条件，abc为三个柱子
    global num
    if n==1:
        print("{}-->{}".format(a,c))
        num+=1
    else:
        fun(n-1,a,c,b)
        print("{}-->{}".format(a,c))
        num+=1
        fun(n-1,b,a,c)

num=0
m=int(input("请输入最左边上的盘子个数"))
print("盘子的移动顺序为： ")
fun(m,'a','b','c')
print("用时= {}".format(num))

# 如果只有一个盘子，就直接从a柱子移动到c柱子.
# 如果有多个盘子，就先把上面n-1个盘子从a柱子借助c柱子移动到b柱子，
# 然后把最下面的盘子从a柱子移动到c柱子，最后再把b柱子上的n-1个盘子借助a柱子移动到c柱子.