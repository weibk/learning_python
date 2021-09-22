#!/usr/bin/python3
# encoding='utf-8'
# @time:2021/9/22 11:13
import random

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
bank_user = {
    '99999999': {
        "username": 'wjj',
        "password": '123456',
        "country": 'zg',
        "province": 'bj',
        "street": 'sh',
        "house_number": '18',
        "bank": "中国工商银行",
        "balance": 200,
    },
    '88888888': {
        "username": 'sy',
        "password": '123456',
        "country": 'zg',
        "province": 'bj',
        "street": 'sh',
        "house_number": '18',
        "bank": "中国工商银行",
        "balance": 20000,
    }
}


def useradd():
    arr = []
    for i in bank_user.keys():
        arr.append(i)
    if len(arr) == 100:
        return 3
    '''
    判断用户是否存在
    '''
    while True:
        username = input("请输入您的姓名：")
        for item in bank_user.keys():
            if username == bank_user[item]['username']:
                return 2
        break
    password = input("请设置一个密码：")
    print("请您填写地址：")
    country = input("\t请输入您所在的国家：")
    province = input("\t请输入您所在的城市：")
    street = input("\t请输入您所在的街道：")
    house_number = input("\t请输入您的门牌号：")
    '''
    判断账号是否已经存在
    如果已经存在则重新生成
    '''
    while True:
        account = str(random.randint(10, 99)) + str(
            random.randint(10, 99)) + str(
            random.randint(10, 99)) + str(random.randint(10, 99))
        if account in bank_user:
            continue
        else:
            break
    bank_user[account] = {
        "username": username,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "house_number": house_number,
        "bank": BANK_NAME,
        "balance": MONEY_INIT,
    }
    info1 = {
        "flag": 1,
        "account": account,
        "username": username,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "house_number": house_number,
        "bank": BANK_NAME,
        "balance": MONEY_INIT,
    }
    return info1


def login():
    while True:
        acc = input("请输入您的账号")
        if acc in bank_user:
            while True:
                pwd = input("请输入密码：")
                if pwd == bank_user[acc]['password']:
                    return {"flag": 1, 'acc': acc}
                else:
                    return 2
        else:
            return 3

while True:
    step = input("请选择业务：")
    if step == "1":
        info = useradd()
        if isinstance(info, dict):
            if info['flag'] == 1:
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
                                 info['house_number'], info['balance'],
                                 info['bank']))
        elif info == 2:
            print("该用户已存在")
            continue
        elif info == 3:
            print("用户库已满暂不支持开户业务")
            continue
    elif step == "2":
        flag = login()
        if isinstance(flag, dict):
            acc1 = flag['acc']
            print(f"登录成功!账户当前余额为{bank_user[acc1]['balance']}")
            while True:
                qukuan = int(input("请输入您要存的金额："))
                bank_user[acc1]['balance'] += qukuan
                print(f"存款成功！余额为{bank_user[acc1]['balance']}")
                break
        elif flag == 2:
            print("密码错误！")
            break
        elif flag == 3:
            print("账号不存在！")
            break
    elif step == "3":
        flag = login()
        if isinstance(flag, dict):
            acc1 = flag['acc']
            print(f"登录成功!账户当前余额为{bank_user[acc1]['balance']}")
            if bank_user[acc1]['balance'] == 0:
                print("您的余额为0，不能使用取款业务")
                continue
            while True:
                qukuan = int(input("请输入您要取的金额："))
                if bank_user[acc1]['balance'] < qukuan:
                    print('您的余额不足')
                    break
                else:
                    bank_user[acc1]['balance'] -= qukuan
                print(f"取款成功！余额为{bank_user[acc1]['balance']}")
                continue
        elif flag == 2:
            print("密码错误！")
            continue
        elif flag == 3:
            print("账号不存在！")
            continue
    elif step == "4":
        flag = login()
        if isinstance(flag, dict):
            acc1 = flag['acc']
            print(f"登录成功!账户当前余额为{bank_user[acc1]['balance']}")
            if bank_user[acc1]['balance'] == 0:
                print("您的余额为0，不能使用转账业务")
                continue
            while True:
                acc2 = input("请输入您要转账的账户：")
                if acc2 in bank_user:
                    zhuan = int(input("请输入您要转的金额："))
                    if bank_user[acc1]['balance'] < zhuan:
                        print("您的余额不足")
                        break
                    else:
                        bank_user[acc1]['balance'] -= zhuan
                        bank_user[acc2]['balance'] += zhuan
                        print(f"转账成功！您的余额为{bank_user[acc1]['balance']}")
                        break
                else:
                    print("您输入的账号不存在")
                    break
        elif flag == 2:
            print("密码错误！")
            continue
        elif flag == 3:
            print("账号不存在！")
            continue
    elif step == "5":
        flag = login()
        if isinstance(flag, dict):
            acc1 = flag['acc']
            pro = bank_user[acc1]
            print(f"登录成功!账户当前信息如下：")
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
            print(profile % (acc1, pro['username'],
                             pro['password'], pro['country'],
                             pro['province'], pro['street'],
                             pro['house_number'], pro['balance'],
                             pro['bank']))
        elif flag == 2:
            print("密码错误！")
            continue
        elif flag == 3:
            print("账号不存在！")
            continue
    elif step == "6":
        break
