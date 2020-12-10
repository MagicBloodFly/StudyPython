# 简单的实现用户注册
# 并且登录来打猜数字小游戏
import random

zm = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v",
      "b", "n", "m"]

n = 6

User = {
    "admin": "admin"
}  # 创建用户文件

mtt = []  # 储存概率

g = 0  # 猜数字开关

while True:
    # 创建防重复密码表
    if len(mtt) != 0:
        mtt = []
        continue
    else:
        n = input("请输入你的用户名(输入login来登录到登录系统):")
        if n == "login":
            break
        if n not in User:
            password = input("请输入你的密码:")

            if len(password) == 0:
                print("由于你没有输入密码,所以系统自动为你生成六位密码")
                for i in range(0, 6):
                    mt = random.randint(0, 25)
                    mtt.append(int(mt))
                p = zm[mtt[0]] + "" + zm[mtt[1]] + "" + zm[mtt[2]] + "" + zm[mtt[3]] + "" + zm[mtt[4]] + "" + zm[
                    mtt[5]]
                print("你的密码为:" + str(p))
                print("正在为你保存数据,数据正在导入User...")
                User[n] = p
            else:
                print("你的密码为:" + str(password))
                print("正在为你保存数据,数据正在导入User...")
                User[n] = password
        else:
            print("您已经注册,请使用密码登录!")
            break

# 登录部分
while True:

    n = input("请输入你的名称:")
    arg = []

    if n not in User:
        print("啊哦,你输入的名称不在账户列表里")
        continue

    p = input("请输入你的密码:")
    if n == "admin" and p == "admin":
        print("管理员登录成功")
        print("-----当前密码表-----")
        print(User)
        print("------------------")
    if p != User[n]:
        print("密码错误,请重试! 找回密码请联系开发者")
        continue
    else:
        print("密码正确!登录成功")
        g += 1
        break
        # 结束

if g == 1:
    arg = int(input("请输入你要从哪个数字开始猜:"))
    arg2 = int(input("请输入你要从哪个数字结束猜:"))
    number = int(input("请输入你想要几次机会:"))

    sz = [arg, arg2]

    if number < 0:
        number = - number

    mt = random.randint(sz[0], sz[1])

    while number > 0:
        number -= 1
        n = int(input("输入数字(" + str(sz[0]) + "到" + str(sz[1]) + "中间):"))
        if n > sz[1] or n < sz[0]:
            print("请输入" + str(sz[0]) + "到" + str(sz[1]) + "里面一个词")
            break
        if number == 0:
            # 给予提示
            text = "但是你没有机会了!"
        else:
            text = "还有(" + str(number) + ")次机会!"

        if n > mt:
            print("你输入的数字比随机数大,再试试吧," + text)
        elif n < mt:
            print("你输入的数字比随机数小,再试试吧," + text)
        else:
            print("恭喜你猜对啦!")
            break  # 终止
            # 谢谢使用...
