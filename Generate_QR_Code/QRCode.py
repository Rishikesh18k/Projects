from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import showerror, askyesno
from tkinter.colorchooser import askcolor
from PIL import Image
import warnings
import time
warnings.filterwarnings("ignore")
#>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<
win=CTk()
win.title("QR Hub")
win.geometry("420x590+440+40")
win.resizable(False, False)
win.config(bg="#4D90FE")
wallpaper_label=CTkFrame(win,width=430,height=600,fg_color="#4D90FE")
wallpaper_label.place(x=0,y=0)
#>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<
def CustomizePage():
    url_container=link.get()
    if (len(url_container)>=12) and (len(url_container)<=2040):
        fill_color=StringVar()
        def get_qr_color():
            qr_color=askcolor(title="Choose colour")
            if qr_color[1] is not None:
                fill_color.set(qr_color[1])
                Choose_QR_color.configure(text=qr_color[1],fg_color=f"{qr_color[1]}")
            else:
                pass
        back_color = StringVar()
        def get_bg_color():
            bg_color=askcolor(title="Choose colour")
            if bg_color[1] is not None:
                back_color.set(bg_color[1])
                Choose_Background_color.configure(text=bg_color[1],fg_color=f"{bg_color[1]}")
            else:
                pass
        def generate_QR():
            size_value=size.get()
            border_value=border.get()
            color_x=fill_color.get()
            color_y=back_color.get()
            if color_x:
                if color_y:
                    if size_value.isdigit():
                        if (eval(size_value)>=2) and (eval(size_value)<=20):
                            if border_value.isdigit():
                                if (eval(border_value)>=2) and (eval(border_value)<=50):
                                    import qrcode
                                    from tkinter import filedialog
                                    qr = qrcode.QRCode(version=1,error_correction=qrcode.ERROR_CORRECT_H,box_size=size_value,border=border_value)
                                    qr.add_data(f"{url_container}")
                                    qr.make(fit=True)
                                    img=qr.make_image(fill_color=f"{color_x}",back_color=f"{color_y}")
                                    time.sleep(1)
                                    generate_btn.configure(text="QR Code Generated")
                                    qr_file = filedialog.asksaveasfile(
                                        title="Save QR ",initialdir="/",
                                        defaultextension="*.png",
                                        filetypes=(("PNG files","*.png"),("All files","*.*")))
                                    if qr_file:
                                        img.save(qr_file.name)
                                        qr_file.close()
                                        home_frame_x.destroy()
                                        next_btn.configure(command=CustomizePage)
                                        entry_label.delete(0,END)
                                    else:
                                        home_frame_x.destroy()
                                        entry_label.delete(0,END)
                                else:
                                    showerror(message="Please enter Border size between 2 and 50.")
                            else:
                                showerror(message="Please enter border size.\nAllow only digit value.")
                        else:
                            showerror(message="Please enter QR size between 2 and 20.")
                    else:
                        showerror(message="Please enter QR size.\nAllow only digit value.")
                else:
                    showerror(message="Background Colour not found!")
            else:
                showerror(message="QR Colour not found!")
        def Go_To_home():
            home_frame_x.destroy()
        home_frame_x = CTkFrame(wallpaper_label, width=360, height=520,bg_color="#4d90fe",fg_color="#F5F5FA",
                                corner_radius=30)
        back_btn = CTkButton(home_frame_x,text="⬅",font=("Arial",16),text_color="#333333",fg_color="#F5F5FA",
                            cursor='hand2',height=30,width=30,corner_radius=6,hover_color="#e6e6e6",bg_color="#F5F5FA",
                            command=Go_To_home)
        back_btn.place(x=20,y=20)
        title = CTkLabel(home_frame_x,text="𝐐𝐑 𝐇𝐮𝐛",font=("Aptos",42,"bold"), text_color="#333333",
                                fg_color="#F5F5FA")
        title.place(x=120,y=30)
        title_x = CTkLabel(home_frame_x,text="Please adjust your QR code",font=("Aptos",13,"bold"), text_color="#262626",
                            fg_color="#F5F5FA")
        title_x.place(x=98,y=85)
        screen_width_x = 200
        screen_height_x = 200
        image = Image.open("C:\\Users\\Rishikesh\\OneDrive\\Desktop\\Generate_QR_Code\\cubeQR.png")
        image_x = image.resize((screen_width_x, screen_height_x))
        bg_image_x = ImageTk.PhotoImage(image_x)
        wallpaper_label_x = CTkLabel(home_frame_x,image=bg_image_x,text="",width=170,height=170,fg_color="#F5F5FA",
                                            bg_color="#F5F5FA",corner_radius=30)
        wallpaper_label_x.place(x=50, y=122)
        Choose_QR_color = CTkButton(home_frame_x,text="Choose QR Color",font=("Franklin Gothic Demi Cond",15),
                                    width=145,height=32,text_color="#595959",fg_color="#e6e6ff",corner_radius=5,
                                    border_color="#67a1fe",border_width=2,hover_color="#67a1fe",bg_color="#F5F5FA",
                                    cursor="hand2",command=get_qr_color)
        Choose_QR_color.place(x=30,y=335)
        Choose_Background_color = CTkButton(home_frame_x,text="Background Color",font=("Franklin Gothic Demi Cond",15),
                                width=145,height=32,text_color="#595959",fg_color="#e6e6ff",corner_radius=5,
                                border_color="#67a1fe",border_width=2,hover_color="#67a1fe",bg_color="#F5F5FA",
                                cursor="hand2",command=get_bg_color)
        Choose_Background_color.place(x=185,y=335)
        size_list = ['2','4','6','8','10','12','14','16','18','20']
        size = CTkComboBox(home_frame_x,values=size_list,text_color="#595959",font=("Franklin Gothic Demi Cond",15),width=145,height=32,
                            fg_color="#e6e6ff",bg_color="#F5F5FA",border_width=2,border_color="#67a1fe",corner_radius=5,
                            button_color="#67a1fe", dropdown_text_color="#595959",dropdown_font=("Franklin Gothic Demi Cond",15),
                            dropdown_fg_color="#F5F5FA",dropdown_hover_color="#67a1fe",button_hover_color="#80b1fe")
        size.set(value="QR code size")
        size.place(x=30,y=380)
        border_list = ['2','5','10','15','20','25','30','35','40','45','50']
        border = CTkComboBox(home_frame_x,values=border_list,text_color="#595959",font=("Franklin Gothic Demi Cond",15),width=145,height=32,
                            fg_color="#e6e6ff", bg_color="#F5F5FA",border_width=2,border_color="#67a1fe",corner_radius=5,
                            button_color="#67a1fe", dropdown_text_color="#595959",dropdown_font=("Franklin Gothic Demi Cond",15),
                            dropdown_fg_color="#F5F5FA",dropdown_hover_color="#67a1fe",button_hover_color="#80b1fe")
        border.set(value="Border size")
        border.place(x=185,y=380)
        generate_btn = CTkButton(home_frame_x,text="Generate QR Code",font=("Franklin Gothic Demi Cond",19),height=45,
                                width=300,text_color="#FFFFFF",fg_color="#4d90fe",corner_radius=10,
                                border_color="#4d90fe",border_width=2,hover_color="#67a1fe",bg_color="#F5F5FA",
                                cursor="hand2",command=generate_QR)
        generate_btn.place(x=30,y=426)
        page_numberA = CTkLabel(home_frame_x,text="●",font=("Aptos",22),fg_color="#F5F5FA",text_color="#9ac0fe")
        page_numberA.place(x=160,y=479)
        page_numberB = CTkLabel(home_frame_x,text="●",font=("Aptos",22),fg_color="#F5F5FA",text_color="#3481fe")
        page_numberB.place(x=180,y=479)
        home_frame_x.place(x=30,y=35)
    else:
        showerror(message="Link not found!\nTry again please.")
