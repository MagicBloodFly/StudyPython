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
print(bicycles[0])# 下标0
print(bicycles[3])

# 倒数的索引
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])

# 列表元素的用法与变量完全一样
message = "My first bicycle was a "+bicycles[0].title()+"."
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