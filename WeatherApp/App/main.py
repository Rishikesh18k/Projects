from customtkinter import *
from tkinter.messagebox import showerror
import requests
import socket
import datetime
import time

win = CTk()
win.geometry("410x580+500+60)")
win.resizable(False,False)
win.config(bg="#333333")
win.title("𝐖𝐞𝐚𝐭𝐡𝐞𝐫")
win.iconbitmap("C:\\Users\\Rishikesh\\OneDrive\\Desktop\\WeatherApp\\App\\weather_icon.ico")

def Search_page():
    def destroy_search_frame():
        search_frame.destroy()
        search_btn.configure(command=Search_page)
        search_entry.delete(0,END)
        search_entry.insert(0,'Enter City')
    def Current_Time_x():
        times = datetime.datetime.now()
        hour = times.strftime('%I')
        minuts = times.strftime('%M')
        am_pm = times.strftime('%p')
        day = times.strftime('%a')
        day_data_label_x.configure(text=day)
        hour_label_x.configure(text=hour)
        minuts_label_x.configure(text=minuts)
        am_pm_label_x.configure(text=am_pm)
        hour_label_x.after(200,Current_Time)
    def Save_City_Name():
        def check_connection():
            try:
                socket.create_connection(("Google.com",80))
                return True
            except:
                return False
        check_connection()
        if check_connection:
            your_city = cityname.get()
            with open("Current_City.txt","w") as file:
                file.write(your_city)
                file.close()
            refresh_home_page()
        else:
            showerror(title="Connection",message="No internet connection🛜")
    def Check_Temprature():
        def check_connection():
            try:
                socket.create_connection(("Google.com",80))
                return True
            except:
                return False
        check_connection()
        if check_connection():   
            try:
                city_name = cityname.get()
                data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name.lower()+"&appid=e059032dcf8a0b1ccf150a0677ddb549").json()
                state_logo_x.configure(text=data['name'])
                temprature_label_x.configure(text=str(int(data["main"] ["temp"]-273.15)))
                humidity_data_x.configure(text=str(data['main'] ["humidity"])+"%")
                cloud_name_data_x.configure(text=str(data['weather'] [0] ["main"]))
                wind_speed_data_x.configure(text=str(data['wind'] ["speed"])+" km/s")
                description_data_x.configure(text=str(data['weather'] [0] ["description"]))
                min_temprature_data_x.configure(text=str(data['main'] ["temp_min"])+"  C|F") 
            except Exception:
                def GoTo_home():
                    Invailid_City_Frame.destroy()
                    search_frame.destroy()
                    search_btn.configure(command=Search_page)
                    search_btn.configure(command=Search_page)
                    search_entry.delete(0,END)
                    search_entry.insert(0,'Enter City')
                Invailid_City_Frame = CTkFrame(win,height=580,width=410,border_width=0,border_color="#262626",
                                               corner_radius=0,fg_color="#404040")
                home_button_x = CTkButton(Invailid_City_Frame,text="⬅",font=("Arial",18),text_color="#EEEEEE",fg_color="#404040",
                                            cursor='hand2',height=34,width=30,corner_radius=6,hover_color="#4d4d4d",
                                            command=GoTo_home)
                home_button_x.place(x=10,y=10)
                message_label = CTkLabel(Invailid_City_Frame,text="𝐂𝐢𝐭𝐲 𝐧𝐨𝐭 𝐟𝐨𝐮𝐧𝐝 ⚠️",font=("Arial",22),fg_color="#404040",
                                        text_color="#FFFFFF",height=45,width=60)
                message_label.place(x=138,y=210)
                emoji_label = CTkLabel(Invailid_City_Frame,text="🙂..🤔..🥴",font=("Arial",22),fg_color="#404040",
                                        text_color="#ffcc00",height=23,width=30)
                emoji_label.place(x=165,y=250)
                Invailid_City_Frame.place(x=0,y=0)
        else:
            def refresh_connection():
                def check_connection():
                    try:
                        socket.create_connection(("Google.com",80))
                        return True
                    except:
                        return False
                check_connection()
                if check_connection():
                    Internet_Frame.destroy()
                else:
                    showerror(title="Connection", message="Please Connect your\ndevice to the Internet 🛜")
            Internet_Frame = CTkFrame(win,height=580,width=410,border_width=0,border_color="#262626",
                                               corner_radius=0,fg_color="#404040")
            connection_message = CTkLabel(Internet_Frame,text="⚠️ɴᴏ ɪɴᴛᴇʀɴᴇᴛ ᴄᴏɴɴᴇᴄᴛɪᴏɴ 🛜",font=("Arial",16),fg_color="#404040",
                                    text_color="#FFFFFF",height=45,width=60)
            connection_message.place(x=105,y=210)
            refresh_panel = CTkButton(Internet_Frame,text="Refresh",font=("Arial",12,"bold"),fg_color="#333333",border_width=0,
                                    text_color="#EEEEEE",height=35,width=30,corner_radius=50,hover_color="#4d4d4d",cursor="hand2",
                                    command=refresh_connection)
            refresh_panel.place(x=168,y=258)
            Internet_Frame.place(x=0,y=0)
    # /////////////////////////////////////////////////////////////////////////////////////////////////
    search_frame = CTkFrame(win,height=580,width=410,fg_color="#333333",corner_radius=3,border_width=0)
    def search_page_menu_button():
        def destroy_search_menu():
            menu_frame_x.destroy()
            dot_button_x.configure(command=search_page_menu_button)
        def destroy_search_menu_option(e):
            menu_frame_x.destroy()
            dot_button_x.configure(command=search_page_menu_button)
        def refresh_search_page():
            Check_Temprature()
            menu_frame_x.destroy()
            dot_button_x.configure(command=search_page_menu_button)
        menu_frame_x = CTkFrame(search_frame,height=92,width=90,fg_color="#333333",border_color="#595959",border_width=1,corner_radius=4)
        menu_frame_x.place(x=302,y=57)
        save_btn_x = CTkButton(menu_frame_x,text="Save",font=("Arial",13,"bold"),fg_color="#333333",text_color="white",
                        border_width=0,hover_color="#404040",width=88.35,corner_radius=0,height=30,cursor="hand2",
                        command=Save_City_Name)
        save_btn_x.place(x=0.70,y=30.50)
        refresh_btn_x = CTkButton(menu_frame_x,text="Refesh",font=("Arial",13,"bold"),fg_color="#333333",text_color="white",
                            border_width=0,hover_color="#404040",width=88.35,corner_radius=0,height=30,cursor="hand2",
                            command=refresh_search_page)
        refresh_btn_x.place(x=0.70,y=0.50)
        status_btn_x = CTkButton(menu_frame_x,text="Status",font=("Arial",13,"bold"),fg_color="#333333",text_color="white",
                            border_width=0,hover_color="#404040",width=88.35,corner_radius=0,height=30,cursor="hand2")
        status_btn_x.place(x=0.70,y=61)
        dot_button_x.configure(command=destroy_search_menu)
        search_frame.bind('<Button>',destroy_search_menu_option)
        temprature_label_x.bind('<Button>',destroy_search_menu_option)
        celcius_label_x.bind('<Button>',destroy_search_menu_option)
        weather_data_frame_x.bind('<Button>',destroy_search_menu_option)
        search_frame.bind('<Button>',destroy_search_menu_option)
        state_logo_x.bind('<Button>',destroy_search_menu_option)
        sun_img_label_x.bind('<Button>',destroy_search_menu_option)
    # ///////////////////////////////////////////////////////////////////////////////////////////////
    state_logo_x = CTkLabel(search_frame,text="Gorakhpur",font=("Arial",35,"bold"),fg_color="#333333",
                        text_color="yellow")
    state_logo_x.place(x=5,y=20)
    city_img_label_x = CTkLabel(search_frame,text="🏘️",font=("Arial",18),fg_color="#333333",height=22,
                            width=20,text_color="#ffffff")
    city_img_label_x.place(x=15,y=60)
    city_logo_x = CTkLabel(search_frame,text="City ●",font=("Arial",14,"bold"),fg_color="#333333",height=22,
                        width=20,text_color="#cccccc")
    city_logo_x.place(x=40,y=62)
    home_button_x = CTkButton(search_frame,text="⬅",font=("Arial",18),text_color="#EEEEEE",fg_color="#333333",
                            cursor='hand2',height=34,width=30,corner_radius=6,hover_color="#404040",command=destroy_search_frame)
    home_button_x.place(x=315,y=31)
    dot_button_x = CTkButton(search_frame,text="⋮",font=("Arial Rounded MT Bold",20),text_color="#EEEEEE",
                        fg_color="#333333",cursor='hand2',height=30,width=22,corner_radius=4,hover_color="#404040",
                        command=search_page_menu_button)
    dot_button_x.place(x=380,y=30)
    sun_label_x = CTkLabel(search_frame,text="☀️",font=("Arial",30),fg_color="#333333",text_color="#ffb833")
    sun_label_x.place(x=335,y=74)
    weather_logo_x = CTkLabel(search_frame,text="Weather",font=("Arial",18,"bold"),text_color="white",fg_color="#333333")
    weather_logo_x.place(x=325,y=90)
    hour_label_x = CTkLabel(search_frame,text="00",font=("Arial",12,"bold"),fg_color="#333333",text_color="white",
                        height=13,width=14)
    hour_label_x.place(x=336,y=119)
    col_label_x = CTkLabel(search_frame,text=":",font=("Arial",13,"bold"),fg_color="#333333",text_color="white",
                        height=13,width=8)
    col_label_x.place(x=350,y=117)
    minuts_label_x = CTkLabel(search_frame,text="00",font=("Arial",12,"bold"),fg_color="#333333",text_color="white",
                            height=13,width=14)
    minuts_label_x.place(x=358,y=119)
    am_pm_label_x = CTkLabel(search_frame,text="AM",font=("Arial",12,"bold"),fg_color="#333333",text_color="white",
                        height=12,width=15)
    am_pm_label_x.place(x=376,y=119)
    day_name_label_x = CTkLabel(search_frame,text="day -", font=("Arial",12,"bold"),fg_color="#333333",text_color="white",
                            height=14)
    day_name_label_x.place(x=340,y=137)
    day_data_label_x = CTkLabel(search_frame,text="Mon", font=("Arial",12,"bold"),fg_color="#333333",text_color="white",
                            height=14)
    day_data_label_x.place(x=371,y=137)
    sun_img_label_x = CTkLabel(search_frame,text="☀️",font=("Arial",55),fg_color="#333333",text_color="#ffb833")
    sun_img_label_x.place(x=150,y=86)
    degree_label_x = CTkLabel(search_frame,text="o",font=("Arial Rounded MT Bold",25),fg_color="#333333",width=17,
                            height=16,text_color="#ffffff")
    degree_label_x.place(x=249,y=150)
    temprature_label_x = CTkLabel(search_frame,text="....",font=("Arial Rounded MT Bold",80),text_color="white",
                                fg_color="#333333",width=62,height=60)
    temprature_label_x.place(x=150,y=152)
    celcius_label_x = CTkLabel(search_frame,text="C",font=("Arial Rounded MT Bold",35),width=30,height=22,
                            fg_color="#333333",text_color="#3bb0de")
    celcius_label_x.place(x=262,y=195)
    frame_x = CTkFrame(search_frame,border_color="#595959",border_width=1,width=350,height=2,corner_radius=0).place(x=30,y=288)
    #/////////////////////////////////////////////////////////////////////////////////////////////////////
    weather_data_frame_x = CTkFrame(search_frame,fg_color="#404040",border_width=1,border_color="#404040",
                                    height=190,width=314,corner_radius=8)
    weather_data_frame_x.place(x=50,y=340)
    humidity_label_x = CTkLabel(weather_data_frame_x,text="Humidity  :", font=("Franklin Gothic Demi Cond",18),
                            fg_color="#404040",text_color="white")
    humidity_dot_x = CTkLabel(weather_data_frame_x,text="●",font=("Arial",25),text_color="#ff5c33",fg_color="#404040").place(x=35,y=18)
    humidity_label_x.place(x=55,y=20)
    wind_label_x = CTkLabel(weather_data_frame_x,text="Wind Speed  :", font=("Franklin Gothic Demi Cond",18),
                        fg_color="#404040",text_color="white")
    wind_dot_x = CTkLabel(weather_data_frame_x,text="●",font=("Arial",25),text_color="#ffffff",fg_color="#404040").place(x=35,y=48)
    wind_label_x.place(x=55,y=50)
    description_label_x = CTkLabel(weather_data_frame_x,text="Description  :",font=("Franklin Gothic Demi Cond",18),
                                fg_color="#404040",text_color="white")
    desc_dot_x = CTkLabel(weather_data_frame_x,text="●",font=("Arial",25),text_color="#00ff00",fg_color="#404040").place(x=35,y=78)
    description_label_x.place(x=55,y=80)
    cloud_label_x = CTkLabel(weather_data_frame_x,text="Weather Climate  :", font=("Franklin Gothic Demi Cond",18),
                            fg_color="#404040",text_color="white")
    cloud_dot_x = CTkLabel(weather_data_frame_x,text="●",font=("Arial",25),text_color="#51b8e1",fg_color="#404040").place(x=35,y=108)
    cloud_label_x.place(x=55,y=110)
    min_temprature_label_x = CTkLabel(weather_data_frame_x,text="Min Temprature  :", font=("Franklin Gothic Demi Cond",18),
                                    fg_color="#404040",text_color="white")
    min_temp_dot_x = CTkLabel(weather_data_frame_x,text="●",font=("Arial",25),text_color="#ffff1a",fg_color="#404040").place(x=35,y=138)
    min_temprature_label_x.place(x=55,y=140)
    humidity_data_x = CTkLabel(weather_data_frame_x,text="-------",font=("Franklin Gothic Demi Cond",16.50),fg_color="#404040",
                            text_color="white",height=18)
    humidity_data_x.place(x=134,y=23)
    wind_speed_data_x = CTkLabel(weather_data_frame_x,text="-------", font=("Franklin Gothic Demi Cond",16.50),fg_color="#404040",
                            text_color="white",height=18)
    wind_speed_data_x.place(x=155,y=53)
    description_data_x = CTkLabel(weather_data_frame_x,text="-------",font=("Franklin Gothic Demi Cond",16.75),fg_color="#404040",
                                text_color="white",height=18)
    description_data_x.place(x=152,y=83)
    cloud_name_data_x = CTkLabel(weather_data_frame_x,text="-------", font=("Franklin Gothic Demi Cond",16.70),fg_color="#404040",
                            text_color="white",height=18)
    cloud_name_data_x.place(x=190,y=113)
    min_temprature_data_x = CTkLabel(weather_data_frame_x,text="-------",font=("Franklin Gothic Demi Cond",16),fg_color="#404040",
                                text_color="white",height=18)
    min_temprature_data_x.place(x=185,y=143)
    search_frame.place(x=0,y=0)
    Current_Time_x()
    Check_Temprature()
