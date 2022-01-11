from tkinter import *
from tkinter.filedialog import askopenfilename
import json
import shutil
from PIL import Image, ImageTk

BLACK = "#1C2626"
WHITE = "#FFFFFF"
RED = "#FF0000"
PURPLE = "#552D96"
GREEN = "#00FF00"
GRAY = "#C4C4C4"
FONT = "Poppins"

class AddStudent:
    def __init__(self, main_window):
        self.name = ""
        self.id = ""
        self.dob = ""
        self.phone = ""
        self.pict_path = ""
        self.name_text = StringVar()
        self.id_text = StringVar()
        self.dob_text = StringVar()
        self.phone_text = StringVar()
        self.main_window = main_window

    def callback_add_student(self, *args):
        self.name = str(self.name_text.get())
        self.id = str(self.id_text.get())
        self.dob = str(self.dob_text.get())
        self.phone = str(self.phone_text.get())

    def vcmd_add_student(self):
        self.name_text.trace_add("write", callback=self.callback_add_student)
        self.id_text.trace_add("write", callback=self.callback_add_student)
        self.dob_text.trace_add("write", callback=self.callback_add_student)
        self.phone_text.trace_add("write", callback=self.callback_add_student)

    def open_file(self):
        self.pict_path = str(askopenfilename(filetypes=[("Image Files", ".jpg")]))
        try:
            image = Image.open(self.pict_path)
            resize_image = image.resize((200, 224))
            self.main_window.student_image = student_image = ImageTk.PhotoImage(resize_image)
            self.add_pict_button.config(image=student_image, width=200, height=224, highlightthickness=0)
        except:
            pass

    def show_error(self, message, column, row):
        error_label = Label(text=str(message), fg=RED, bg=BLACK, font=(FONT, 12))
        error_label.grid(column=column, row=row)
        self.main_window.after(2000, error_label.destroy)

    def add_student_func(self, *event):
        if str(self.pict_path) == "":
            return self.show_error("Please Upload Your Photo!", 0, 7)
            
        if len(self.name)<=0 or len(self.id)<=0 or len(self.dob)<=0 or len(self.phone)<=0:
            return self.show_error("Please Complete the Field!", 0, 7)
            
        destination = f"../data/student_image/{self.id}.jpg"
        shutil.copyfile(self.pict_path, destination)

        data = {
            f"{self.id}":{
                "Name": f"{self.name}",
                "DOB": f"{self.dob}",
                "Phone": f"{self.phone}",
                "Path": f"{destination}",
            }
        }

        with open(f"../data/student.json", mode="r") as file:
            student_dict = json.load(file)

        student_dict.update(data)

        with open(f"../data/student.json", mode="w") as file:
            file.write((json.dumps(student_dict, indent=4, sort_keys=True)))
        
        indicator_label = Label(text="Student Added!", fg=GREEN, bg=BLACK, font=(FONT, 12, "bold"))
        indicator_label.grid(column=0, row=7)
        self.main_window.after(1000, func=self.to_menu)

    def to_menu(self):
        from menu import Menu
        menu = Menu(self.main_window)
        menu.menu_page()

    def add_student_data(self):
        # --------------- reset page
        for widget in self.main_window.winfo_children():
            widget.destroy()

        # --------------- student data page frame
        student_data_page = Frame(self.main_window, bg=BLACK)
        student_data_page.grid(column=0, row=0)

        # --------------- student data label
        add_student_data_label = Label(student_data_page, text="ADD STUDENT DATA", fg=WHITE, bg=BLACK, font=(FONT, 35, "bold"))
        add_student_data_label.grid(column=1, row=0, columnspan=2)

        # --------------- student pict
        student_data_page.student_image = student_image = PhotoImage(file=r"../ui_image/not_found.png")
        self.add_pict_button = Button(student_data_page, image=student_image, command=self.open_file, width=200, height=224, highlightthickness=0)
        self.add_pict_button.configure(bg=BLACK, fg=WHITE)
        self.add_pict_button.grid(column=0, row=1, rowspan=5)

        # --------------- student info label
        info_label = Label(student_data_page, text="STUDENT INFO:", fg=WHITE, bg=BLACK, font=(FONT, 16))
        info_label.grid(column=1, row=1, columnspan=2)

        # --------------- name
        name_label = Label(student_data_page, text="Name:", fg=WHITE, bg=BLACK, font=(FONT, 12))
        name_label.grid(column=1, row=2)

        name_entry = Entry(student_data_page, width=30, validate="focusin", validatecommand=self.vcmd_add_student, textvariable=self.name_text)
        self.name_text.set("")
        name_entry.focus()
        name_entry.configure(background=BLACK, fg=WHITE, font=(FONT, 12))
        name_entry.grid(column=2, row=2, ipady=3)

        # --------------- id
        id_label = Label(student_data_page, text="Student ID:", fg=WHITE, bg=BLACK, font=(FONT, 12))
        id_label.grid(column=1, row=3)

        id_entry = Entry(student_data_page, width=30, validate="focusin", validatecommand=self.vcmd_add_student, textvariable=self.id_text)
        self.id_text.set("")
        id_entry.configure(background=BLACK, fg=WHITE, font=(FONT, 12))
        id_entry.grid(column=2, row=3, ipady=3)

        # --------------- dob
        dob_label = Label(student_data_page, text="DOB:", fg=WHITE, bg=BLACK, font=(FONT, 12))
        dob_label.grid(column=1, row=4)

        dob_entry = Entry(student_data_page, width=30, validate="focusin", validatecommand=self.vcmd_add_student, textvariable=self.dob_text)
        self.dob_text.set("")
        dob_entry.configure(background=BLACK, fg=WHITE, font=(FONT, 12))
        dob_entry.grid(column=2, row=4, ipady=3)

        # --------------- phone
        phone_label = Label(student_data_page, text="Phone:", fg=WHITE, bg=BLACK, font=(FONT, 12))
        phone_label.grid(column=1, row=5)

        phone_entry = Entry(student_data_page, width=30, validate="focusin", validatecommand=self.vcmd_add_student, textvariable=self.phone_text)
        self.phone_text.set("")
        phone_entry.configure(background=BLACK, fg=WHITE, font=(FONT, 12))
        phone_entry.grid(column=2, row=5, ipady=3)

        # --------------- cancel button
        cancel_button = Button(student_data_page, text="Cancel", command=self.to_menu, width=14, height=1)
        cancel_button.configure(background=BLACK, fg=WHITE, font=(FONT, 12, "bold"))
        cancel_button.grid(column=0, row=6, pady=60)

        # --------------- save button
        save_button = Button(student_data_page, text="Save Data", command=self.add_student_func, width=14, height=1)
        save_button.configure(background=PURPLE, fg=WHITE, font=(FONT, 12, "bold"))
        save_button.grid(column=2, row=6, pady=60, columnspan=2, sticky="E")

        # --------------- save button using enter
        self.main_window.bind("<Return>", self.add_student_func)