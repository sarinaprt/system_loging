from tkinter import *

window=Tk()
window.title("calculator")
window.geometry("300x400")
window.resizable(width=False,height=False)

def show_num(NewValue):
    current=number.get()
    number.delete(0,END)
    number.insert(END,current+NewValue)

def clear():
    number.delete(0,END)

def calculater():
    current=number.get()
    result=eval(current)
    number.delete(2,END)
    number.insert(result)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), (' . ', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('( ', 5, 1), (' )', 5, 2), ('^', 5, 3)
]

number=Entry(window,font=("ARIAL",20),relief="groove",justify="right")
number.grid(row=0,columnspan=4)

for (text,row,coulmn) in buttons:
    if text=='c':
        button=Button(window,text=text,width=9,height=4,command=lambda:clear())
    elif text=='=':
        button=Button(window,text=text,width=9,height=4, command=lambda:calculater())
    else:
        button=Button(window,text=text,width=9,height=4,command=lambda text=text: show_num(text))
    button.grid(row=row,column=coulmn)


window.mainloop()
