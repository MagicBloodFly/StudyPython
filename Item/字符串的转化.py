
# 整数转化为字符串
# 浮点数是属于有理数中某特定子集的数的数字表示,在计算机中用以近似表示任意某个实数。
age = 23

message = "Happy "+str(age)+"rd Birthday!"

print(message)

print(type(age))

# 字串符转化为整数
# input返回是字符串

x = int(input("输入x:"))

y = int(input("输入y:"))

sum = x+y

print("和:"+str(sum))

# 字符串转化为浮点数

fx = float(input("输入矩形的宽度:"))

fy = float(input("输入矩形的长度:"))

print("矩形面积:"+str(fx * fy))

# 一行显示多个字符串方法
n1, n2 = map(float, input("").split(" "))
# split(" ")表示空格隔开

z = n1 * n2

z = ("%.6f" % z)

print("y="+z)