# //////////////////////////////////////////////////////////// 
def refresh_home_page():
    refresh_button.configure(text="•••••••", state="disabled")
    Your_City_Nature()
    refresh_button.after(400, animate_button)
def animate_button():
    refresh_button.configure(text="𝐑𝐞𝐟𝐫𝐞𝐬𝐡", state="normal", fg_color="#333333")
    time.sleep(1)
# ///////////////////////////////////////
def Current_Time():
    times = datetime.datetime.now()
    hour = times.strftime('%I')
    minuts = times.strftime('%M')
    am_pm = times.strftime('%p')
    day = times.strftime('%a')
    second = time.strftime('%S')
    second_label.configure(text=second)
    day_data_label.configure(text=day)
    hour_label.configure(text=hour)
    minuts_label.configure(text=minuts)
    am_pm_label.configure(text=am_pm)
    hour_label.after(200,Current_Time)
# ///////////////////////////////////////
def Save_City_Name():
    def check_connection():
        try:
            socket.create_connection(("Google.com",80))
            return True
        except:
            return False
    check_connection()
    if check_connection:
        your_city = "Deoria"
        with open("Current_City.txt","w") as file:
            file.write(your_city)
            file.close()
    else:
        print("No internet connection !")
# /////////////////////////////////////////////////////
def Your_City_Nature():
    def check_connection():
        try:
            socket.create_connection(("Google.com",80))
            return True
        except:
            return False
    check_connection()
    if check_connection():
        try:
            with open("Current_City.txt","r+") as file:
                your_city_data = file.read()
                file.close()
            data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+your_city_data.lower()+"&appid=e059032dcf8a0b1ccf150a0677ddb549").json()
            state_logo.configure(text=data['name'])
            temprature_label.configure(text=str(int(data["main"] ["temp"]-273.15)))
            humidity_data.configure(text=str(data['main'] ["humidity"])+"%")
            cloud_name_data.configure(text=str(data['weather'] [0] ["main"]))
            wind_speed_data.configure(text=str(data['wind'] ["speed"])+" km/s")
            description_data.configure(text=str(data['weather'] [0] ["description"]))
            min_temprature_data.configure(text=str(data['main'] ["temp_min"])+"  C|F.")
        except Exception:
            showerror(title="Invailid City",message="City not found 🙂")
    else:
        def refresh_connection():
                def check_connection():
                    try:
                        socket.create_connection(("Google.com",80))
                        return True
                    except:
                        return False
                check_connection()
                if check_connection():
                    Internet_Frame_home.destroy()
                else:
                    showerror(title="Connection", message="Please Connect your\ndevice to the Internet 🛜")
        Internet_Frame_home = CTkFrame(win,height=580,width=410,border_width=0,border_color="#262626",
                                corner_radius=0,fg_color="#404040")
        connection_message_home = CTkLabel(Internet_Frame_home,text="⚠️ɴᴏ ɪɴᴛᴇʀɴᴇᴛ ᴄᴏɴɴᴇᴄᴛɪᴏɴ 🛜",font=("Arial",16),fg_color="#404040",
                                    text_color="#FFFFFF",height=45,width=60)
        connection_message_home.place(x=105,y=210)
        refresh_panel_home = CTkButton(Internet_Frame_home,text="Refresh",font=("Arial",12,"bold"),fg_color="#333333",border_width=0,
                                    text_color="#EEEEEE",height=35,width=30,corner_radius=50,hover_color="#4d4d4d",cursor="hand2",
                                    command=refresh_connection)
        refresh_panel_home.place(x=168,y=258)
        Internet_Frame_home.place(x=0,y=0)
