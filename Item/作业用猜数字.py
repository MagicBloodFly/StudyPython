import random

# 导入random
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