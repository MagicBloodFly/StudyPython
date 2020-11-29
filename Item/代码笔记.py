# join()函数 把数组里面的数据结合并表达出来
# join()只针对字符串
# sort()函数也是针对字符串
# 例子
t, s = "one", "two"

arg = [t, s]

z1 = " ".join(arg)  # 用空格分开

print(z1)

z2 = ":".join(arg)  # 用冒号分开

print(z2)

# 保留小数方法
s = 3.14

s = ("%.6f" % s)  # 6位小数

print(s)

# sum()用法
n = sum([1, 2, 3])  # 等于6
print(n)

# split(",") 用法
n = map(float, input("").split(","))  # 使用逗号隔开输入
# 例如输入  1,2

# isdigit()检测字符串是否是数字 返回True或者False
tx = "sd4731"
print(tx.isdigit())
tx2 = "45"
print(tx2.isdigit())

# line是一个字符串变量
line = "Python is simple.I practice programming everyday."
n_i = line.count("i")  # count()统计在字符串里面i出现多少次
i_t = line.index("t")  # index()统计在字符串里面t首次出现的下标
