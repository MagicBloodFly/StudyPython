n1, n2= map(float, input("").split(" "))

z = n1 * n2

z = ("%.6f" % z)

print("y="+z)

# 作业
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



