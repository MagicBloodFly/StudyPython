num_line = input("输入一组整数,用空格隔开:")
num_str = num_line.split()
num_list = []
for s in num_str:
    num_list.append(int(s))

print(num_list)
