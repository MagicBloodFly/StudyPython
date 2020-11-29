# line是一个字符串变量
line = "Python is simple.I practice programming everyday."
zdzf = max(line)
zxzf = min(line)
line_len = len(line)
print(zdzf)
print(zxzf)
print(line_len)

n_i = line.count("i")  # count()统计在字符串里面i出现多少次
i_t = line.index("t")  # index()统计在字符串里面t首次出现的下标
print(n_i)
print(i_t)

# sum()函数进行统计
socores = [8, 9, 7.5, 7, 10, 9.5, 8, 7, 6, 8.5]
total = sum(socores)
avg = total/len(socores)
print(avg)
print(max(socores))
print(min(socores))
print(socores.count(8))
print(socores.index(7))

# 列表推导式
# 写法 变量 = [表达式 for v in 列表]
squares = [v**2 for v in range(11)]
print(squares)

# asciis码比较大小
asciis = [ord(s) for s in "abcd efgy"]
print(asciis)

# 用列表推导式读入一行中的数
ns = [int(s) for s in input("输入:").split()]
print(ns)

# 推导后持续输入
n = int(input("输入整数:"))
fs = [float(input("输入浮点数:")) for i in range(n)]
print(fs)

# 输出矩阵
smtx = [input("矩阵测试:").split() for r in range(3)]
print(smtx)

# 强制转整数
imtx = [[int(s) for s in input("输入整数:").split()] for i in range(2)]
print(imtx)



