import pandas as pd
import customtkinter as ctk
import tkinter as tk
from PIL import ImageTk, Image


class LoginPage:
    def __init__(self, master):
        self.master = master
        master.geometry('620x460')
        master.title('Login')

        ctk.set_appearance_mode('System')
        ctk.set_default_color_theme('green')

        img1 = ImageTk.PhotoImage(Image.open('Bilder\\LoginBackgrung\\pattern.png'))
        self.label = ctk.CTkLabel(master=master, image=img1)
        self.label.pack()

        self.login_frame = ctk.CTkFrame(master=self.label, width=320, height=360, corner_radius=20)
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        l2 = ctk.CTkLabel(master=self.login_frame, text='Login into your Account', font=('Century Gothic', 20))
        l2.place(x=50, y=55)
        self.entry1 = ctk.CTkEntry(master=self.login_frame, width=220, placeholder_text="Username")
        self.entry1.place(x=50, y=115)

        self.entry2 = ctk.CTkEntry(master=self.login_frame, width=220, placeholder_text="Password")
        self.entry2.place(x=50, y=175)

        l3 = ctk.CTkLabel(master=self.login_frame, text='Forget Password ?', font=('Century Gothic', 15))
        l3.place(x=140, y=205)

        self.login_button = ctk.CTkButton(master=self.login_frame, width=220, text='Login', corner_radius=6, fg_color='white', text_color='black', hover_color='#B7AD99', command=self.login_btn_fun)
        self.login_button.place(x=50, y=240)

        img2 = ImageTk.PhotoImage(Image.open('Bilder\\icons_login\\Google__G__Logo.svg.webp').resize((20,20), Image.ANTIALIAS))
        img3 = ImageTk.PhotoImage(Image.open('Bilder\\icons_login\\facebook.png').resize((20,20), Image.ANTIALIAS))

        fb_i_button = ctk.CTkButton(master=self.login_frame, width=100, height=20, image=img3, text='Facebook', corner_radius=6, compound='left', text_color='Black', fg_color='white', hover_color='#B7AD99')
        fb_i_button.place(x=50, y=290)

        google_i_button = ctk.CTkButton(master=self.login_frame, width=100, height=20, image=img2, text='Google', corner_radius=6, compound='left', text_color='Black', fg_color='white', hover_color='#B7AD99')
        google_i_button.place(x=170, y=290)


    def login_btn_fun(self):
        self.master.destroy()
        home = ctk.CTk()
        home_window = HomeWindow(home)
        home.mainloop()



class HomeWindow:
    def __init__(self, master):
        self.master = master
        master.geometry('1100x620')
        master.title('Home page')

        l1 = ctk.CTkLabel(master=master, text="Bäcker Startseite", font=('Century Gothic', 30))
        l1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


if __name__== "__main__":
    root = ctk.CTk() # ctk = customtkinter
    app = LoginPage(root)
    root.mainloop()