# //////////////////////////////////////////////////////////////////////////////////////////////////
weather_frame = CTkFrame(win,height=580,width=410,fg_color="#333333",corner_radius=3,border_width=0,)
def menu_button():
    def destroy_menu():
        menu_frame.destroy()
        dot_button.configure(command=menu_button)
    def destroy_menu_option(e):
        menu_frame.destroy()
        dot_button.configure(command=menu_button)
    menu_frame = CTkFrame(weather_frame,height=62,width=90,fg_color="#333333",border_color="#595959",border_width=1,corner_radius=4)
    menu_frame.place(x=302,y=57)
    status_btn = CTkButton(menu_frame,text="Status",font=("Arial",13,"bold"),fg_color="#333333",text_color="white",
                       border_width=0,hover_color="#404040",width=88.35,corner_radius=0,height=30,cursor="hand2")
    status_btn.place(x=0.70,y=0.50)
    about_btn = CTkButton(menu_frame,text="About",font=("Arial",13,"bold"),fg_color="#333333",text_color="white",
                        border_width=0,hover_color="#404040",width=88.35,corner_radius=0,height=30,cursor="hand2")
    about_btn.place(x=0.70,y=30.50)
    dot_button.configure(command=destroy_menu)
    weather_frame.bind('<Button>',destroy_menu_option)
    temprature_label.bind('<Button>',destroy_menu_option)
    celcius_label.bind('<Button>',destroy_menu_option)
    weather_data_frame.bind('<Button>',destroy_menu_option)
    weather_frame.bind('<Button>',destroy_menu_option)
    state_logo.bind('<Button>',destroy_menu_option)
    sun_img_labelx.bind('<Button>',destroy_menu_option)
    search_entry.bind('<Button>',destroy_menu_option)
    search_btn.bind('<Button>',destroy_menu_option)
