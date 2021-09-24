#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/9/24 10:14

a = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# 所有键
for k in a.keys():
    print(k)

# 所有值
for v in a.values():
    print(v)

# 添加成员
a['k4'] = 'v4'
print(a)

# 买水果
fruits = {
    '苹果': 32.8,
    '香蕉': 22,
    '葡萄': 15.5,
    '草莓': 4.5,
    '橘子': 6.4,
    '樱桃': 15.8
}
info = {
    '小明': {
        'fruits': {
            '苹果': 4,
            '草莓': 13,
            '香蕉': 10,
        }
    },
    '小刚': {
        'fruits': {
            '葡萄': 19,
            '橘子': 12,
            '樱桃': 30,
        }
    },
}
for k, v in info.items():
    money = 0
    for k2, v2 in v.items():
        for k3, v3 in v2.items():
            for k4, v4 in fruits.items():
                if k3 == k4:
                    money += v3 * v4
    print(f"{k}花了{money}元")
    info[k]['money'] = money
print(info)

# 编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
arr = [21, 21, 10, 21, 56, 10, 56, 56, 56, 56, 10, 56, 56, 56, 56]


def counts(arr1):
    result = {}
    b = set(arr1)
    print(b)
    for value in b:
        cou = 0
        for x in arr1:
            if value == x:
                cou += 1
        result[value] = cou
    return result


nn = counts(arr)
print(nn)

# 有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
names = [
    ["刘备", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700, "10"]
]
fields = ['姓名', '年龄', '性别', '编号', '任职公司', '薪资', '部门编号']

employee = {}
for item in names:
    # 遍历员工信息，把每个员工的名字做键，值为字典
    employee[item[0]] = {}
    for ite in item:
        # 遍历单个员工信息，遇到名字跳过
        if item.index(ite) == 0:
            continue
        for field in fields:
            # 遍历字段信息，遇到姓名跳过
            if fields.index(field) == 0:
                continue
                # 如果字段和员工信息对应，则加入字典
            elif item.index(ite) == fields.index(field):
                employee[item[0]][field] = ite
print(employee)
