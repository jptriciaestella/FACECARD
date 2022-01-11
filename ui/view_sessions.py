from tkinter import *
import json
import tkinter.ttk as tk
import tkinter.messagebox as tkm
import datetime as dt
from tkcalendar import *

BLACK = "#1C2626"
WHITE = "#FFFFFF"
RED = "#FF0000"
PURPLE = "#552D96"
GREEN = "#00FF00"
GRAY = "#C4C4C4"
FONT = "Poppins"

class ViewSessions:
    def __init__(self, main_window, class_code):
        self.main_window = main_window
        self.class_code = str(class_code)
        self.search_text = StringVar()
        self.search = ""
        self.session_data = {}
        self.selections = []
        self.status = ""

    def callback_view_sessions(self, *args):
        self.search = str(self.search_text.get())

    def vcmd_view_class(self):
        self.search_text.trace_add("write", callback=self.callback_view_sessions)

    def click_search(self, *args):
        if str(self.search_text.get()) == "Search...":
            self.search_text.set("")

    def leave_search(self, *args):
        if str(self.search_text.get()) == "":
            self.search_text.set("Search...")

    def search_session(self, *event):
        query = str(self.search)
        selections = []
        for child in self.session_table.get_children():
            item = self.session_table.item(child)["values"]
            if query.lower() in str(item[0]).lower() or query.lower() in str(item[1]).lower() or query.lower() in str(item[2]).lower():
                selections.append(child)

        self.session_table.selection_set(selections)
        try:
            self.session_table.see(str(selections[0]))
        except:
            pass

    def to_view_class_info(self):
        from view_class_info import ViewClassInfo
        mc = ViewClassInfo(self.main_window, self.class_code)
        mc.view_class_info()

    def sort_by_date(self):
        ordered = sorted(self.session_data[self.class_code]["Session"].items(), key=lambda e:dt.datetime.strptime(e[0].rsplit(" ")[1], "%d-%m-%Y"))

        ordered = {date[0]: date[1] for date in ordered}
        self.session_data[self.class_code]["Session"] = ordered

    def add_session_data(self, choosen_date):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        students =  self.session_data[self.class_code]["StudentNIM"]
        
        data = {nim: 0 for nim in students}

        date_key = f"{days[choosen_date.weekday()]} {choosen_date.day}-{choosen_date.month}-{choosen_date.year}"

        self.session_data[self.class_code]["Session"][date_key] = data
        self.session_data[self.class_code]["Session"][date_key]["Status"] = "UPCOMING"
        self.sort_by_date()

        with open("../data/class_student.json", mode="w") as file:
            file.write(json.dumps(self.session_data, indent=4))

        tkm.showinfo(parent=self.main_window, title="FACE CARD MANAGER", message="DATA SUCCESSFULLY ADDED!")

        self.view_sessions_page()

    def get_date(self):
        self.calendar_date = str(self.calendar.get_date())
        self.calendar_date = self.calendar_date.rsplit("/")
        self.calendar_date[2] = f"{self.calendar_date[2]}"
        choosen_date = self.calendar_date

        day = int(choosen_date[0])
        month = int(choosen_date[1])
        year = int(choosen_date[2])
        choosen_date = dt.datetime(year, month, day)
        month = str(choosen_date.strftime("%B")).upper()

        now = dt.datetime.now()
        now = now.replace(hour=0, minute=0, second=0, microsecond=0)
        if choosen_date < now:
            msgbox = tkm.showwarning(parent=self.main_window, title="FACE CARD MANAGER", message="CANNOT CHOOSE ELAPSED DATE!")
            return

        else:
            msgbox = tkm.askquestion(parent=self.main_window, title="FACE CARD MANAGER", message=f"ADD NEW SESSION TO {self.class_code} ON {day} {month} {year}?")
            if msgbox == "no":
                return
            elif msgbox == "yes":
                self.add_session_data(choosen_date)

    def add_session(self):
        for widget in self.main_window.winfo_children():
            widget.destroy()

        now = dt.datetime.now()

        calendar_frame = Frame(self.main_window, bg=BLACK)
        calendar_frame.grid(column=0, row=0)

        select_date_label = Label(calendar_frame, text=f"SELECT DATE", fg=WHITE, bg=BLACK, font=(FONT, 35, "bold"))
        select_date_label.grid(column=0, row=0, sticky="EW", padx=(200, 220), pady=(0, 80))

        self.calendar = Calendar(calendar_frame, selectmode="day", year=now.year, month=now.month, day=now.day, date_pattern="dd/MM/yyyy")
        self.calendar.grid(column=0, row=1, sticky="EW")

        # --------------- back button
        back_button = Button(calendar_frame, text="Cancel", command=self.to_view_class_info, width=14, height=1)
        back_button.configure(background=BLACK, fg=WHITE, font=(FONT, 12, "bold"))
        back_button.grid(column=0, row=3, pady=(50, 0), sticky="W")

        # --------------- add student button
        add_session_button = Button(calendar_frame, text="Confirm", command=self.get_date, width=14, height=1)
        add_session_button.configure(background=PURPLE, fg=WHITE, font=(FONT, 12, "bold"))
        add_session_button.grid(column=0, row=3, pady=(50, 0), sticky="E")

    def selected(self, *event):
        try:
            id = int(self.session_table.identify("item", event[0].x, event[0].y))
            children = self.session_table.get_children()
            items = self.session_table.item(children[id])["values"]
            date = str(items[0])
            self.status = str(items[1])
            self.view_absent_page(date)
        except:
            return

    def view_absent_page(self, date):
        from view_absent import ViewAbsent
        vap = ViewAbsent(self.main_window, self.class_code, date)
        vap.view_absent_page()

    def view_sessions_page(self):
        # --------------- reset
        for widget in self.main_window.winfo_children():
            widget.destroy()

        sessions_frame = Frame(self.main_window, bg=BLACK)
        sessions_frame.grid(column=0, row=0)

        search_student_label = Label(sessions_frame, text=f"VIEW SESSIONS {self.class_code}", fg=WHITE, bg=BLACK, font=(FONT, 35, "bold"))
        search_student_label.grid(column=0, row=0)

        # --------------- search
        search_bar = Entry(sessions_frame, width=80, validate="focusin", validatecommand=self.vcmd_view_class, textvariable=self.search_text)
        self.search_text.set("Search...")
        search_bar.bind("<FocusIn>", self.click_search)
        search_bar.bind("<FocusOut>", self.leave_search)
        search_bar.configure(background=GRAY, fg=BLACK, font=(FONT, 12))
        search_bar.grid(column=0, row=1, sticky="W", pady=(40, 20))

        self.main_window.bind("<Return>", self.search_session)

        # --------------- table page
        table_style = tk.Style()
        table_style.configure("Treeview", font=("Poppins", 12), rowheight=30)
        table_style.configure("Treeview.Heading", font=("Poppins", 12, "bold"))

        scrollbar = Scrollbar(sessions_frame, orient="vertical")
        scrollbar.grid(column=0, row=2, sticky="NSE")

        self.session_table = tk.Treeview(sessions_frame, yscrollcommand=scrollbar.set)
        self.session_table.grid(column=0, row=2, sticky="W")
        self.session_table.configure(height=8)

        scrollbar.config(command=self.session_table.yview)

        self.session_table["columns"] = ("Date", "Status", "Present")
        self.session_table.column("#0", width=0, stretch=NO)
        self.session_table.column("Date", anchor=CENTER, width=233, stretch=NO)
        self.session_table.column("Status", anchor=CENTER, width=233, stretch=NO)
        self.session_table.column("Present", anchor=CENTER, width=233, stretch=NO)

        self.session_table.heading("#0", text="", anchor=CENTER)
        self.session_table.heading("Date", text="Date", anchor=CENTER)
        self.session_table.heading("Status", text="Status", anchor=CENTER)
        self.session_table.heading("Present", text="Present", anchor=CENTER)

        with open("../data/class_student.json", mode="r") as file:
            self.session_data = json.load(file)
            self.sort_by_date()

        temp = self.session_data[self.class_code]["Session"]
        session_dates = [str(key) for key in temp]
        sessions = {key: temp[key] for key in temp}

        # days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        now = dt.datetime.now()
        day = now.day
        month = now.month
        year = now.year
        counter = 0
        for date in session_dates:
            self.status = self.session_data[self.class_code]["Session"][date]["Status"]
            present = "0"
            for nim in sessions[date]:
                if sessions[date][nim] == 1:
                    present = f"{int(present) + 1}"

            temp_date = date
            temp_date = date.rsplit(" ")[1].rsplit("-")
            d1 = dt.datetime(int(temp_date[2]), int(temp_date[1]), int(temp_date[0]))
            d2 = dt.datetime(year, month, day)

            if d1 > d2:
                present = "-"
            elif d1 < d2:
                self.status = "COMPLETED"
            elif d1 == d2 and self.status == "UPCOMING":
                self.status = "ONGOING"

            self.session_table.insert(parent="", index="end", iid=counter, text="", values=(str(date), str(self.status), str(present)))
            counter += 1

            self.session_data[self.class_code]["Session"][date]["Status"] = self.status
        
        if len(session_dates) == 0:
            self.session_table.insert(parent="", index="end", iid=counter, text="", values=("", "Please Enter Data to Continue", ""))

        with open("../data/class_student.json", mode="w") as file:
            file.write(str(json.dumps(self.session_data, indent=4)))

        self.main_window.bind("<Double-Button-1>", self.selected)

        with open("../data/student.json", mode="r") as file:
            temp = json.load(file)

        # --------------- back button
        back_button = Button(sessions_frame, text="Back", command=self.to_view_class_info, width=14, height=1)
        back_button.configure(background=BLACK, fg=WHITE, font=(FONT, 12, "bold"))
        back_button.grid(column=0, row=3, pady=(50, 0), sticky="W")

        # --------------- add student button
        if len(temp) == 0:
            add_session_button = Button(sessions_frame, text="Add Session", command="", width=14, height=1)
            add_session_button.configure(background=PURPLE, fg=WHITE, font=(FONT, 12, "bold"))
            add_session_button.grid(column=0, row=3, pady=(50, 0), sticky="E")
        else:
            add_session_button = Button(sessions_frame, text="Add Session", command=self.add_session, width=14, height=1)
            add_session_button.configure(background=PURPLE, fg=WHITE, font=(FONT, 12, "bold"))
            add_session_button.grid(column=0, row=3, pady=(50, 0), sticky="E")