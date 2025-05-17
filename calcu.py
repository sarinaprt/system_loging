from tkinter import *

def calculator():
    def show_num(NewValue):
        current=number.get()
        number.delete(0,END)
        number.insert(END,current+NewValue)


    def calculater():
        current=number.get()
        result=eval(current)
        number.delete(0,END)
        number.insert(END,result)
    def clear():
        number.delete(0,END)

    window=Tk()
    window.title("calculator")
    window.geometry("300x400")
    window.resizable(width=False,height=False)

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
        if text=='=':
            button=Button(window,text=text,width=9,height=4, command=calculater)
        elif text=='C':
            button=Button(window,text=text,width=9,height=4,command=clear)
        else:
            button=Button(window,text=text,width=9,height=4,command=lambda NewValue=text: show_num(NewValue))
        button.grid(row=row,column=coulmn)


    window.mainloop()
