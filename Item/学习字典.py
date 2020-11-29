# 建:值
word_dict = {
    "name": "名字",
    "python": "蟒蛇",
    "dictionary": "字典",
    "list": "列表",
    "variable": "变量",
    "class": "类",
    "object": "对象"
}
# 字典实现生词本
word = input("输入单词:")
if word in word_dict:
    print(word+"->翻译为:"+word_dict[word])
else:
    print("没有这个单词")

