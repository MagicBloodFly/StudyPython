"""
重要作业1
对于在一行内输入多个数字，split()函数为分割符号
"""

n1, n2= map(float, input("").split(" "))

z = n1 * n2

z = ("%.6f" % z)

print("y="+z)

"""
重要作业2
对于列表的使用和函数的运用
join()函数 输出列表并使用空格隔开
append()函数 在列表最后保存一个数据
"""
n = int(input(""))

arg = []

number = 4

var = 0

while number > 0:

    number -= 1

    s = n**var

    var += 1

    arg.append(str(s))


print(" ".join(arg))


"""
重要作业3
输入格式:
行1：输入字符串
行2：输入子串起始位置
行3：输入子串结束位置
输出格式:
输出截取子串，如果起始或结束位置不合法，输出没子串！

"""
py = input("")

n1 = int(input(""))

n2 = int(input(""))

if n1 < 0 or n2 > len(py):

    print("没子串！")

else:
    n1 -= 1

    print(py[n1:n2])




