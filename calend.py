from tkinter import *
from tkcalendar  import *
import DDL

def app_calender(user_id):

    def Diary_not(event):
        date=calender.get_date()
        days_page=Toplevel()
        days_page.geometry("400x400")
        days_page.title(f"{date}")
        global entry
        entry=Text(days_page,fg="gray")
        entry.insert(1.0,"you can write your history")
        memory=DDL.get_calendar_note(user_id,date)
        if memory:
            entry.delete(1.0,END)
            entry.insert(1.0,memory)
            entry.config(fg="black")
        entry.bind("<FocusIn>",writing)
        entry.bind("<FocusOut>",not_typing)
        entry.place(width=400,height=300)
        button=Button(days_page,text="save",command=daily_history).place(x=150,y=350,width=100)
        
    def writing(event):
        if entry.get(1.0,END).strip()=="you can write your history":
            entry.delete(1.0,END)
            entry.config(fg="black")
    def not_typing(event):
        if entry.get(1.0,END).strip()=="":
            entry.insert(1.0,"you can write your history")
            entry.config(fg="gray")
        
    def daily_history():
        date=calender.get_date()
        text=entry.get("1.0", END).strip()
        if text !="" and text!="you can write your history":
            DDL.update_or_insert_calendar(user_id,date,text)
            entry.delete(1.0, END)  
            entry.insert(1.0,text)  
            entry.config(fg="black") 


    window=Tk()
    window.geometry("600x600")
    window.title("calendar")
    window.resizable(width=False,height=False)
    calender=Calendar(window,selectmode="day",locale="en_US",date_pattern="yyy-mm-dd",font=(15))
    calender.bind("<<CalendarSelected>>", Diary_not)
    calender.pack(fill="both",expand=True)



    window.mainloop()

