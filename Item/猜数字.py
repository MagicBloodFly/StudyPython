
import random


number = int(input("请猜一个数字:"))

mt = random.randint(1,4)

if number == mt:

    print("恭喜您猜对啦!!!")

else:
    print("猜错啦")

    print(mt)




computer=random.randint(1,100)
while True:
    number=int(input("请输入100以内的整数："))
    if(number>computer):
        print("大了")
    elif(number<computer):
        print("小了")
    else:
        print("恭喜你赢了")
        break
