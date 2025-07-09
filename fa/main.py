from tkinter import *
from tkinter import messagebox, ttk
from time import strftime
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageTk
import os
import tkinter

# Importing other project files
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendance
from developer import Developer
from help import Help

class Face_Recoginition_System:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title("Face Recognition Attendance System - Main Dashboard")

        # --- Modern UI Style Configuration ---
        self.font_title = ("Segoe UI", 30, "bold")
        self.font_clock = ("Segoe UI", 14, "bold")
        self.font_button_text = ("Segoe UI", 14, "bold")
        
        self.color_bg = "#2C3E50"
        self.color_title_fg = "#FFFFFF"
        self.color_button_bg = "#EAEAEA"
        self.color_button_fg = "#2C3E50"
        self.color_button_hover = "#FFFFFF"
        self.color_hover_highlight = "#3498DB"

        BASE_DIR = Path(__file__).resolve().parent
        IMAGE_DIR = BASE_DIR / "college_images"
        
        # --- Background Image ---
        try:
            screen_w, screen_h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
            bg_img_pil = Image.open(IMAGE_DIR / "wp2551980.jpg").resize((screen_w, screen_h), Image.Resampling.LANCZOS)
            self.bg_photoimg = ImageTk.PhotoImage(bg_img_pil)
            bg_label = Label(self.root, image=self.bg_photoimg)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            self.root.config(bg=self.color_bg)
            print(f"Error loading background image: {e}")

        # --- Header with three images ---
        header_frame = Frame(self.root, bg="#FFFFFF", bd=1, relief=SOLID)
        # Using pack for robust top-to-bottom layout
        header_frame.pack(side=TOP, fill=X)
        self._create_header_image(header_frame, IMAGE_DIR / "Stanford.jpg").pack(side=LEFT, fill=BOTH, expand=True)
        self._create_header_image(header_frame, IMAGE_DIR / "facialrecognition.png").pack(side=LEFT, fill=BOTH, expand=True)
        self._create_header_image(header_frame, IMAGE_DIR / "u.jpg").pack(side=LEFT, fill=BOTH, expand=True)

        # --- Title Bar ---
        title_frame = Frame(self.root, bg="#34495E")
        # --- FIX: Using pack instead of place to prevent overlap ---
        title_frame.pack(pady=0 ,padx=60, fill=X)
        
        title_lbl = Label(title_frame, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=self.font_title, fg=self.color_title_fg, bg=title_frame['bg'])
        title_lbl.pack(side=LEFT, padx=140, pady=15)

        # --- Clock ---
        self.clock_lbl = Label(title_frame, font=self.font_clock, fg="#FFFFFF", bg=title_frame['bg'])
        self.clock_lbl.pack(side=RIGHT, padx=20, pady=10)
        self.update_time()

        # --- Main Dashboard Buttons Frame ---
        dashboard_frame = Frame(self.root, bg="#FFFFFF")
        # --- FIX: Using pack with expand=True for proper centering and no overlap ---
        dashboard_frame.pack(pady=2, padx=10, expand=True )

        # Button data: (image_file, text, command)
        buttons_data = [
            ("studentb.jpg", "Student Details", self.student_details),
            ("face_detector1.jpg", "Face Detector", self.face_data),
            ("report.jpg", "Attendance", self.attendence_data),
            ("helpDesk.jpg", "Help Desk", self.Help_data),
            ("Train.jpg", "Train Data", self.train_data),
            ("opencv_face_reco_more_data.jpg", "Photos", self.open_img),
            ("Team-Management-Software-Development.jpg", "Developer", self.Developer_data),
            ("exit.jpg", "Exit", self.Exit)
        ]

        # Create and place buttons in a 4x2 grid
        for i, data in enumerate(buttons_data):
            row, col = divmod(i, 4)
            img_path = IMAGE_DIR / data[0]
            button = self._create_dashboard_button(dashboard_frame, img_path, data[1], data[2])
            button.grid(row=row, column=col, padx=25, pady=5)

    def _create_header_image(self, parent, path):
        """Helper to create and pack header images."""
        try:
            img = Image.open(path).resize((500, 130), Image.Resampling.LANCZOS)
            photo_img = ImageTk.PhotoImage(img)
            label = Label(parent, image=photo_img, bg="#FFFFFF")
            label.image = photo_img
            return label
        except Exception:
            return Label(parent, text=f"Img not found", bg="#FFFFFF")
    
    def _create_dashboard_button(self, parent, image_path, text, command):
        """Creates a modern, styled button with image and text."""
        try:
            img = Image.open(image_path).resize((180, 180), Image.Resampling.LANCZOS)
            photo_img = ImageTk.PhotoImage(img)
        except Exception:
            photo_img = None

        # Change the button background to the parent's background for a "flat" look
        button = Button(parent, text=text, command=command, image=photo_img,
                        compound=TOP, font=self.font_button_text,
                        bg=parent.cget("bg"), fg=self.color_button_fg,
                        relief=FLAT, bd=0, cursor="hand2",  # bd=0 and relief=FLAT makes it look cleaner
                        activebackground=self.color_button_hover, activeforeground=self.color_button_fg,
                        pady=10)
        button.image = photo_img

        # A cleaner hover effect for flat buttons
        button.bind("<Enter>", lambda e: e.widget.config(bg=self.color_button_hover))
        button.bind("<Leave>", lambda e: e.widget.config(bg=parent.cget("bg")))

        return button

    def update_time(self):
        """Updates the clock every second."""
        string = strftime('%I:%M:%S %p')
        self.clock_lbl.config(text=string)
        self.clock_lbl.after(1000, self.update_time)

    # ================= BACKEND FUNCTIONS (UNCHANGED) =================
    
    def open_img(self):
        f_path = r"C:\Users\shiva\Documents\projects\project\Secure-Attend-main\photodata"
        if os.path.exists(f_path) and os.path.isdir(f_path):
            try:
                os.startfile(f_path)
            except Exception as e:
                messagebox.showerror("Error", f"Could not open the directory: {e}", parent=self.root)
        else:
            messagebox.showerror("Error", "Directory 'photodata' does not exist.", parent=self.root)

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
    
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendence_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
    
    def Developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)
    
    def Help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)
  
    def Exit(self):
        should_exit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit?", parent=self.root)
        if should_exit:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recoginition_System(root)
    root.mainloop()