from tkinter import *
import datetime

def Time():
    time = datetime.datetime.now()
    hour = time.strftime('%I')
    minuts = time.strftime('%M')
    second = time.strftime('%S')
    am_pm = time.strftime('%p')
    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')
    hr_label.config(text=hour)
    min_label.config(text=minuts)
    am_label.config(text=am_pm)
    sec_label.config(text=second)
    date_label.config(text=date)
    month_label.config(text=month)
    year_label.config(text=year)
    day_label.config(text=day)
    hr_label.after(200,Time)
#>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<
win = Tk()
win.title("Digital Watch")
win.geometry("345x250+500+180")
win.config(bg="#000000")
win.config
win.resizable(False,False)
icon = PhotoImage(file="C:\\Users\\Rishikesh\\OneDrive\\Desktop\\Digital Watch\\pngtree-hand-painted-black-alarm-clock-illustration-png-image_4094512.png")
win.iconphoto(False, icon)
#>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
hr_label = Label(win,text="00",font=("Arial",50,"bold"),relief=FLAT,bg="#000000",fg="Red")
hr_label.place(x=40,y=25)
cola_label = Label(win,text=":",font=("Arial",45,"bold"),relief=FLAT,bg="#000000",fg="Red")
cola_label.place(x=122,y=25)
min_label = Label(win,text="00",font=("Arial",50,"bold"),relief=FLAT,bg="#000000",fg="Red")
min_label.place(x=147,y=25)
colb_label = Label(win,text=":",font=("Arial",45,"bold"),relief=FLAT,bg="#000000",fg="Red")
colb_label.place(x=230,y=25)
am_label = Label(win,text="",font=("Arial",16,"bold"),relief=FLAT,bg="#000000",fg="Red")
am_label.place(x=261,y=45,height=20)
sec_label = Label(win,text="00",font=("Arial",19,"bold"),relief=FLAT,bg="#000000",fg="Red")
sec_label.place(x=262,y=69,height=20)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
date_frame = Frame(win,relief=GROOVE,bg="#000000",bd=0.50)
date_frame.place(x=-1,y=123,width=347,height=140)

date_label = Label(date_frame,text="00",font=("Arial",50,"bold"),relief=FLAT,bg="#000000",fg="Red")
date_label.place(x=40,y=20)

slacea_label = Label(date_frame,text="/",font=("Arial",46,"bold"),relief=FLAT,bg="#000000",fg="Red")
slacea_label.place(x=122,y=24)

month_label = Label(date_frame,text="00",font=("Arial",50,"bold"),relief=FLAT,bg="#000000",fg="Red")
month_label.place(x=147,y=20)

slaceb_label = Label(date_frame,text=".",font=("Arial",45),relief=FLAT,bg="#000000",fg="Red")
slaceb_label.place(x=230,y=25)

year_label = Label(date_frame,text="00",font=("Arial",21,"bold"),relief=FLAT,bg="#000000",fg="Red")
year_label.place(x=261,y=42,height=21)

day_label = Label(date_frame,text="Mon",font=("Arial",16,"bold"),relief=FLAT,bg="#000000",fg="Red")
day_label.place(x=262,y=66,height=20)
Time()
win.mainloop()