# ///////////////////////////////////////////////////////////////////////////////////////////////
def remove_placeholder(e):
    search_entry.delete(0,END)
state_logo = CTkLabel(weather_frame,text="Gorakhpur",font=("Arial",35,"bold"),fg_color="#333333",
                      text_color="#e6e600")
state_logo.place(x=5,y=20)
city_img_label = CTkLabel(weather_frame,text="🏘️",font=("Arial",18),fg_color="#333333",height=22,
                          width=20,text_color="#ffffff")
city_img_label.place(x=15,y=60)
city_logo = CTkLabel(weather_frame,text="City ●",font=("Arial",14,"bold"),fg_color="#333333",height=22,
                     width=20,text_color="#cccccc")
city_logo.place(x=40,y=62)
refresh_button = CTkButton(weather_frame,text="𝐑𝐞𝐟𝐫𝐞𝐬𝐡",font=("Arial",17),text_color="#EEEEEE",fg_color="#333333",
                        cursor='hand2',height=34,width=30,corner_radius=6,hover_color="#404040",command=refresh_home_page)
refresh_button.place(x=310,y=30)
dot_button = CTkButton(weather_frame,text="⋮",font=("Arial Rounded MT Bold",20),text_color="#EEEEEE",
                       fg_color="#333333",cursor='hand2',height=30,width=22,corner_radius=4,hover_color="#404040",
                       command=menu_button)
