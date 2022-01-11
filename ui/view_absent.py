from tkinter import *
import json
import tkinter.ttk as tk
from tkcalendar import *

BLACK = "#1C2626"
WHITE = "#FFFFFF"
RED = "#FF0000"
PURPLE = "#552D96"
GREEN = "#00FF00"
GRAY = "#C4C4C4"
FONT = "Poppins"

class ViewAbsent:
    def __init__(self, main_window, class_code, date):
        self.main_window = main_window
        self.class_code = class_code
        self.date = date
        self.search_text = StringVar()
        self.search = ""
        
    def callback_view_absent(self, *args):
        self.search = str(self.search_text.get())

    def vcmd_view_absent(self):
        self.search_text.trace_add("write", callback=self.callback_view_absent)

    def click_search(self, *args):
        if str(self.search_text.get()) == "Search...":
            self.search_text.set("")

    def leave_search(self, *args):
        if str(self.search_text.get()) == "":
            self.search_text.set("Search...")
    
    def to_view_session(self):
        from view_sessions import ViewSessions
        vsp = ViewSessions(self.main_window, self.class_code)
        vsp.view_sessions_page()

    def search_student(self, *event):
        query = str(self.search)
        selections = []
        for child in self.absent_table.get_children():
            item = self.absent_table.item(child)["values"]
            if query.lower() in str(item[0]).lower() or query.lower() in str(item[1]).lower() or query.lower() in str(item[2]).lower():
                selections.append(child)

        self.absent_table.selection_set(selections)
        try:
            self.absent_table.see(str(selections[0]))
        except:
            pass

    def view_absent_page(self):
        for widget in self.main_window.winfo_children():
            widget.destroy()

        view_frame = Frame(self.main_window, bg=BLACK)
        view_frame.grid(column=0, row=0)

        absent_label = Label(view_frame, text=f"{self.date} - {self.class_code} LIST", fg=WHITE, bg=BLACK, font=(FONT, 35, "bold"))
        absent_label.grid(column=0, row=0)

        search_bar = Entry(view_frame, width=80, validate="focusin", validatecommand=self.vcmd_view_absent, textvariable=self.search_text)
        self.search_text.set("Search...")
        search_bar.bind("<FocusIn>", self.click_search)
        search_bar.bind("<FocusOut>", self.leave_search)
        search_bar.configure(background=GRAY, fg=BLACK, font=(FONT, 12))
        search_bar.grid(column=0, row=1, sticky="W", pady=(40, 20))

        with open("../data/class_student.json", mode="r") as file:
            class_data = json.load(file)

        with open("../data/student.json", mode="r") as file:
            student_data = json.load(file)

        temp = class_data[self.class_code]["Session"][self.date]
        student_name = {str(nim): str(student_data[nim]["Name"]) for nim in student_data}
        nim_absent = {str(key): str(temp[key]) for key in temp}

        table_style = tk.Style()
        table_style.configure("Treeview", font=("Poppins", 12), rowheight=30)
        table_style.configure("Treeview.Heading", font=("Poppins", 12, "bold"))

        scrollbar = Scrollbar(view_frame, orient="vertical")
        scrollbar.grid(column=0, row=2, sticky="NSE")

        self.absent_table = tk.Treeview(view_frame, yscrollcommand=scrollbar.set)
        self.absent_table.grid(column=0, row=2, sticky="W")
        self.absent_table.configure(height=8)

        scrollbar.config(command=self.absent_table.yview)

        self.absent_table["columns"] = ("Name", "Student ID", "Notes")
        self.absent_table.column("#0", width=0, stretch=NO)
        self.absent_table.column("Name", anchor=CENTER, width=233, stretch=NO)
        self.absent_table.column("Student ID", anchor=CENTER, width=233, stretch=NO)
        self.absent_table.column("Notes", anchor=CENTER, width=233, stretch=NO)

        self.absent_table.heading("#0", text="", anchor=CENTER)
        self.absent_table.heading("Name", text="Name", anchor=CENTER)
        self.absent_table.heading("Student ID", text="Student ID", anchor=CENTER)
        self.absent_table.heading("Notes", text="Notes", anchor=CENTER)

        counter = 0
        for nim in nim_absent:
            if str(nim) == "Status":
                continue

            stats = "Absent"
            if str(nim_absent[str(nim)]) == "1":
                stats = "Present"

            self.absent_table.insert(parent="", index="end", iid=counter, text="", values=(str(student_name[f"{nim}"]), str(nim), str(stats)))
            counter += 1
        
        if len(nim_absent) == 0:
            self.absent_table.insert(parent="", index="end", iid=counter, text="", values=("", "Please Enter Data to Continue", ""))

        self.main_window.bind("<Return>", self.search_student)

        # --------------- back button
        back_button = Button(view_frame, text="Back", command=self.to_view_session, width=14, height=1)
        back_button.configure(background=BLACK, fg=WHITE, font=(FONT, 12, "bold"))

        status = class_data[self.class_code]["Session"][self.date]["Status"]

        if status != "ONGOING":
            back_button.grid(column=0, row=3, pady=(50, 0), sticky="EW")

        else:
            back_button.grid(column=0, row=3, pady=(50, 0), sticky="W")

            # --------------- absent button
            scan_button = Button(view_frame, text="Start Scanning", command=self.scan_faces, width=14, height=1)
            scan_button.configure(background=PURPLE, fg=WHITE, font=(FONT, 12, "bold"))
            scan_button.grid(column=0, row=3, pady=(50, 0), sticky="E")
    
    def scan_faces(self):
        from face_scanner import FaceScanner
        fsp = FaceScanner(self.main_window, self.class_code, self.date)
        fsp.face_scanner_page()