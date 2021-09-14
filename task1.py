#!/usr/bin/python3
# encoding='utf-8'
# @time:2021/9/14 10:37

items = [
    {
        "date": "1号",
        "name": "羽绒服",
        "price": 253.6,
        "stock": 500,
        "sales": 10,
    },
    {
        "date": "2号",
        "name": "牛仔裤",
        "price": 83.6,
        "stock": 600,
        "sales": 60,
    },
    {
        "date": "3号",
        "name": "风衣",
        "price": 98.6,
        "stock": 335,
        "sales": 43,
    },
    {
        "date": "4号",
        "name": "皮草",
        "price": 135.9,
        "stock": 855,
        "sales": 63,
    },
    {
        "date": "5号",
        "name": "T恤",
        "price": 65.8,
        "stock": 632,
        "sales": 63,
    },
    {
        "date": "6号",
        "name": "衬衫",
        "price": 49.3,
        "stock": 562,
        "sales": 120,
    },
    {
        "date": "7号",
        "name": "牛仔裤",
        "price": 86.3,
        "stock": 600,
        "sales": 72,
    },
    {
        "date": "8号",
        "name": "羽绒服",
        "price": 253.6,
        "stock": 500,
        "sales": 69,
    },
    {
        "date": "9号",
        "name": "牛仔裤",
        "price": 86.3,
        "stock": 600,
        "sales": 35,
    },
    {
        "date": "10号",
        "name": "羽绒服",
        "price": 253.6,
        "stock": 500,
        "sales": 140,
    },
    {
        "date": "11号",
        "name": "牛仔裤",
        "price": 86.3,
        "stock": 600,
        "sales": 90,
    },
    {
        "date": "12号",
        "name": "皮草",
        "price": 135.9,
        "stock": 855,
        "sales": 24,
    },
    {
        "date": "13号",
        "name": "T恤",
        "price": 65.8,
        "stock": 632,
        "sales": 45,
    },
    {
        "date": "14号",
        "name": "风衣",
        "price": 96.8,
        "stock": 335,
        "sales": 25,
    },
    {
        "date": "15号",
        "name": "牛仔裤",
        "price": 86.3,
        "stock": 600,
        "sales": 90,
    },
    {
        "date": "16号",
        "name": "T恤",
        "price": 65.8,
        "stock": 632,
        "sales": 129,
    },
    {
        "date": "17号",
        "name": "羽绒服",
        "price": 253.6,
        "stock": 500,
        "sales": 10,
    },
    {
        "date": "18号",
        "name": "风衣",
        "price": 96.8,
        "stock": 335,
        "sales": 43,
    },
    {
        "date": "19号",
        "name": "T恤",
        "price": 65.8,
        "stock": 632,
        "sales": 63,
    },
    {
        "date": "20号",
        "name": "牛仔裤",
        "price": 86.3,
        "stock": 600,
        "sales": 60,
    },
    {
        "date": "21号",
        "name": "皮草",
        "price": 135.9,
        "stock": 855,
        "sales": 63,
    },
    {
        "date": "22号",
        "name": "风衣",
        "price": 96.8,
        "stock": 335,
        "sales": 60,
    },
    {
        "date": "23号",
        "name": "T恤",
        "price": 65.8,
        "stock": 632,
        "sales": 58,
    },
    {
        "date": "24号",
        "name": "牛仔裤",
        "price": 86.3,
        "stock": 600,
        "sales": 140,
    },
    {
        "date": "25号",
        "name": "T恤",
        "price": 65.8,
        "stock": 632,
        "sales": 48,
    },
    {
        "date": "26号",
        "name": "风衣",
        "price": 96.8,
        "stock": 335,
        "sales": 43,
    },
    {
        "date": "27号",
        "name": "皮草",
        "price": 135.9,
        "stock": 855,
        "sales": 57,
    },
    {
        "date": "28号",
        "name": "羽绒服",
        "price": 253.6,
        "stock": 500,
        "sales": 10,
    },
    {
        "date": "29号",
        "name": "T恤",
        "price": 65.8,
        "stock": 632,
        "sales": 63,
    },
    {
        "date": "30号",
        "name": "风衣",
        "price": 96.8,
        "stock": 335,
        "sales": 78,
    },
]
print("日期---服装名称---价格/件---库存数量---销售量/每日")
# 总销售金额
sums = 0
# 总销售量
sales = 0

for item in items:
    sums += item['price'] * item['sales']
    sales += item['sales']
    print(item['date'] + '----' + item['name'] + '----' + str(item['price']) +
          '---' +
          str(item['stock']) + '---' + str(item['sales']))

print(f"总销售额为：{round(sums, 2)}元")
print(f"平均每日销售数量为：{round(sales / 30, 1)}")

# 计算各个种类的总销售量
a, b, c, d, e, f = 0, 0, 0, 0, 0, 0
for i in items:
    if i['name'] == '羽绒服':
        a += i['sales']
    elif i['name'] == '牛仔裤':
        b += i['sales']
    elif i['name'] == '风衣':
        c += i['sales']
    elif i['name'] == '皮草':
        d += i['sales']
    elif i['name'] == 'T恤':
        e += i['sales']
    elif i['name'] == '衬衫':
        f += i['sales']

print(f"羽绒服的月销售量占比：{round((a / sales)*100)}%")
print(f"牛仔裤的月销售量占比：{round((b / sales)*100)}%")
print(f"风衣的月销售量占比：{round((c / sales)*100)}%")
print(f"皮草的月销售量占比：{round((d / sales)*100)}%")
print(f"T恤的月销售量占比：{round((e / sales)*100)}%")
print(f"衬衫的月销售量占比：{round((f / sales)*100)}%")