# >>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<< 
home_frame = CTkFrame(wallpaper_label, width=360, height=520,bg_color="#4D90FE",fg_color="#F5F5FA",
               corner_radius=30, border_width=2,border_color="#F5F5FA")
title = CTkLabel(home_frame,text="𝐐𝐑 𝐇𝐮𝐛",font=("Aptos",42,"bold"), text_color="#333333",
                    fg_color="#F5F5FA")
title.place(x=120,y=30)
title_x = CTkLabel(home_frame,text="Generate QR Codes Instantly",font=("Aptos",13), text_color="#262626",
                    fg_color="#F5F5FA")
title_x.place(x=100,y=85)
screen_width_x = 118
screen_height_x = 118
image_x = Image.open("C:\\Users\\Rishikesh\\OneDrive\\Desktop\\Generate_QR_Code\\Rishikesh_Kushwaha.ico")
image_x = image_x.resize((screen_width_x, screen_height_x))
bg_image_x = ImageTk.PhotoImage(image_x)
wallpaper_label_x = CTkLabel(home_frame,image=bg_image_x,text="",width=180,height=180,fg_color="#9ac0fe",
                            corner_radius=30)
wallpaper_label_x.place(x=90, y=128)
enter_url_message = CTkLabel(home_frame,text="Enter your URL or Link here ↓",font=("Aptos",13),
                            fg_color="#F5F5FA",text_color="#262626")
enter_url_message.place(x=96,y=319)
link = StringVar()
entry_label = CTkEntry(home_frame,text_color="#444444",font=("Aptos",16,"bold"),
                        height=45,width=300,border_width=2,border_color="#a6a6a6",
                        corner_radius=10,fg_color="#eeeef6",bg_color="#F5F5FA",
                        textvariable=link)
entry_label.place(x=30,y=352)
next_btn = CTkButton(home_frame,text="Next →",font=("Aptos",19,"bold"),height=45,
                        width=300,text_color="#FFFFFF",fg_color="#4d90fe",corner_radius=10,
                        border_color="#4d90fe",border_width=2,hover_color="#67a1fe",bg_color="#F5F5FA",
                        cursor="hand2",command=CustomizePage)
next_btn.place(x=30,y=415)
page_number1 = CTkLabel(home_frame,text="●",font=("Aptos",22),fg_color="#F5F5FA",text_color="#3481fe")
page_number1.place(x=160,y=474)
page_number2 = CTkLabel(home_frame,text="●",font=("Aptos",22),fg_color="#F5F5FA",text_color="#9ac0fe")
page_number2.place(x=180,y=474)
home_frame.place(x=30,y=35)
win.mainloop()