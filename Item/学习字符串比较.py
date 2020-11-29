# 字符串编号比较(ASCII)
# 一直都是比较第一个字符
# 大写字符总是比小写字母小
end_str = input("输入一个字符串:")
if end_str == "end":
    print("你输入的是end")
else:
    print("你输入的不是end")

if end_str < "end":
    print("你输入的字符串小于end")
if end_str > "end":
    print("你输入的字符串大于end")

# 不考虑大小写比较字符串
# 要全部大写
if "Zhong".upper() > "ba".upper():
    print("Zhong > ba")
else:
    print("Zhong < ba")

