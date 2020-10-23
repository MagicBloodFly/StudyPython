
import random

cs = 5


while cs > 0:


    number = int(input("请猜一个数字:"))

    mt = random.randint(1, 4)

    cs -= 1

    if number == mt:

        print("恭喜您猜对啦!!!")

        break

    else:
        print("猜错啦")

        print(mt)
else:
    print("你没有机会再进行下去了")