dot_button.place(x=380,y=30)
sun_labelx = CTkLabel(weather_frame,text="☀️",font=("Arial",30),fg_color="#333333",text_color="#ffb833")
sun_labelx.place(x=335,y=74)
weather_logo = CTkLabel(weather_frame,text="Weather",font=("Arial",18,"bold"),text_color="white",fg_color="#333333")
weather_logo.place(x=325,y=90)
hour_label = CTkLabel(weather_frame,text="00",font=("Arial",12,"bold"),fg_color="#333333",text_color="white",
                    height=13,width=14)
hour_label.place(x=316,y=119)
col_label = CTkLabel(weather_frame,text=":",font=("Arial",13,"bold"),fg_color="#333333",text_color="white",
                    height=13,width=8)
col_label.place(x=330,y=117)
minuts_label = CTkLabel(weather_frame,text="00",font=("Arial",12,"bold"),fg_color="#333333",text_color="white",
                        height=13,width=14)
minuts_label.place(x=338,y=119)
# //////////////////////////////////////////////////////////////////////////////////
colx_label = CTkLabel(weather_frame,text=":",font=("Arial",13,"bold"),fg_color="#333333",text_color="white",
                    height=13,width=8)
colx_label.place(x=352,y=117)
second_label = CTkLabel(weather_frame,text="00",font=("Arial",12,"bold"),fg_color="#333333",text_color="white",
                        height=13,width=14)
