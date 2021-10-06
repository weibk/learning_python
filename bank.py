#!/usr/bin/python3
# encoding='utf-8'
# author:weibk
# @time:2021/9/23 19:10

import pymysql
import random

con = pymysql.connect(host="localhost",
                      user="root",
                      password="123456",
                      database="db",
                      charset="utf8")
cursor = con.cursor(cursor=pymysql.cursors.DictCursor)
print("*****************************")
print("*        中国工商银行         *")
print("*        账户管理系统         *")
print("*           V1.0            *")
print("*****************************")
print("*                           *")
print("* 1.开户                     *")
print("* 2.存款                     *")
print("* 3.取款                     *")
print("* 4.转账                     *")
print("* 5.查询                     *")
print("* 6.退出                     *")
print("*****************************")
BANK_NAME = "中国工商银行"
MONEY_INIT = 0


# 根据账号查询信息
def getinfo(account):
    cursor.execute('select * from bank_user where account=%s', (account,))
    result = cursor.fetchone()
    return result


# 添加用户
def useradd():
    # 判断用户库是否已满
    s = cursor.execute("select * from bank_user")
    if s == 100:
        return 3
    # 判断用户是否存在
    while True:
        username = input("请输入您的姓名：")
        cursor.execute("select username from bank_user")
        uname = cursor.fetchall()
        for item in uname:
            if username == item['username']:
                return 2
        break
    password = input("请设置一个密码：")
    print("请您填写地址：")
    country = input("\t请输入您所在的国家：")
    province = input("\t请输入您所在的城市：")
    street = input("\t请输入您所在的街道：")
    house_number = input("\t请输入您的门牌号：")
    # 判断账号是否已经存在,如果已经存在则重新生成
    while True:
        account = str(random.randint(10, 99)) + str(
            random.randint(10, 99)) + str(
            random.randint(10, 99)) + str(random.randint(10, 99))
        cursor.execute("select account from bank_user")
        uname = cursor.fetchall()
        for item in uname:
            if account == item['account']:
                continue
        else:
            break
    cursor.execute("insert into bank_user values "
                   "(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (repr(account), repr(username), repr(password),
                    repr(country), repr(province),
                    repr(street), repr(house_number),
                    repr(BANK_NAME), repr(MONEY_INIT)))
    con.commit()
    cursor.execute("select * from bank_user where account=%s", (account,))
    info1 = cursor.fetchone()
    return info1


# 登录方法
def login():
    while True:
        acc = int(input("请输入您的账号"))
        cursor.execute("select account from bank_user")
        uname = cursor.fetchall()
        for item in uname:
            if acc == item['account']:
                while True:
                    pwd = input("请输入密码：")
                    cursor.execute("select * from bank_user where "
                                   "account=%s", (acc,))
                    info1 = cursor.fetchone()
                    if pwd == info1['password']:
                        return {"flag": 1, 'info': info1}
                    else:
                        return 2
            else:
                continue
        return 3


