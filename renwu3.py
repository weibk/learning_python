#!/usr/bin/python3
# encoding='utf-8'
# @time:2021/9/22 16:38

# 有下列人员数据库，请按要求实现
import math

names = [
    ["曹操", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700, "10"]
]

# 每个人的平均工资
arr = []
for i in names:
    arr.append(i[0])
arr1 = set(arr)

for i in arr1:
    k = 0
    sum1 = 0
    for j in names:
        if j[0] == i:
            k += 1
            sum1 += j[5]
    print(f'{i}的平均工资为{sum1 / k}')

# 每个人的平均年龄
arr = []
for i in names:
    arr.append(i[0])
arr1 = set(arr)

for i in arr1:
    k = 0
    sum1 = 0
    for j in names:
        if j[0] == i:
            k += 1
            sum1 += int(j[1])
    print(f'{i}的平均年龄为{sum1 / k}')

# 添加员工
names.append(['刘备', '45', '男', '220', 'alibaba', 500, '30'])
print(names)

# 统计公司男女数
arr = []
for i in names:
    arr.append(i[4])
arr1 = set(arr)

for i in arr1:
    male = 0
    female = 0
    for j in names:
        if j[4] == i:
            if j[2] == '男':
                male += 1
            elif j[2] == '女':
                female += 1
    print(f'{i}公司的男性有{male}人，女性有{female}人')

# 每个部门的人数
arr = []
for i in names:
    arr.append(i[6])
arr1 = set(arr)

for i in arr1:
    k = 0
    for j in names:
        if j[6] == i:
            k += 1
    print(f'{i}部门有{k}人')

# 现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
# [罗恩, 23 ,35 ,44]
# [哈利 ,60, 77 ,68 ,88, 90]
# [赫敏, 97 ,99 ,89 ,91, 95, 90]
# [马尔福 ,100, 85 ,90]
# 求每个人的总成绩？
grade = [
    ['罗恩', 23, 35, 44],
    ['哈利', 60, 77, 68, 88, 90],
    ['赫敏', 97, 99, 89, 91, 95, 90],
    ['马尔福', 100, 85, 90]
]
for i in grade:
    sum1 = 0
    for j in i:
        if isinstance(j, int):
            sum1 += j
    print(f'{i[0]}的总成绩为{sum1}')

# 冒泡排序
a = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]


def maopao(b):
    m = 0
    while m < len(b) - 1:
        j = 0
        while j < len(b) - 1 - m:
            if b[j] > b[j + 1]:
                b[j], b[j + 1] = b[j + 1], b[j]
            j += 1
        m += 1

maopao(a)
print(a)