second_label.place(x=360,y=119)
# //////////////////////////////////////////////////////////////////////////////////
am_pm_label = CTkLabel(weather_frame,text="AM",font=("Arial",12,"bold"),fg_color="#333333",text_color="white",
                       height=12,width=15)
am_pm_label.place(x=378,y=119)
day_name_label = CTkLabel(weather_frame,text="day -", font=("Arial",12,"bold"),fg_color="#333333",text_color="white",
                        height=14)
day_name_label.place(x=340,y=137)
day_data_label = CTkLabel(weather_frame,text="Mon", font=("Arial",12,"bold"),fg_color="#333333",text_color="white",
                        height=14)
day_data_label.place(x=371,y=137)
sun_img_labelx = CTkLabel(weather_frame,text="☀️",font=("Arial",52),fg_color="#333333",text_color="#ffb833")
sun_img_labelx.place(x=152,y=86)
degree_label = CTkLabel(weather_frame,text="o",font=("Arial Rounded MT Bold",24),fg_color="#333333",width=17,
                        height=16,text_color="#ffffff")
degree_label.place(x=241,y=142)
temprature_label = CTkLabel(weather_frame,text="....",font=("Arial Rounded MT Bold",76),text_color="white",
                            fg_color="#333333",width=62,height=60)
temprature_label.place(x=152,y=147)
celcius_label = CTkLabel(weather_frame,text="C",font=("Arial Rounded MT Bold",36),width=30,height=22,
                        fg_color="#333333",text_color="#3bb0de")
celcius_label.place(x=258,y=182)
cityname = StringVar(value='Enter City')
search_entry = CTkEntry(weather_frame,text_color="#b3b3b3",font=("Franklin Gothic Demi Cond",16),height=40,width=316,border_width=1,
                        border_color="#737373",corner_radius=50,fg_color="#262626",textvariable=cityname)
