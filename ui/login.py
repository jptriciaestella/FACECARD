from tkinter import *
import json
from menu import Menu

BLACK = "#1C2626"
WHITE = "#FFFFFF"
RED = "#FF0000"
PURPLE = "#552D96"
GREEN = "#00FF00"
GRAY = "#C4C4C4"
FONT = "Poppins"
class Login:
    def __init__(self, main_window):
        self.username = ""
        self.password = ""
        self.username_text = StringVar()
        self.password_text = StringVar()
        self.main_window = main_window
        self.menu = Menu(main_window)

        with open("../data/admin.json", mode="r") as file:
            self.admin_dict = json.load(file)

    # ----------------------------------- login function ----------------------------------- #
    def callback_login(self, *args):
        self.username = str(self.username_text.get())
        self.password = str(self.password_text.get())

    def vcmd_login(self):
        self.username_text.trace_add("write", callback=self.callback_login)
        self.password_text.trace_add("write", callback=self.callback_login)

    def login_func(self, *event):
        try:
            if len(self.username)>0 and len(self.password)>0 and str(self.password) == str(self.admin_dict[f"{self.username}"]):
                self.menu.menu_page()
            else:
                wrong_cred_label = Label(text="Wrong Credentials", fg=RED, bg=BLACK, font=(FONT, 16))
                wrong_cred_label.grid(column=0, row=4)
        except:
            wrong_cred_label = Label(text="Enter Your Username and Password!", fg=RED, bg=BLACK, font=(FONT, 16))
            wrong_cred_label.grid(column=0, row=4)

    # ----------------------------------- login page ----------------------------------- #
    def login_page(self):
        # --------------- reset page
        for widget in self.main_window.winfo_children():
            widget.destroy()
        
        # --------------- login page frame
        login_page_frame = Frame(self.main_window, bg=BLACK)
        login_page_frame.grid(column=0, row=0)

        # --------------- login admin label
        login_admin_label = Label(login_page_frame, text="LOGIN ADMIN", fg=WHITE, bg=BLACK, font=(FONT, 35, "bold"))
        login_admin_label.grid(column=0, row=0)

        # --------------- admin picture
        canvas_admin = Canvas(login_page_frame, width=200, height=224, bg=BLACK, highlightthickness=0)
        login_page_frame.admin_image = admin_image = PhotoImage(file=r"../ui_image/admin_page.png")
        canvas_admin.create_image(100, 112, image=admin_image)
        canvas_admin.grid(column=0, row=1)

        # --------------- username input entry
        username_label = Label(login_page_frame, text="username", font=(FONT, 10), bg=BLACK, fg=WHITE)
        username_label.grid(column=0, row=2, sticky="W")

        username_entry = Entry(login_page_frame, width=62, validate="focusin", validatecommand=self.vcmd_login, textvariable=self.username_text)
        username_entry.configure(background=BLACK, fg=WHITE, font=(FONT, 16))
        username_entry.grid(column=0, row=3, pady=3, ipady=3)

        # --------------- password input entry
        password_label = Label(login_page_frame, text="password", font=(FONT, 10), bg=BLACK, fg=WHITE)
        password_label.grid(column=0, row=4, sticky="W")

        password_entry = Entry(login_page_frame, width=62, validatecommand=self.vcmd_login, textvariable=self.password_text, show="*")
        password_entry.configure(background=BLACK, fg=WHITE, font=(FONT, 16))
        password_entry.grid(column=0, row=5, ipady=3, pady=3)

        # --------------- sign in button
        sign_in_button = Button(login_page_frame, text="Sign in", command=self.login_func, width=14, height=1)
        sign_in_button.configure(background=PURPLE, fg=WHITE, font=(FONT, 16, "bold"))
        sign_in_button.grid(column=0, row=6, pady=20)

        # --------------- bind enter to login function
        self.main_window.bind("<Return>", self.login_func)