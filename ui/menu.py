from tkinter import *

BLACK = "#1C2626"
WHITE = "#FFFFFF"
RED = "#FF0000"
PURPLE = "#552D96"
GREEN = "#00FF00"
GRAY = "#C4C4C4"
FONT = "Poppins"

class Menu:
    def __init__(self, main_window):
        self.main_window = main_window

    def to_login(self):
        from login import Login
        login_page = Login(self.main_window)
        login_page.login_page()

    def to_manage_class(self):
        from manage_class import ManageClass
        manage_class_page = ManageClass(self.main_window)
        manage_class_page.manage_class()

    def menu_page(self):
        from add_students import AddStudent
        add_student = AddStudent(self.main_window)
        # --------------- reset page
        for widget in self.main_window.winfo_children():
            widget.destroy()

        # --------------- menu page frame
        menu_page_frame = Frame(self.main_window, bg=BLACK)
        menu_page_frame.grid(column=0, row=0)

        # --------------- manage data label
        manage_data_label = Label(menu_page_frame, text="MANAGE DATA", fg=WHITE, bg=BLACK, font=(FONT, 35, "bold"))
        manage_data_label.grid(column=1, row=0)

        # --------------- add student picture
        canvas_add_student = Canvas(menu_page_frame, width=200, height=224, bg=BLACK, highlightthickness=0)
        menu_page_frame.add_student_image = add_student_image = PhotoImage(file=r"../ui_image/add_student_data.png")
        canvas_add_student.create_image(100,112,image=add_student_image)
        canvas_add_student.grid(column=0, row=1)

        # --------------- schedule picture
        canvas_schedule = Canvas(menu_page_frame, width=200, height=224, bg=BLACK, highlightthickness=0)
        menu_page_frame.schedule_image = schedule_image = PhotoImage(file=r"../ui_image/class_schedule.png")
        canvas_schedule.create_image(100,112,image=schedule_image)
        canvas_schedule.grid(column=1, row=1)

        # --------------- activity picture
        canvas_activity = Canvas(menu_page_frame, width=200, height=224, bg=BLACK, highlightthickness=0)
        menu_page_frame.activity_image = activity_image = PhotoImage(file=r"../ui_image/student_activity.png")
        canvas_activity.create_image(100,112,image=activity_image)
        canvas_activity.grid(column=2, row=1)

        # --------------- add student button
        add_data_button = Button(menu_page_frame, text="Add Student Data", command=add_student.add_student_data, width=18, height=1)
        add_data_button.configure(background=PURPLE, fg=WHITE, font=(FONT, 10, "bold"))
        add_data_button.grid(column=0, row=2, pady=40)

        # --------------- schedule button
        schedule_button = Button(menu_page_frame, text="Class Schedule", command=self.to_manage_class, width=18, height=1)
        schedule_button.configure(background=PURPLE, fg=WHITE, font=(FONT, 10, "bold"))
        schedule_button.grid(column=1, row=2, pady=40)

        # --------------- activity button
        activity_button = Button(menu_page_frame, text="Student Activity", command="", width=18, height=1)
        activity_button.configure(background=PURPLE, fg=WHITE, font=(FONT, 10, "bold"))
        activity_button.grid(column=2, row=2, pady=40)

        # --------------- logout button
        logout_button = Button(menu_page_frame, text="Log Out", command=self.to_login, width=14, height=1)
        logout_button.configure(background=BLACK, fg=WHITE, font=(FONT, 10, "bold"))
        logout_button.grid(column=2, row=3, sticky="EN")