#!/usr/bin/python3
# encoding='utf-8'
# @time:2021/9/18 14:00

home = {
    "地球": {
        "亚洲": {
            "中国": {
                "北京市": {
                    "昌平区": {
                        "沙河镇": {
                            "沙阳路": {
                                "18号": "汉科软"
                            }
                        }
                    }
                },
                "河南省": {
                    "南阳市": {
                        "方城县": {
                            "广阳镇": {
                                "无敌村": {
                                    "13号": "家"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

address = input("请输入地址：")


# 遍历字典


def fun(dic):
    for key in dic:
        if key == address:
            print("ok")
            break
        elif isinstance(dic[key], dict):
            fun(dic[key])
        else:
            if dic[key] == address:
                print("ok")
                break


fun(home)
