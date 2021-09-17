#!/usr/bin/python3
# encoding='utf-8'
# @time:2021/9/17 19:04
import random

shop = [
    ['牛仔裤', 99],
    ["风衣", 130],
    ["皮草", 150],
    ["衬衫", 100],
    ["羽绒服", 100],
    ["T恤", 80],
    ["辣条", 10],
    ["汽水", 10]
]

money = int(input("请输入你的金额："))
# 优惠券
ticket = random.randint(1, 10)
print(f"恭喜您抽中了{ticket}元的优惠券")
mycart = []
print(f"序号---名称---价格")
for index, value in enumerate(shop):
    print(f"{index + 1}----{value[0]}----{value[1]}")


while True:
    result = 0
    choose = input("请输入你要买的商品的序号：")
    if not mycart:
        pass
    else:
        for item in mycart:
            result += item[1]
    if choose.isdigit():
        choose = int(choose)
        if 0 < choose <= len(shop):
            if money-result >= shop[choose - 1][1]:
                mycart.append(shop[choose - 1])
                print("加入购物车成功!!")
            else:
                print("您的资金不足，购物车已满，输入Q/q结账")
        else:
            print("商品不存在！！")
    elif choose == 'Q' or choose == 'q':
        print("购物结束，欢迎下次光临！")
        if not mycart:
            print("您本次没有购买商品")
        else:
            if mycart.count(["辣条", 10]) >= 10:
                result -= 0.3
            elif mycart.count(["汽水", 10]) >= 20:
                result -= 0.9
            print("您的购物清单如下：")
            newcart = []
            for item in mycart:
                if [item[0], mycart.count(item)] not in newcart:
                    newcart.append([item[0], mycart.count(item)])
            for x in newcart:
                print(x[0], "X", x[1])
            print("您的余额为：", money - result + ticket, "元")
            break
    else:
        print("输入非法！！")