# 基础列表学习
courses = ["阿巴", "啊这", "keep on", "python"]

print(courses)

scores = [99.5, 100, 97.5]

print(scores)

ns = ["python", 10000, 77.5, "加油"]

print(ns)

# 空列表
blist = []

# 定义列表时使用变量
sun = "11111"
liu = 22222
yang = "33333"
xm = [sun, liu, yang]
print(xm)

# 访问列表元素
bicycles = ["trek", "cannondale", "redline", "捷安特", "凤凰", "永久"]
print(bicycles[0])  # 下标0
print(bicycles[3])

# 倒数的索引
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])

# 列表元素的用法与变量完全一样
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# 修改列表元素
motorcycles = ["honda", "yamaha", "suzuki", "宗申", "钱江"]
print(motorcycles)
motorcycles[0] = "嘉陵"
print(motorcycles)

# 尾部添加元素
motorcycles.append("哈雷")
print(motorcycles)

# 插入元素 函数insert(在哪加入, 加入啥)
arg = ["honda", "yamaha", "suzuki"]
arg.insert(0, "哈雷")
arg.insert(1, "嘉陵")
print(arg)

# 第二课
# 删除列表元素   del 列表名[i]  i == "整数"
del motorcycles[0]
print(motorcycles)
del motorcycles[2]
print(motorcycles)

# pop()删除尾部元素
motorcycles = ["honda", "yamaha", "suzuki", "宗申", "钱江"]
hl = motorcycles.pop()
print(motorcycles)
print(hl)  # 知道删了什么
honda = motorcycles.pop(0)
zs = motorcycles.pop(2)
print(motorcycles)

# remove(value) 删除值为value的元素
motorcycles = ["honda", "yamaha", "suzuki", "宗申", "钱江"]
motorcycles.remove("honda")
print(motorcycles)

# 如果有三个honda，使用remove()会怎样
motorcycles = ["honda", "yamaha", "suzuki", "honda", "宗申", "钱江", "honda"]
motorcycles.remove("honda")  # 只会删除第一个元素 只匹配到第一个元素就停止了
print(motorcycles)

# 对列表进行排序 sort()函数 从a开始排序 中文从a开始排序
motorcycles = ["honda", "yamaha", "suzuki", "honda", "宗申", "啊江"]
motorcycles.sort()  # 调通形式:列表名.sort()
print(motorcycles)
# reverse = True 逆行排序 sort(reverse = True)
# True and false == 布尔类型
motorcycles = ["honda", "yamaha", "suzuki", "honda", "宗申", "钱江"]
motorcycles.sort(reverse=True)
print(motorcycles)

# sorted()不改变列表元素进行排序
motorcycles = ["honda", "yamaha", "suzuki", "honda", "宗申", "钱江"]
print(type(motorcycles))
result = sorted(motorcycles)
print("列表内容:" + str(motorcycles))
print("sorted()不改变列表排序后结果:" + str(result))
