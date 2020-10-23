

class Dog():

    def __init__(self,name,age):
        #注册类
        self.name = name
        self.age = age

    def sit(self):

        print(self.name.title()+"坐下了")

    def write(self,number):

        print(number)

mydog = Dog("on",7)

youdog = Dog("in",6)

print("你的狗是"+youdog.name+" 我的狗是"+mydog.name)

class TNT():

    def __init__(self,name,r):

        self.name = name

        self.r = r