while True:
    step = input("请选择业务：")
    if step == "1":
        info = useradd()
        print(type(info))
        # 如果开户成功，打印用户信息
        if isinstance(info, dict):
            profile = '''
                用户信息
            ---------------
            账号：%s
            姓名：%s
            密码：%s
            地址：%s-%s-%s-%s
            余额：%s
            开户行：%s
            ---------------
            '''
            print("恭喜你开户成功！！，您的信息如下：")
            print(profile % (info['account'], info['username'],
                             info['password'], info['country'],
                             info['province'], info['street'],
                             info['house_number'], info['bank'],
                             info['balance']))
        elif info == 2:
            print("该用户已存在")
            continue
        elif info == 3:
            print("用户库已满暂不支持开户业务")
            continue
    elif step == "2":
        flag = login()
        if isinstance(flag, dict):
            bank = flag['info']
            yue = bank['balance']
            print(f"你好，{bank['username']}登录成功!账户当前余额为{yue}")
            # 登录成功存款
            while True:
                cunkuan = input("请输入您要存的金额：")
                if cunkuan == 'Q' or cunkuan == 'q':
                    break
                elif cunkuan.isdigit():
                    cunkuan = int(cunkuan)
                else:
                    print('存款请输入正数，输入Q/q可退出业务')
                    continue
                yue += cunkuan
                print(f"存款成功！余额为{yue}")
                cursor.execute("update bank_user set balance=%s where "
                               "account=%s", (yue, bank['account']))
                con.commit()
                break
        elif flag == 2:
            print("密码错误！")
            continue
        elif flag == 3:
            print("账号不存在！")
            continue
    elif step == "3":
        flag = login()
        if isinstance(flag, dict):
            bank = flag['info']
            yue = bank['balance']
            # 判断余额是否为0
            if yue == 0:
                print(f"你好，{bank['username']},您的余额为0，不能使用取款业务")
                continue
            else:
                print(f"你好，{bank['username']},登录成功!账户当前余额为{yue}")
            while True:
                qukuan = input("请输入您要取的金额：")
                if qukuan == 'Q' or qukuan == 'q':
                    break
                elif qukuan.isdigit():
                    qukuan = int(qukuan)
                else:
                    print('取款请输入正数，输入Q/q可退出业务')
                # 判断余额是否足够
                if yue < qukuan:
                    print('您的余额不足')
                    break
                else:
                    yue -= qukuan
                print(f"取款成功！余额为{yue}")
                cursor.execute("update bank_user set balance=%s where "
                               "account=%s", (yue, bank['account']))
                con.commit()
                break
        elif flag == 2:
            print("密码错误！")
            continue
        elif flag == 3:
            print("账号不存在！")
            continue
    elif step == "4":
        flag = login()
        if isinstance(flag, dict):
            bank = flag['info']
            yue = bank['balance']
            acc1 = bank['account']
            # 余额为0不能转账
            if yue == 0:
                print(f"你好，{bank['username']},您的余额为0，不能使用转账业务")
                continue
            else:
                print(f"你好，{bank['username']},登录成功!账户当前余额为{yue}")
            while True:
                acc2 = input("请输入您要转账的账户：")
                # 判断转入账户是否存在
                y = cursor.execute(
                    "select * from bank_user where account=%s", (acc2,))
                x = cursor.fetchone()
                if y == 1:
                    # 判断转出和转入账户是否相同
                    if acc2 != acc1:
                        zhuan = input("请输入您要转的金额：")
                        if zhuan == 'Q' or zhuan == 'q':
                            break
                        elif zhuan.isdigit():
                            zhuan = int(zhuan)
                        else:
                            print('转账请输入正数，输入Q/q可退出业务')
                        # 判断余额
                        if yue < zhuan:
                            print("您的余额不足，输入Q/q可退出业务")
                            break
                        else:
                            # 转出账户余额减少
                            yue -= zhuan
                            print(f"转账成功！您的余额为{yue}")
                            cursor.execute(
                                "update bank_user set balance=%s where "
                                "account=%s", (yue, acc1))
                            con.commit()
                            # 转入账户余额增加

                            x['balance'] += zhuan
                            cursor.execute(
                                "update bank_user set balance=%s where "
                                "account=%s", (x['balance'], acc2))
                            con.commit()
                            break
                    else:
                        print('不能给自己转账，输入Q/q可退出业务')
                        continue
                else:
                    print("您输入的账号不存在，输入Q/q可退出业务")
                    continue
        elif flag == 2:
            print("密码错误！")
            continue
        elif flag == 3:
            print("账号不存在！")
            continue
    elif step == "5":
        flag = login()
        if isinstance(flag, dict):
            bank = flag['info']
            print(f"登录成功!账户当前信息如下：")
            profile = '''
                                用户信息
                            ---------------
                            账号：%s
                            姓名：%s
                            密码：%s
                            地址：%s-%s-%s-%s
                            开户行：%s
                            余额：%s
                            ---------------
                            '''
            print(profile % (bank['account'], bank['username'],
                             bank['password'], bank['country'],
                             bank['province'], bank['street'],
                             bank['house_number'], bank['bank'],
                             bank['balance']))
        elif flag == 2:
            print("密码错误！")
            continue
        elif flag == 3:
            print("账号不存在！")
            continue
    elif step == "6":
        break

con.commit()
cursor.close()
con.close()
