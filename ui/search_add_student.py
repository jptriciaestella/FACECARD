from tkinter import *
import json
import tkinter.ttk as tk

BLACK = "#1C2626"
WHITE = "#FFFFFF"
RED = "#FF0000"
PURPLE = "#552D96"
GREEN = "#00FF00"
GRAY = "#C4C4C4"
FONT = "Poppins"

# sas = SearchAddStudent(self.main_window, self.info_dict, self.student)
# sas.search_student_page()
class SearchAddStudent:
    def __init__(self, main_window, class_code):
        self.main_window = main_window
        self.class_code = class_code
        self.search_text = StringVar()
        self.search = ""
        self.selections = []

    def search_student(self, *event):
        query = str(self.search)
        self.selections.clear()
        for child in self.student_table.get_children():
            item = self.student_table.item(child)["values"]
            if query.lower() in str(item[0]).lower() or query.lower() in str(item[1]).lower():
                self.selections.append(child)

        self.student_table.selection_set(self.selections)
        try:
            self.student_table.see(str(self.selections[0]))
        except:
            pass

    def callback_view_class(self, *args):
        self.search = str(self.search_text.get())

    def vcmd_view_class(self):
        self.search_text.trace_add("write", callback=self.callback_view_class)

    def click_search(self, *args):
        if str(self.search_text.get()) == "Search...":
            self.search_text.set("")

    def leave_search(self, *args):
        if str(self.search_text.get()) == "":
            self.search_text.set("Search...")

    def to_view_class_info(self):
        from view_class_info import ViewClassInfo
        mc = ViewClassInfo(self.main_window, self.class_code)
        mc.view_class_info()

    # ----------------------------------- add student ----------------------------------- #
    def selected(self, event):
        try:
            id = int(self.student_table.identify("item", event.x, event.y))
            self.selections.clear()
            children = self.student_table.get_children()
            items = self.student_table.item(children[id])["values"]
            self.selections.append(items)
            self.student_table.selection_set(self.selections)
            self.student_table.see(str(self.selections[0]))
        except:
            return

    def refresh(self):
        self.selections.clear()
        self.search_add_student_page()

    def add_student(self):
        indicator_label = Label(bg=BLACK, font=(FONT, 12))
        if len(self.selections) != 1:
            indicator_label.configure(text="Please Select the Student!", fg=RED)
            indicator_label.grid(column=0, row=4)
            self.main_window.after(1000, indicator_label.destroy)

        id = str(self.selections[0][1])

        with open("../data/class_student.json", mode="r") as file:
            info_dict = json.load(file)
        
        info_dict[self.class_code]["StudentNIM"].append(id)

        with open("../data/class_student.json", mode="w") as file:
            file.write(json.dumps(info_dict, indent=4, sort_keys=True))

        indicator_label.configure(text="Student Added", fg=GREEN)
        indicator_label.grid(column=0, row=4)
        self.main_window.after(1000, self.refresh)

    # ----------------------------------- ui uaa ----------------------------------- #
    def search_add_student_page(self):
        # --------------- reset
        for widget in self.main_window.winfo_children():
            widget.destroy()

        search_frame = Frame(self.main_window, bg=BLACK)
        search_frame.grid(column=0, row=0)

        search_student_label = Label(search_frame, text=f"SEARCH STUDENT", fg=WHITE, bg=BLACK, font=(FONT, 35, "bold"))
        search_student_label.grid(column=0, row=0)

        # --------------- search
        search_bar = Entry(search_frame, width=80, validate="focusin", validatecommand=self.vcmd_view_class, textvariable=self.search_text)
        self.search_text.set("Search...")
        search_bar.bind("<FocusIn>", self.click_search)
        search_bar.bind("<FocusOut>", self.leave_search)
        search_bar.configure(background=GRAY, fg=BLACK, font=(FONT, 12))
        search_bar.grid(column=0, row=1, sticky="W", pady=(40, 20))

        self.main_window.bind("<Return>", self.search_student)
        self.main_window.bind("<Button-1>", self.selected)

        # --------------- table page
        table_style = tk.Style()
        table_style.configure("Treeview", font=("Poppins", 12), rowheight=30)
        table_style.configure("Treeview.Heading", font=("Poppins", 12, "bold"))

        scrollbar = Scrollbar(search_frame, orient="vertical")
        scrollbar.grid(column=0, row=2, sticky="NSE")

        self.student_table = tk.Treeview(search_frame, yscrollcommand=scrollbar.set)
        self.student_table.grid(column=0, row=2, sticky="W")
        self.student_table.configure(height=8)

        scrollbar.config(command=self.student_table.yview)

        self.student_table["columns"] = ("Name", "Student ID")
        self.student_table.column("#0", width=0, stretch=NO)
        self.student_table.column("Name", anchor=CENTER, width=350, stretch=NO)
        self.student_table.column("Student ID", anchor=CENTER, width=350, stretch=NO)

        self.student_table.heading("#0", text="", anchor=CENTER)
        self.student_table.heading("Name", text="Name", anchor=CENTER)
        self.student_table.heading("Student ID", text="Student ID", anchor=CENTER)

        with open("../data/student.json", mode="r") as file:
            student_data = json.load(file)

        classNIM = []
        allNIM = [nim for nim in student_data]

        with open("../data/class_student.json", mode="r") as file:
            temp = json.load(file)
            classNIM.extend(temp[self.class_code]["StudentNIM"])

        counter = 0
        for nim in allNIM:
            if not(nim in classNIM):
                name = student_data[nim]["Name"]
                self.student_table.insert(parent="", index="end", iid=counter, text="", values=(f"{name}", f"{nim}"))
                counter += 1
        if len(allNIM) == 0:
            self.student_table.insert(parent="", index="end", iid=counter, text="", values=("Please Enter Data to Continue", ""))
        
        # --------------- back button
        back_button = Button(search_frame, text="Back", command=self.to_view_class_info, width=14, height=1)
        back_button.configure(background=BLACK, fg=WHITE, font=(FONT, 12, "bold"))
        back_button.grid(column=0, row=3, pady=(50, 0), sticky="W")

        # --------------- add student button
        if len(allNIM) == 0:
            add_student_button = Button(search_frame, text="Add", command=self.add_student, width=14, height=1)
            add_student_button.configure(background=PURPLE, fg=WHITE, font=(FONT, 12, "bold"))
            add_student_button.grid(column=0, row=3, pady=(50, 0), sticky="E")
        else:
            add_student_button = Button(search_frame, text="Add", command=self.add_student, width=14, height=1)
            add_student_button.configure(background=PURPLE, fg=WHITE, font=(FONT, 12, "bold"))
            add_student_button.grid(column=0, row=3, pady=(50, 0), sticky="E")