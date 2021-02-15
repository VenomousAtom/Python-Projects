import tkinter

root = tkinter.Tk()
root.title("Click Counter")

x = 1

def click_count():
    global x
    label_display = tkinter.Label(root,text="You've Clicked: "+str(x)+" times")
    x += 1
    label_display.grid(row=1,column=0)

label_button = tkinter.Button(root,text="Click Here",command=click_count)
label_button.grid(row=0,column=0)

root.mainloop()