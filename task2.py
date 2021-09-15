#!/usr/bin/python3
# encoding='utf-8'
# @time:2021/9/15 10:51
# 猜数字

import random

# 初始资金
capital = 500
count = 0
input_num = input("请输入一个0-20的整数：")


# 产生随机数
def suiji():
    guess1 = random.randint(0, 20)
    # 显示随机数
    # print(guess1)
    return guess1


# 判断输入是否为数字
def isnum(num):
    while True:
        flag = num.isdigit()
        if flag:
            num = int(num)
            return num
        else:
            print("注意：请输入0-20的整数！！！")


# 判断大小
def compare(num, cap, coun):
    guess = suiji()
    while True:
        if num < guess:
            cap -= 100
            coun += 1
            if coun == 3:
                print(f"您已经猜错{coun}次了，游戏结束！")
                break
            if cap <= 0:
                print("您的资金已经为0,游戏结束")
                break
            print(f"您输入的数字偏小了,当前资金剩余{cap},您已经猜错{coun}次了,还有{3 - coun}次机会,请重新输入：")
            num = isnum(input("请输入一个0-20的整数："))
            continue
        elif num > guess:
            cap -= 100
            coun += 1
            if coun == 3:
                print(f"您已经猜错{coun}次了，游戏结束！")
                break
            if cap <= 0:
                print("您的资金已经为0,游戏结束")
                break
            print(f"您输入的数字偏大了,当前资金剩余{cap},您已经猜错{coun}次了,还有{3 - coun}次机会,请重新输入：")
            num = isnum(input("请输入一个0-20的整数："))
            continue
        else:
            coun = 0
            cap += 10
            print(f"恭喜你猜对了！！,当前资金为{cap}")
            guess = suiji()
            num = isnum(input("请输入一个0-20的整数："))
            continue

input_num = isnum(input_num)
compare(input_num, capital, count)
