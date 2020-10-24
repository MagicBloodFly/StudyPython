# join()函数 把数组里面的数据结合并表达出来
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
