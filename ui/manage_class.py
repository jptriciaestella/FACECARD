from tkinter import *
import tkinter.ttk as tk
import json

BLACK = "#1C2626"
WHITE = "#FFFFFF"
RED = "#FF0000"
PURPLE = "#552D96"
GREEN = "#00FF00"
GRAY = "#C4C4C4"
FONT = "Poppins"

class ManageClass:
    def __init__(self, main_window):
        self.main_window = main_window
        self.search_text = StringVar()
        self.class_text = StringVar()
        self.course_text = StringVar()
        self.lec_text = StringVar()
        self.time_text = StringVar()
        self.search = ""
        self.class_name = ""
        self.course_name = ""
        self.lec_name = ""
        self.time_stamp = ""
        
        with open("../data/class_student.json", mode="r") as file:
            self.class_dict = json.load(file)

    # -------------------------------------------- add class function -------------------------------------------- #
    def callback_add_class(self, *args):
        self.class_name = str(self.class_text.get())
        self.course_name = str(self.course_text.get())
        self.lec_name = str(self.lec_text.get())
        self.time_stamp = str(self.time_text.get())

    def vcmd_add_class(self):
        self.class_text.trace_add("write", callback=self.callback_add_class)
        self.course_text.trace_add("write", callback=self.callback_add_class)
        self.lec_text.trace_add("write", callback=self.callback_add_class)
        self.time_text.trace_add("write", callback=self.callback_add_class)

    def add_new_schedule(self, *event):
        if len(self.class_name)<=0 or len(self.course_name)<=0 or len(self.lec_name)<=0 or len(self.time_stamp)<=0:
            self.indicator_label.configure(text="Please Enter the Field!", fg=RED)
            return self.add_frame.after(1000, func=self.add_class_schedule)

        key_checker = [key for key in self.class_dict]
        if self.class_name in key_checker:
            self.indicator_label.configure(text="Class Already Exists!", fg=RED)
            return self.add_frame.after(1000, func=self.add_class_schedule)
        
        data = {
            "Subject": str(self.course_name),
            "StudentNIM": [],
            "Lecturer": str(self.lec_name),
            "Time": str(self.time_stamp),
            "Session":{}
        }
        self.class_dict[f"{self.class_name}"] = data

        with open("../data/class_student.json", mode="w") as file:
            file.write(str(json.dumps(self.class_dict, indent=4, sort_keys=True)))

        self.indicator_label.configure(text="Class Added!", fg=GREEN)
        self.add_frame.after(1000, func=self.manage_class)

    # -------------------------------------------- add class ui -------------------------------------------- #
    def add_class_schedule(self):
        # --------------- reset page
        for widget in self.main_window.winfo_children():
            widget.destroy()

        with open("../data/class_student.json", mode="r") as file:
            self.class_dict = json.load(file)
        
        self.add_frame = Frame(self.main_window, bg=BLACK)
        self.add_frame.grid(column=0, row=0)

        # --------------- label add schedule
        add_schedule_label = Label(self.add_frame, text="ADD CLASS SCHEDULE", fg=WHITE, bg=BLACK, font=(FONT, 35, "bold"))
        add_schedule_label.grid(column=0, row=0, columnspan=3, pady=(0, 20))

        # --------------- class name label and entry
        class_name_label = Label(self.add_frame, text="Class Name", fg=WHITE, bg=BLACK, font=(FONT, 12))
        class_name_label.grid(column=1, row=1, sticky="W")

        class_entry = Entry(self.add_frame, textvariable=self.class_text, width=35, validate="focusin", validatecommand=self.vcmd_add_class)
        class_entry.configure(background=BLACK, fg=WHITE, font=(FONT, 16))
        self.class_text.set("")
        class_entry.grid(column=1, row=2, pady=(0, 10), sticky="W")

        # --------------- course name label and entry
        course_name_label = Label(self.add_frame, text="Course Name", fg=WHITE, bg=BLACK, font=(FONT, 12))
        course_name_label.grid(column=1, row=3, sticky="W")

        course_name_entry = Entry(self.add_frame, textvariable=self.course_text, width=35, validate="focusin", validatecommand=self.vcmd_add_class)
        course_name_entry.configure(background=BLACK, fg=WHITE, font=(FONT, 16))
        self.course_text.set("")
        course_name_entry.grid(column=1, row=4, pady=(0, 10), sticky="W")

        # --------------- lecturer name label and entry
        lec_name_label = Label(self.add_frame, text="Lecturer", fg=WHITE, bg=BLACK, font=(FONT, 12))
        lec_name_label.grid(column=1, row=5, sticky="W")

        lec_name_entry = Entry(self.add_frame, textvariable=self.lec_text, width=35, validate="focusin", validatecommand=self.vcmd_add_class)
        lec_name_entry.configure(background=BLACK, fg=WHITE, font=(FONT, 16))
        self.lec_text.set("")
        lec_name_entry.grid(column=1, row=6, pady=(0, 10), sticky="W")

        # --------------- time label and entry
        time_label = Label(self.add_frame, text="Time", fg=WHITE, bg=BLACK, font=(FONT, 12))
        time_label.grid(column=1, row=7, sticky="W")

        time_entry = Entry(self.add_frame, textvariable=self.time_text, width=35, validate="focusin", validatecommand=self.vcmd_add_class)
        time_entry.configure(background=BLACK, fg=WHITE, font=(FONT, 16))
        self.time_text.set("")
        time_entry.grid(column=1, row=8, pady=(0, 10), sticky="W")

        # --------------- indicator label
        self.indicator_label = Label(self.add_frame, text="", fg=GREEN, bg=BLACK, font=(FONT, 12, "bold"))
        self.indicator_label.grid(column=1, row=9, pady=(50, 50))

        # --------------- cancel button
        cancel_button = Button(self.add_frame, text="Cancel", command=self.manage_class, width=14, height=1)
        cancel_button.configure(background=BLACK, fg=WHITE, font=(FONT, 12, "bold"))
        cancel_button.grid(column=0, row=10, sticky="E")

        # --------------- add new button
        add_new_button = Button(self.add_frame, text="Add New", command=self.add_new_schedule, width=14, height=1)
        add_new_button.configure(background=PURPLE, fg=WHITE, font=(FONT, 12, "bold"))
        add_new_button.grid(column=2, row=10, sticky="W")

        # --------------- add new enter
        self.main_window.bind("<Return>", self.add_new_schedule)

    # -------------------------------------------- manage class function -------------------------------------------- #
    def callback_manage_class(self, *args):
        self.search = str(self.search_text.get())

    def vcmd_manage_class(self):
        self.search_text.trace_add("write", callback=self.callback_manage_class)

    def click_search(self, *args):
        if str(self.search_text.get()) == "Search...":
            self.search_text.set("")

    def leave_search(self, *args):
        if str(self.search_text.get()) == "":
            self.search_text.set("Search...")

    def to_menu(self):
        from menu import Menu
        menu_page = Menu(self.main_window)
        menu_page.menu_page()

    def class_info(self, *event):
        try:
            select = self.schedule_table.focus()
            class_code = dict(self.schedule_table.item(select))
            class_code = class_code["values"][0]

            from view_class_info import ViewClassInfo
            vci = ViewClassInfo(self.main_window, class_code)
            vci.view_class_info()
        except:
            return

    # -------------------------------------------- search class ui -------------------------------------------- #
    def search_class(self, *event):
        query = str(self.search)
        selections = []
        for child in self.schedule_table.get_children():
            item = self.schedule_table.item(child)["values"]
            if query.lower() in item[0].lower() or query.lower() in item[1].lower() or query.lower() in item[2].lower():
                selections.append(child)

        self.schedule_table.selection_set(selections)
        try:
            self.schedule_table.see(str(selections[0]))
        except:
            pass

    # -------------------------------------------- manage class ui -------------------------------------------- #
    def manage_class(self):
        # --------------- reset page
        for widget in self.main_window.winfo_children():
            widget.destroy()
        
        manage_class_frame = Frame(self.main_window, bg=BLACK)
        manage_class_frame.grid(column=0, row=0)

        manage_class_label = Label(manage_class_frame, text="MANAGE CLASS SCHEDULE", fg=WHITE, bg=BLACK, font=(FONT, 35, "bold"))
        manage_class_label.grid(column=0, row=0, padx=50, columnspan=2)

        # --------------- search
        search_bar = Entry(manage_class_frame, width=60, validate="focusin", validatecommand=self.vcmd_manage_class, textvariable=self.search_text)
        self.search_text.set("Search...")
        search_bar.bind("<FocusIn>", self.click_search)
        search_bar.bind("<FocusOut>", self.leave_search)
        search_bar.configure(background=GRAY, fg=BLACK, font=(FONT, 16))
        search_bar.grid(column=0, row=1, padx=10, pady=10, columnspan=2)

        self.main_window.bind("<Return>", self.search_class)

        # --------------- table page
        table_style = tk.Style()
        table_style.configure("Treeview", font=("Poppins", 12), rowheight=30)
        table_style.configure("Treeview.Heading", font=("Poppins", 12, "bold"))

        scrollbar = Scrollbar(manage_class_frame, orient="vertical")
        scrollbar.grid(column=1, row=2, sticky="NSE", columnspan=2)

        self.schedule_table = tk.Treeview(manage_class_frame, yscrollcommand=scrollbar.set)
        self.schedule_table.grid(column=0, row=2, columnspan=2, sticky="W")

        scrollbar.config(command=self.schedule_table.yview)

        self.schedule_table["columns"] = ("Class", "Course", "Time")
        self.schedule_table.column("#0", width=0, stretch=NO)
        self.schedule_table.column("Class", anchor=CENTER, width=130, stretch=NO)
        self.schedule_table.column("Course", anchor=CENTER, width=300, stretch=NO)
        self.schedule_table.column("Time", anchor=CENTER, width=300, stretch=NO)

        self.schedule_table.heading("#0", text="", anchor=CENTER)
        self.schedule_table.heading("Class", text="Class", anchor=CENTER)
        self.schedule_table.heading("Course", text="Course", anchor=CENTER)
        self.schedule_table.heading("Time", text="Time", anchor=CENTER)

        self.main_window.bind("<Double-Button-1>", self.class_info)

        counter = 0
        for class_code in self.class_dict:
            subject = self.class_dict[class_code]["Subject"]
            time_stamp = self.class_dict[class_code]["Time"]
            self.schedule_table.insert(parent="", index="end", iid=counter, text="", values=(f"{class_code}", f"{subject}", f"{time_stamp}"))
            counter += 1
        
        if len(self.class_dict) == 0:
            self.schedule_table.insert(parent="", index="end", iid=counter, text="", values=("", "Please Enter Data to Continue", ""))

        # --------------- back button
        back_button = Button(manage_class_frame, text="Back", command=self.to_menu, width=14, height=1)
        back_button.configure(background=BLACK, fg=WHITE, font=(FONT, 12, "bold"))
        back_button.grid(column=0, row=3, pady=20, sticky="W")

        # --------------- add class button
        add_class_button = Button(manage_class_frame, text="Add New", command=self.add_class_schedule, width=14, height=1)
        add_class_button.configure(background=PURPLE, fg=WHITE, font=(FONT, 12, "bold"))
        add_class_button.grid(column=1, row=3, pady=20, sticky="E")