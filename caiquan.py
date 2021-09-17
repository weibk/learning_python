#!/usr/bin/python3
# encoding='utf-8'
# @time:2021/9/18 9:19
import random

items = ['石头', '剪刀', '布']
for item in items:
    print(items.index(item) + 1, '---', item)

while True:
    your = int(input("请选择你的手势："))
    if your > 3:
        print("请输入1-3:！！")
        continue
    suiji = random.randint(0, 2)
    flag = suiji - (your - 1)
    xitong = items[suiji]
    if flag == 0:
        print(f"游戏平局!你和机器人都选择了{xitong}")
    elif flag == 1 or flag == 2:
        print(f"你输了！你选择了{items[your - 1]}，机器人选择了{xitong}")
    else:
        print(f"你赢了！你选择了{items[your - 1]}，机器人选择了{xitong}")
