from tkinter import *
from login import Login
import os

BLACK = "#1C2626"
WHITE = "#FFFFFF"
RED = "#FF0000"
PURPLE = "#552D96"
GREEN = "#00FF00"
GRAY = "#C4C4C4"
FONT = "Poppins"

try:
    with open("../data/class_student.json", mode="r") as file:
        pass
except:
    with open("../data/class_student.json", mode="w") as file:
        file.write("{}")

try:
    with open("../data/student.json", mode="r") as file:
        pass
except:
    with open("../data/student.json", mode="w") as file:
        file.write("{}")

path_exists = os.path.exists("../data/student_image")
if path_exists == False:
    os.makedirs("../data/student_image")

main_window = Tk()
main_window.title("FACE CARD MANAGER")
main_window.config(bg=BLACK, padx=60, pady=60)
main_window.wm_minsize(875, 600)
main_window.wm_maxsize(875, 600)
main_window.iconbitmap("../ui_image/logo.ico")

login = Login(main_window)
login.login_page()

main_window.mainloop()