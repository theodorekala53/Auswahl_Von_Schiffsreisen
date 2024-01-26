import pandas as pd
import customtkinter
import tkinter as tk
from PIL import ImageTk, Image
import time

class SplashScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Splash Screen')

        width_of_window = 427
        height_of_window = 250
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width_of_window / 2)
        y_coordinate = (screen_height / 2) - (height_of_window / 2)
        self.root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
        self.root.overrideredirect(1)

        tk.Frame(self.root, width=427, height=250, bg='#272727').place(x=0, y=0)
        label1 = tk.Label(self.root, text='PROGRAMMED', fg='white', bg='#272727')
        label1.configure(font=("Game Of Squids", 24, "bold"))
        label1.place(x=80, y=90)

        label2 = tk.Label(self.root, text='Loading...', fg='white', bg='#272727')
        label2.configure(font=("Calibri", 11))
        label2.place(x=10, y=215)

        self.image_a = ImageTk.PhotoImage(Image.open('Bilder\loginpunkte\c1.png'))
        self.image_b = ImageTk.PhotoImage(Image.open('Bilder\loginpunkte\c2.png'))

    def animate(self):
        for i in range(2):
            l1 = tk.Label(self.root, image=self.image_a, border=0, relief=tk.SUNKEN)
            l1.place(x=180, y=145)
            l2 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN)
            l2.place(x=200, y=145)
            l3 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN)
            l3.place(x=220, y=145)
            l4 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN)
            l4.place(x=240, y=145)
            self.root.update_idletasks()
            time.sleep(0.5)

            l1 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN)
            l1.place(x=180, y=145)
            l2 = tk.Label(self.root, image=self.image_a, border=0, relief=tk.SUNKEN)
            l2.place(x=200, y=145)
            l3 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN)
            l3.place(x=220, y=145)
            l4 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN)
            l4.place(x=240, y=145)
            self.root.update_idletasks()
            time.sleep(0.5)

            l1 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN)
            l1.place(x=180, y=145)
            l2 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN)
            l2.place(x=200, y=145)
            l3 = tk.Label(self.root, image=self.image_a, border=0, relief=tk.SUNKEN)
            l3.place(x=220, y=145)
            l4 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN)
            l4.place(x=240, y=145)
            self.root.update_idletasks()
            time.sleep(0.5)

            l1 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN)
            l1.place(x=180, y=145)
            l2 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN)
            l2.place(x=200, y=145)
            l3 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN)
            l3.place(x=220, y=145)
            l4 = tk.Label(self.root, image=self.image_a, border=0, relief=tk.SUNKEN)
            l4.place(x=240, y=145)
            self.root.update_idletasks()
            time.sleep(0.5)

    def run(self):
        self.root.after(0, self.animate)
        self.root.mainloop()


class HomeWindow:
    def __init__(self, master):
        self.master = master
        master.geometry('1280x720')
        master.title('Willkommen Bei Bäcker')

        l1 = customtkinter.CTkLabel(master=master, text="Willkommen Bei Bäcker", font=('Century Gothic', 30))
        l1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


class LoginApp:
    def __init__(self, master):
        self.master = master
        master.geometry("600x440")
        master.title("Login")

        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("green")

        img1 = ImageTk.PhotoImage(Image.open('Bilder\\LoginBackgrung\\pattern.png'))
        self.label = customtkinter.CTkLabel(master=master, image=img1)
        self.label.pack()

        self.login_frame = customtkinter.CTkFrame(master=self.label, width=320, height=360, corner_radius=20)
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        l2 = customtkinter.CTkLabel(master=self.login_frame, text='Login into your Account', font=('Century Gothic', 20))
        l2.place(x=50, y=55)
        self.entry1 = customtkinter.CTkEntry(master=self.login_frame, width=220, placeholder_text="Username")
        self.entry1.place(x=50, y=115)

        self.entry2 = customtkinter.CTkEntry(master=self.login_frame, width=220, placeholder_text="Password")
        self.entry2.place(x=50, y=175)

        l3 = customtkinter.CTkLabel(master=self.login_frame, text='Forget Password ?', font=('Century Gothic', 15))
        l3.place(x=140, y=205)

        self.login_button = customtkinter.CTkButton(master=self.login_frame, width=220, text='Login', corner_radius=6, fg_color='white', text_color='black', hover_color='#B7AD99', command=self.login_btn_fun)
        self.login_button.place(x=50, y=240)

        img2 = ImageTk.PhotoImage(Image.open('Bilder\\icons_login\\Google__G__Logo.svg.webp').resize((20,20), Image.ANTIALIAS))
        img3 = ImageTk.PhotoImage(Image.open('Bilder\\icons_login\\facebook.png').resize((20,20), Image.ANTIALIAS))

        fb_i_button = customtkinter.CTkButton(master=self.login_frame, width=100, height=20, image=img3, text='Facebook', corner_radius=6, compound='left', text_color='Black', fg_color='white', hover_color='#B7AD99')
        fb_i_button.place(x=50, y=290)

        google_i_button = customtkinter.CTkButton(master=self.login_frame, width=100, height=20, image=img2, text='Google', corner_radius=6, compound='left', text_color='Black', fg_color='white', hover_color='#B7AD99')
        google_i_button.place(x=170, y=290)

    def login_btn_fun(self):
        self.master.destroy()
        splash_screen = SplashScreen()
        splash_screen.run()
        home = customtkinter.CTk()
        home_window = HomeWindow(home)
        home.mainloop()

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = LoginApp(root)
    root.mainloop()
