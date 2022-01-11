import face_recognition
import cv2 as cv
import numpy as np
from tkinter import *
import json
from tkcalendar import *
import imutils
import tkinter.messagebox as tkm

BLACK = "#1C2626"
WHITE = "#FFFFFF"
RED = "#FF0000"
PURPLE = "#552D96"
GREEN = "#00FF00"
GRAY = "#C4C4C4"
FONT = "Poppins"

class FaceScanner:
    def __init__(self, main_window, class_code, date):
        self.main_window = main_window
        self.class_code = class_code
        self.date = date
        self.absent = []
        self.thread = None
        self.camera = cv.VideoCapture(0)

    def cam_to_tk(self):
        try:
            while True:
                return_value, frame = self.camera.read()
                frame = imutils.resize(frame, width=500, height=300)

                rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                rgb_frame = cv.resize(frame, (0, 0), None, 0.25, 0.25)

                student = {"Name": "Unknown", "NIM": "Unknown"}
                cam_face_loc = face_recognition.face_locations(rgb_frame)
                cam_face_encode = face_recognition.face_encodings(rgb_frame, cam_face_loc)

                for face in cam_face_encode:
                    match = face_recognition.compare_faces(self.known_face_encodes, face)
                    face_dist = face_recognition.face_distance(self.known_face_encodes, face)
                    match_index = np.argmin(face_dist)

                    if match[match_index]:
                        student = self.known_face_names[match_index]

                if not student["NIM"] in self.absent:
                    self.absent.append(str(student['NIM']))

                for top, right, bottom, left in cam_face_loc:
                    top, right, bottom, left = top*4, right*4, bottom*4, left*4
                    cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv.FILLED)
                    font = cv.FONT_HERSHEY_DUPLEX
                    cv.putText(frame, student["Name"], (left+6, bottom-6), font, 1.0, (255, 255, 255), 1)

                cv.imshow("PLEASE PRESS X TO TERMINATE THIS PAGE", frame)

                if cv.waitKey(1) & 0xFF == ord("x"):
                    msgbox = tkm.askquestion(parent=self.main_window, title="FACE CARD MANAGER", message=f"ARE YOU SURE WANT TO TERMINATE ABSENT PAGE? (CANNOT UNDO)")
                    if msgbox == "no":
                        pass
                    elif msgbox == "yes":
                        self.camera.release()
                        cv.destroyAllWindows()
                        break
            
            with open("../data/class_student.json", mode="r") as file:
                class_data = json.load(file)

            nimstudent = class_data[self.class_code]["Session"][self.date]

            for nim in self.absent:
                try:
                    nimstudent[nim]
                    class_data[self.class_code]["Session"][self.date][nim] = 1
                except:
                    continue

            class_data[self.class_code]["Session"][self.date]["Status"] = "COMPLETED"

            with open("../data/class_student.json", mode="w") as file:
                file.write(str(json.dumps(class_data, indent=4, sort_keys=True)))

            for widget in self.main_window.winfo_children():
                widget.destroy()
                
        except:
            pass
        
        from view_absent import ViewAbsent
        vap = ViewAbsent(self.main_window, self.class_code, self.date)
        vap.view_absent_page()

    def stream(self, student_credentials):
        p = "../data/student_image"
        self.known_face_encodes = []
        self.known_face_names = []

        for index in range(len(student_credentials)):
            path = f"{p}/{str(student_credentials[index]['NIM'])}.jpg"
            image = cv.imread(path)
            rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            face_loc = face_recognition.face_locations(rgb_image)
            face_encode = face_recognition.face_encodings(rgb_image, face_loc)
            
            for encoding in face_encode:
                self.known_face_encodes.append(encoding)
                self.known_face_names.append(student_credentials[index])

        self.cam_to_tk()

    def face_scanner_page(self):
        with open("../data/class_student.json", mode="r") as file:
            class_data = json.load(file)

        with open("../data/student.json", mode="r") as file:
            student_data = json.load(file)

        nim = class_data[self.class_code]["StudentNIM"]
        student_credentials = []

        for n in nim:
            data = {
                "NIM": str(n),
                "Name": str(student_data[str(n)]["Name"])
            }
            student_credentials.append(data)
        
        self.stream(student_credentials)