#!/usr/bin/python3
# encoding='utf-8'
# @time:2021/9/15 14:22

# 实现输入10个数字，并打印10个数的求和结果
# i = 1
# result = 0
# while i <= 10:
#     num = int(input(f"请输入第{i}个数字："))
#     result += num
#     i += 1
# print(f"求和结果为：{result}")

# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# i = 1
# result = 0
# list1 = []
# while i <= 10:
#     num = int(input(f"请输入第{i}个数字："))
#     result += num
#     list1.append(num)
#     i += 1
# list1.sort()
# print("最大数为：", list1[-1])
# print(f"求和结果为：{result}")
# print(f"平均数为：{result / 10}")

# 使用random模块，如何产生 50~150之间的数？
# import random
# # 随机整数
# suiji = random.randint(50, 150)
# print(suiji)
# # 随机浮点数
# suiji = random.uniform(50, 150)
# print(suiji)

# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
# a = int(input("请输入边a的长度："))
# b = int(input("请输入边b的长度："))
# c = int(input("请输入边c的长度："))
# bian = [a, b, c]
# bian.sort()
# [a, b, c] = bian
# print(a, b, c)
# if a + b > c and c - b < a:
#     if a == b:
#         print("等腰三角形")
#     elif a**2 + b**2 == c**2:
#         print("直角三角形")
#     elif a == b == c:
#         print("等边三角形")
#     else:
#         print("普通三角形")
# else:
#     print("不能构成三角形")
#
# print(math.sqrt(2))

# 有以下两个数，使用+，-号实现两个数的调换。
# a = 56
# b = 78
# c = b - a
# a = a + c
# b = b - c
# print(a, b)

# 实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# i = 1
# while i <= 3:
#     username = input("请输入用户名：")
#     password = input("请输入密码：")
#     if username == 'root' and password == 'admin':
#         print("登录成功！！")
#         break
#     else:
#         if i == 3:
#             print("登录次数已达上限")
#             break
#         print("用户名或密码错误，请重新登录！")
#         i += 1
#         continue

# 打印一个等边三角形
# i = 1
# while i <= 7:
#     print('  ' * (7 - i) + '*   ' * i)
#     i += 1

# 九九乘法表
i, j = 1, 1
result = ' '
while j <= 9:
    while i <= j:
        result += f"{i} * {j} = {i * j}\t"
        i += 1
        if i > j:
            i = 1
            print(result)
            result = ' '
            break
    j += 1

# 倒序乘法表
# i, j = 1, 9
# result = ' '
# while j >= 1:
#     while i <= j:
#         result += f"{i} * {j} = {i * j}\t"
#         i += 1
#         if i > j:
#             i = 1
#             print(result)
#             result = ' '
#             break
#     j -= 1

# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
# h = 20
# i = 0
# while h > 0:
#     h = h - 3
#     i += 1
#     if h <= 0:
#         break
#     h = h + 2
# print(i)

# 20以内的阶乘和
# import math
#
# i = 1
# result = 0
# while i <= 20:
#     result += math.factorial(i)
#     i += 1
# print(result)
# 不使用math函数
# i = 1
# j = 1
# result = 0
# res = 1
# while i <= 20:
#     while j <= i:
#         res *= j
#         j += 1
#     result += res
#     i += 1
# print(result)

# 求是5的倍数的数的和

# a = [1, 5, 21, 30, 15, 9, 30, 24]
# result = 0
# for i in range(len(a)):
#     if a[i] % 5 == 0:
#         result += a[i]
#     else:
#         continue
#
# print(result)

# dict1 = {
#     'first': 1,
#     'second': 2,
#     'third': 3,
# }
# for k, v in dict1.items():
#     print(k, v)


a = [[1, 2], [1, 2], [2, 3]]
b = set(a)
print(b)
for x in b:
    print(x)
