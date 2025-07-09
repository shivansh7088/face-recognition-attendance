# --- IMPORTS ---
from sys import path 
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
from pathlib import Path

# --- GLOBAL PATHS ---
BASE_DIR = Path(__file__).resolve().parent

class Face_Recognition:

    # ===================== UI SETUP (INIT METHOD) ===================
    # This is the new, modern, and responsive UI.
    def __init__(self, root):
        self.root = root
        
        # Make the window start maximized to fit the screen
        self.root.state('zoomed') 
        self.root.title("Face Recognition Panel")

        # --- Style Configuration ---
        BG_COLOR = "#F0F0F0"
        TITLE_COLOR = "#2C3E50"
        FRAME_BG_COLOR = "#FFFFFF"
        BUTTON_BG = "#3498DB"
        BUTTON_FG = "#FFFFFF"
        WHITE = "#FFFFFF" # Definition for WHITE color
        TITLE_FONT = ("Segoe UI", 28, "bold")
        BUTTON_FONT = ("Segoe UI", 15, "bold")
        
        IMAGE_DIR = BASE_DIR / "college_images"
        
        self.root.config(bg=BG_COLOR)
        
        # --- Title Label ---
        title_lbl = Label(self.root, text="Face Recognition System", font=TITLE_FONT, fg=TITLE_COLOR, bg=BG_COLOR)
        title_lbl.pack(pady=20)

        # --- Main Content Frame ---
        main_frame = Frame(self.root, bg=BG_COLOR)
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
        
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)

        # --- Left Image Frame ---
        left_frame = Frame(main_frame, bd=2, relief=RIDGE, bg=FRAME_BG_COLOR)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        left_frame.pack_propagate(False)

        img_left = Image.open(IMAGE_DIR / "face_detector1.jpg")
        img_left = img_left.resize((700, 650), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl_left = Label(left_frame, image=self.photoimg_left)
        f_lbl_left.pack(fill=BOTH, expand=True)

        # --- Right Section (Image and Button) ---
        right_frame = Frame(main_frame, bd=2, relief=RIDGE, bg=FRAME_BG_COLOR)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        
        img_right = Image.open(IMAGE_DIR / "face_detector2.jpg")
        img_right = img_right.resize((700, 500), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl_right = Label(right_frame, image=self.photoimg_right)
        f_lbl_right.pack(pady=20)

        # --- Single, Combined Button ---
        detect_button = Button(right_frame,
                               text="Scan Face to Mark Attendance",
                               command=self.face_recog,
                               font=BUTTON_FONT, cursor="hand2", bg=BUTTON_BG, fg=BUTTON_FG,
                               activebackground="#2980B9", activeforeground=WHITE,
                               relief=RAISED, bd=2, pady=15)
        detect_button.pack(padx=100, pady=(0, 40), fill=X)


    # ===================== Attendance ===================
    # YOUR ORIGINAL BACKEND CODE - UNCHANGED
    def mark_attendance(self, i, r, n):
        if not os.path.exists("Attendence.csv"):
            with open("Attendence.csv", "w", newline="\n") as f:
                f.write("ID,Roll,Name,Time,Date,Status\n")

        with open("Attendence.csv", "r+", newline="\n") as f:
            myDatalist = f.readlines()
            id_list = []
            for line in myDatalist:
                entry = line.strip().split(",")
                id_list.append(entry[0])

            if i not in id_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.write(f"{i},{r},{n},{dtString},{d1},Present\n")


    # ==================== Face recognition (Updated to close on 2nd Enter) ==================
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                if w > 0 and h > 0:
                    face_roi_gray = gray_image[y:y+h, x:x+w]
                    id, predict = clf.predict(face_roi_gray)
                    recognition_threshold = 65
                    conn = None
                    cursor = None
                    student_data = None
                    try:
                       conn = mysql.connector.connect(username='root', password='root', host='localhost', database='face_recognizer', port=3306)
                       cursor = conn.cursor()
                       cursor.execute("SELECT Student_ID, Name, Roll FROM student WHERE Student_ID = %s", (id,))
                       student_data = cursor.fetchone()
                    except mysql.connector.Error:
                       cv2.putText(img, "DB Error", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)
                       student_data = None
                    finally:
                       if cursor is not None:
                           cursor.close()
                       if conn is not None and conn.is_connected():
                           conn.close()
                    
                    if student_data is not None and predict < recognition_threshold:
                       s_id, name, roll = map(str, student_data)
                       attendance_id = s_id
                       attendance_roll = roll
                       attendance_name = name
                       cv2.putText(img, f"ID: {attendance_id}", (x, y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                       cv2.putText(img, f"Name: {attendance_name}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                       cv2.putText(img, f"Roll: {attendance_roll}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                       self.mark_attendance(attendance_id, attendance_roll, attendance_name)
                    else:
                       cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                       cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
            return img

        def recognize(img, clf, faceCascade):
             processed_img = draw_boundray(img, faceCascade, 1.1, 10, clf)
             return processed_img

        faceCascade_path = r"C:\Users\shiva\Documents\projects\project\Secure-Attend-main\fa\haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(faceCascade_path)
        if faceCascade.empty():
            messagebox.showerror("Error", "Could not load face detection model.", parent=self.root)
            return

        classifier_model_path = r"C:\Users\shiva\Documents\projects\project\Secure-Attend-main\fa\classifier.xml"
        clf = cv2.face.LBPHFaceRecognizer_create()
        if not os.path.exists(classifier_model_path):
            messagebox.showerror("Error", f"Face recognition model not found.\nPlease run Train.py first.", parent=self.root)
            return
        clf.read(classifier_model_path)

        videoCap = cv2.VideoCapture(0)
        if not videoCap.isOpened():
            messagebox.showerror("Error", "Could not open camera.", parent=self.root)
            return

        enter_press_count = 0 # Initialize a counter for Enter presses

        while True:
            ret, img = videoCap.read()
            if not ret or img is None:
                break
            
            processed_img = recognize(img, clf, faceCascade)
            
            # Add a message to the screen after the first press
            if enter_press_count == 1:
                height = processed_img.shape[0]
                cv2.putText(processed_img, "Press Enter again to close", (10, height - 20), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            
            cv2.imshow("Face Detector", processed_img)

            key = cv2.waitKey(1) & 0xFF

            # Check for Enter key press and update the counter
            if key == 13: # 13 is the Enter key
                enter_press_count += 1
                if enter_press_count >= 2: # If pressed twice, break
                    break
            
            # Allow 'Esc' key to close immediately as a failsafe
            if key == 27: # 27 is the Escape key
                break

        videoCap.release()
        cv2.destroyAllWindows()


# ===================== SCRIPT EXECUTION ===================
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()