import tkinter

root = tkinter.Tk()
root.title("Calculator")

e = tkinter.Entry(root,width=35,border=7,bg='Black',fg='Lime')
first_num = tkinter.Entry(root)
operation = tkinter.Entry(root)
back_num = tkinter.Entry(root)
back_num.insert(0,"")

def on_click(num):
    e.delete(0,tkinter.END)
    x = str(back_num.get())+str(num)
    e.insert(0,x)
    back_num.delete(0,tkinter.END)
    back_num.insert(0,x)

def on_add():
    first_num.insert(0,e.get())
    operation.insert(0,"+")
    e.delete(0,tkinter.END)
    back_num.delete(0, tkinter.END)

def on_sub():
    first_num.insert(0,e.get())
    operation.insert(0, "-")
    e.delete(0,tkinter.END)
    back_num.delete(0, tkinter.END)

def on_mul():
    first_num.insert(0,e.get())
    operation.insert(0, "*")
    e.delete(0,tkinter.END)
    back_num.delete(0, tkinter.END)

def on_div():
    first_num.insert(0,e.get())
    operation.insert(0, "/")
    e.delete(0,tkinter.END)
    back_num.delete(0, tkinter.END)

def on_clr():
    e.delete(0,tkinter.END)
    operation.delete(0, tkinter.END)
    first_num.delete(0, tkinter.END)
    back_num.delete(0,tkinter.END)

def on_eq():
    y = e.get()
    e.delete(0,tkinter.END)

    if operation.get() == "+":
        e.insert(0,float(first_num.get())+float(y))

    elif operation.get() == "-":
        e.insert(0,float(first_num.get())-float(y))

    elif operation.get() == "*":
        e.insert(0,float(first_num.get())*float(y))

    elif operation.get() == "/":
        e.insert(0,float(first_num.get())/float(y))

    operation.delete(0, tkinter.END)
    first_num.delete(0, tkinter.END)
    back_num.delete(0, tkinter.END)

button_1 = tkinter.Button(root,text='1',padx=20,pady=20,activebackground='Black',activeforeground='Cyan',command=lambda: on_click(1))
button_2 = tkinter.Button(root,text='2',padx=20,pady=20,activebackground='Black',activeforeground='Cyan',command=lambda: on_click(2))
button_3 = tkinter.Button(root,text='3',padx=20,pady=20,activebackground='Black',activeforeground='Cyan',command=lambda: on_click(3))
button_4 = tkinter.Button(root,text='4',padx=20,pady=20,activebackground='Black',activeforeground='Cyan',command=lambda: on_click(4))
button_5 = tkinter.Button(root,text='5',padx=20,pady=20,activebackground='Black',activeforeground='Cyan',command=lambda: on_click(5))
button_6 = tkinter.Button(root,text='6',padx=20,pady=20,activebackground='Black',activeforeground='Cyan',command=lambda: on_click(6))
button_7 = tkinter.Button(root,text='7',padx=20,pady=20,activebackground='Black',activeforeground='Cyan',command=lambda: on_click(7))
button_8 = tkinter.Button(root,text='8',padx=20,pady=20,activebackground='Black',activeforeground='Cyan',command=lambda: on_click(8))
button_9 = tkinter.Button(root,text='9',padx=20,pady=20,activebackground='Black',activeforeground='Cyan',command=lambda: on_click(9))
button_0 = tkinter.Button(root,text='0',padx=48,pady=20,activebackground='Black',activeforeground='Cyan',command=lambda: on_click(0))
button_dot = tkinter.Button(root,text='.',padx=21,pady=20,activebackground='Black',activeforeground='Cyan',command=lambda: on_click('.'))
button_add = tkinter.Button(root,text='+',padx=20,pady=52,command=on_add)
button_sub = tkinter.Button(root,text='-',padx=20,pady=20,command=on_sub)
button_div = tkinter.Button(root,text='/',padx=20,pady=20,command=on_div)
button_mul = tkinter.Button(root,text='*',padx=20,pady=20,command=on_mul)
button_clr = tkinter.Button(root,text='Clr',padx=15,pady=20,command=on_clr)
button_eq = tkinter.Button(root,text='=',padx=20,pady=52,command=on_eq)

e.grid(row=0,column=0,columnspan=4)
#first_num.grid(row=6,column=0,columnspan=4)
#operation.grid(row=7,column=0,columnspan=4)
#back_num.grid(row=8,column=0,columnspan=4)
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_0.grid(row=5,column=0,columnspan=2)
button_dot.grid(row=5,column=2)
button_add.grid(row=2,column=3,rowspan=2)
button_sub.grid(row=1,column=3)
button_mul.grid(row=1,column=2)
button_div.grid(row=1,column=1)
button_clr.grid(row=1,column=0)
button_eq.grid(row=4,column=3,rowspan=2)

root.mainloop()