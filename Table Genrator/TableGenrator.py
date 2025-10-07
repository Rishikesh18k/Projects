from customtkinter import *
from tkinter.messagebox import showinfo
#>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<
def calculation():
    try:
        value = eval(number.get())
        i = 1
        list = []
        while i <= 10:
            container = value*i
            list.append(container)
            i=i+1
        one.configure(text=list[0])
        two.configure(text=list[1])
        three.configure(text=list[2])
        four.configure(text=list[3])
        five.configure(text=list[4])
        six.configure(text=list[5])
        seven.configure(text=list[6])
        eight.configure(text=list[7])
        nine.configure(text=list[8])
        ten.configure(text=list[9])
    except Exception:
        showinfo(title="Empty Number",message="Please enter the Number!")
# >>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<
def Clear_btn():
    one.configure(text="")
    two.configure(text="")
    three.configure(text="")
    four.configure(text="")
    five.configure(text="")
    six.configure(text="")
    seven.configure(text="")
    eight.configure(text="")
    nine.configure(text="")
    ten.configure(text="")
    entry_label.delete(0,END)
# >>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<
win = CTk()
win.title("Table Genrator")
win.geometry("380x650+500+20")
win.resizable(False, False)
win.config(bg="#262626")
# >>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<
message_label = CTkLabel(win,text="Enter the number    --",font=("Franklin Gothic Demi Cond",20),
                        text_color="#EEEEEE",fg_color="#262626")
message_label.place(x=75,y=35)
number = StringVar()
entry_label = CTkEntry(win,text_color="#EEEEEE",font=("Franklin Gothic Demi Cond",18),
                       height=35,width=60,border_width=1.50,border_color="#737373",
                       corner_radius=4,fg_color="#444444",textvariable=number)
entry_label.place(x=256,y=32)
generate_btn = CTkButton(win,text="Generate",font=("Franklin Gothic Demi Cond",20),height=40,
                       width=120,text_color="#FFFFFF",fg_color="#009900",corner_radius=4,
                       border_color="#EEEEEE",border_width=1,hover_color="#00cc00",
                       cursor="hand2", command=calculation)
generate_btn.place(x=72,y=92)
clear_btn = CTkButton(win,text="Clear",font=("Franklin Gothic Demi Cond",18),height=40,
                       width=120,text_color="#000000",fg_color="#EEEEEE",corner_radius=4,
                       border_color="#EEEEEE",border_width=1,hover_color="#ffffff",
                       cursor="hand2",command=Clear_btn)
clear_btn.place(x=198,y=92)
one = CTkLabel(win,text="",font=("Franklin Gothic Demi Cond",22),fg_color="#444444",
               height=40,width=50,corner_radius=4,text_color="#FFFFFF")
one.place(x=168,y=150)
two = CTkLabel(win,text="",font=("Franklin Gothic Demi Cond",22),fg_color="#444444",
               height=40,width=50,corner_radius=5,text_color="#FFFFFF")
two.place(x=168,y=200)
three = CTkLabel(win,text="",font=("Franklin Gothic Demi Cond",22),fg_color="#444444",
               height=40,width=50,corner_radius=5,text_color="#FFFFFF")
three.place(x=168,y=250)
four = CTkLabel(win,text="",font=("Franklin Gothic Demi Cond",22),fg_color="#444444",
               height=40,width=50,corner_radius=5,text_color="#FFFFFF")
four.place(x=168,y=300)
five = CTkLabel(win,text="",font=("Franklin Gothic Demi Cond",22),fg_color="#444444",
               height=40,width=50,corner_radius=5,text_color="#FFFFFF")
five.place(x=168,y=350)
six = CTkLabel(win,text="",font=("Franklin Gothic Demi Cond",22),fg_color="#444444",
               height=40,width=50,corner_radius=5,text_color="#FFFFFF")
six.place(x=168,y=400)
seven = CTkLabel(win,text="",font=("Franklin Gothic Demi Cond",22),fg_color="#444444",
               height=40,width=50,corner_radius=5,text_color="#FFFFFF")
seven.place(x=168,y=450)
eight = CTkLabel(win,text="",font=("Franklin Gothic Demi Cond",22),fg_color="#444444",
               height=40,width=50,corner_radius=5,text_color="#FFFFFF")
eight.place(x=168,y=500)
nine = CTkLabel(win,text="",font=("Franklin Gothic Demi Cond",22),fg_color="#444444",
               height=40,width=50,corner_radius=5,text_color="#FFFFFF")
nine.place(x=168,y=550)
ten = CTkLabel(win,text="",font=("Franklin Gothic Demi Cond",22),fg_color="#444444",
               height=40,width=50,corner_radius=5,text_color="#FFFFFF")
ten.place(x=168,y=600)
win.mainloop()