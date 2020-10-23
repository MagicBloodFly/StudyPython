import tkinter

top = tkinter.Tk()

def gg():

    print("666")


def button():
    top.destroy()
    
    root = tkinter.Tk()

    b3 = tkinter.Label(root, text='测试文本')

    b3.pack()






B = tkinter.Button(top, text ="点我",bg = 'yellow',command=button)#command后面不可以加括号

b2 = tkinter.Label(top, text='测试文本')
# 进入消息循环


B.pack()

b2.pack()

top.mainloop()