search_entry.place(x=50,y=270)
search_entry.bind('<Button>',remove_placeholder)
search_btn_frame = CTkFrame(weather_frame,height=36,width=70,fg_color="#262626",corner_radius=50,border_width=0)                    
search_btn = CTkButton(search_btn_frame,text="Search",font=("Franklin Gothic Demi Cond",17),height=36,width=70,text_color="#3bb0de",
                        fg_color="#262626",corner_radius=50,border_color="#333333",border_width=0,hover_color="#262626",
                        cursor="hand2",command=Search_page)
search_btn.place(x=0,y=0)
search_btn_frame.place(x=280,y=272) 
#/////////////////////////////////////////////////////////////////////////////////////////////////////
weather_data_frame = CTkFrame(weather_frame,fg_color="#404040",border_width=1,border_color="#404040",
                                height=190,width=314,corner_radius=8)
weather_data_frame.place(x=50,y=350)
humidity_label = CTkLabel(weather_data_frame,text="Humidity  :", font=("Franklin Gothic Demi Cond",18),
                        fg_color="#404040",text_color="white")
humidity_dot = CTkLabel(weather_data_frame,text="●",font=("Arial",25),text_color="#ff5c33",fg_color="#404040").place(x=35,y=18)
humidity_label.place(x=55,y=20)
wind_label = CTkLabel(weather_data_frame,text="Wind Speed  :", font=("Franklin Gothic Demi Cond",18),
                      fg_color="#404040",text_color="white")
wind_dot = CTkLabel(weather_data_frame,text="●",font=("Arial",25),text_color="#ffffff",fg_color="#404040").place(x=35,y=48)
wind_label.place(x=55,y=50)
description_label = CTkLabel(weather_data_frame,text="Description  :",font=("Franklin Gothic Demi Cond",18),
                            fg_color="#404040",text_color="white")
desc_dot = CTkLabel(weather_data_frame,text="●",font=("Arial",25),text_color="#00ff00",fg_color="#404040").place(x=35,y=78)
description_label.place(x=55,y=80)
cloud_label = CTkLabel(weather_data_frame,text="Weather Climate  :", font=("Franklin Gothic Demi Cond",18),
                        fg_color="#404040",text_color="white")
cloud_dot = CTkLabel(weather_data_frame,text="●",font=("Arial",25),text_color="#51b8e1",fg_color="#404040").place(x=35,y=108)
cloud_label.place(x=55,y=110)
min_temprature_label = CTkLabel(weather_data_frame,text="Min Temprature  :", font=("Franklin Gothic Demi Cond",18),
                                fg_color="#404040",text_color="white")
min_temp_dot = CTkLabel(weather_data_frame,text="●",font=("Arial",25),text_color="#ffff1a",fg_color="#404040").place(x=35,y=138)
min_temprature_label.place(x=55,y=140)
humidity_data = CTkLabel(weather_data_frame,text="-------",font=("Franklin Gothic Demi Cond",16.50),fg_color="#404040",
                         text_color="white",height=18)
humidity_data.place(x=134,y=23)
wind_speed_data = CTkLabel(weather_data_frame,text="-------", font=("Franklin Gothic Demi Cond",16.50),fg_color="#404040",
                           text_color="white",height=18)
wind_speed_data.place(x=155,y=53)
description_data = CTkLabel(weather_data_frame,text="-------",font=("Franklin Gothic Demi Cond",16.75),fg_color="#404040",
                            text_color="white",height=18)
description_data.place(x=152,y=83)
cloud_name_data = CTkLabel(weather_data_frame,text="-------", font=("Franklin Gothic Demi Cond",16.70),fg_color="#404040",
                           text_color="white",height=18)
cloud_name_data.place(x=190,y=113)
min_temprature_data = CTkLabel(weather_data_frame,text="-------",font=("Franklin Gothic Demi Cond",16),fg_color="#404040",
                               text_color="white",height=18)
min_temprature_data.place(x=185,y=143)
weather_frame.place(x=0,y=0)
Current_Time()
Your_City_Nature()
win.mainloop()