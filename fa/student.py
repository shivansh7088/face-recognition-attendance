# =====================================================================
#             FINAL CORRECTED CODE (ROBUST LAYOUT)
# =====================================================================

from cProfile import label
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
from pathlib import Path

class Student:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title("Face Recognition System")

        # --- Variables (No changes) ---
        BASE_DIR = Path(__file__).resolve().parent
        IMAGE_DIR = BASE_DIR / "college_images"
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()
        self.var_searchTX = StringVar()
        self.var_search = StringVar()

        # --- Header Frame ---
        header_frame = Frame(self.root, bg="white", height=130)
        header_frame.pack(side=TOP, fill=X)
        header_frame.pack_propagate(False)

        img = Image.open(IMAGE_DIR / "Student3.jpg").resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        Label(header_frame, image=self.photoimg).pack(side=LEFT, expand=True, fill=BOTH)

        img1 = Image.open(IMAGE_DIR / "Studeent2.jpeg").resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(header_frame, image=self.photoimg1).pack(side=LEFT, expand=True, fill=BOTH)

        img2 = Image.open(IMAGE_DIR / "smart-attendance.jpg").resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Label(header_frame, image=self.photoimg2).pack(side=LEFT, expand=True, fill=BOTH)

        # --- Background and Main Content Area ---
        img3 = Image.open(IMAGE_DIR / "wp2551980.jpg").resize((1920, 1080), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.pack(side=TOP, expand=True, fill=BOTH)

        title_lbl = Label(bg_img, text="STUDENT DETAIL PANEL", font=("times new roman", 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=0, y=0, relwidth=1, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(relx=0.01, rely=0.07, relwidth=0.98, relheight=0.92)

        # --- Left and Right Frames (Equal Size) ---
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(relx=0.005, rely=0.01, relwidth=0.49, relheight=0.98)

        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(relx=0.505, rely=0.01, relwidth=0.49, relheight=0.98)

        # =================================================================
        #          <<< NEW, ROBUST LAYOUT FIX FOR LEFT FRAME >>>
        # =================================================================
        
        # --- TOP BLOCK (Image and Course Info) ---
        top_info_frame = Frame(Left_frame, bg="white")
        top_info_frame.pack(side=TOP, fill=X, padx=5, pady=5)

        img_left = Image.open(IMAGE_DIR / "smart-attendance.jpg").resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(top_info_frame, image=self.photoimg_left).pack(fill=X)

        current_course_frame = LabelFrame(top_info_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.pack(fill=X, pady=(5,0))
        # (Grid inside here is fine, it's a new parent)
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly", width=17)
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=17)
        course_combo["values"]=("Select Course","BTech","BCA","MBA","BBA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year","2024-25","2025-26","2026-27","2027-28")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=17)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # --- BOTTOM BLOCK (All Buttons) ---
        # Pack this to the BOTTOM first, so it's always anchored there.
        bottom_button_container = Frame(Left_frame, bg="white")
        bottom_button_container.pack(side=BOTTOM, fill=X, padx=5, pady=5)
        
        btn_frame1 = Frame(bottom_button_container, bd=2, relief=RIDGE)
        btn_frame1.pack(fill=X, pady=2)
        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Take Photo Sample", height=1, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.pack(expand=True, fill=BOTH)
        
        btn_frame = Frame(bottom_button_container, bd=2, relief=RIDGE)
        btn_frame.pack(fill=X, pady=2)
        save_btn = Button(btn_frame, text="Save", command=self.add_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.pack(side=LEFT, expand=True, fill=X)
        update_btn = Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.pack(side=LEFT, expand=True, fill=X)
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.pack(side=LEFT, expand=True, fill=X)
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.pack(side=LEFT, expand=True, fill=X)

        radion_frame = Frame(bottom_button_container, bg="white")
        radion_frame.pack(fill=X, pady=2)
        radionbtn1 = ttk.Radiobutton(radion_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radionbtn1.pack(side=LEFT, padx=30)
        radionbtn2 = ttk.Radiobutton(radion_frame, variable=self.var_radio1, text="No Photo Sample", value="NO")
        radionbtn2.pack(side=LEFT, padx=30)

        # --- MIDDLE BLOCK (Student Info) ---
        # This is packed last and will fill all the remaining space.
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_Student_frame.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        # Grid layout for student entry fields (This is correct)
        studentID_label = Label(class_Student_frame, text="StudentID:", font=("times new roman", 12, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        studentID_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        studentName_label = Label(class_Student_frame, text="Student Name:", font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        studentName_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        class_div_label = Label(class_Student_frame, text="Student Div:", font=("times new roman", 12, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        div_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_div, font=("times new roman", 12, "bold"), state="readonly", width=18)
        div_combo["values"] = ("A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        roll_no_label = Label(class_Student_frame, text="Roll NO:", font=("times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        roll_no_entry = ttk.Entry(class_Student_frame, textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        gender_label = Label(class_Student_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        gender_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Male", "Female", "other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        dob_label = Label(class_Student_frame, text="DOB:", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        dob_entry = ttk.Entry(class_Student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        email_label = Label(class_Student_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        email_entry = ttk.Entry(class_Student_frame, textvariable=self.var_email, width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        phone_label = Label(class_Student_frame, text="Phone No:", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        phone_entry = ttk.Entry(class_Student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)
        address_label = Label(class_Student_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        address_entry = ttk.Entry(class_Student_frame, textvariable=self.var_address, width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        teacher_label = Label(class_Student_frame, text="Teacher Name:", font=("times new roman", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        teacher_entry = ttk.Entry(class_Student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # =================================================================
        #                   CONTENT OF RIGHT FRAME (Layout corrected)
        # =================================================================
        img_right = Image.open(IMAGE_DIR / "studentb.jpg").resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        Label(Right_frame, image=self.photoimg_right).pack(side=TOP, fill=X, padx=5, pady=5)

        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.pack(side=TOP, fill=X, padx=5, pady=5)

        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="green", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        search_combo = ttk.Combobox(Search_frame, textvariable=self.var_searchTX, font=("times new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll_No", "Student_id")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)
        search_entry = ttk.Entry(Search_frame, textvariable=self.var_search, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        search_btn = Button(Search_frame, command=self.search_data, text="Search", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)
        showAll_btn = Button(Search_frame, command=self.fetch_data, text="Show All", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=("Dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Sample")
        self.student_table["show"] = "headings"

        for col in self.student_table["columns"]:
            self.student_table.column(col, width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    # =================================================================
    #          ALL FUNCTIONS BELOW ARE UNCHANGED
    # =================================================================

    def add_data(self):
        if (self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or
            self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or
            self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or
            self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or
            self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or
            self.var_teacher.get()==""):
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="Face_recognizer",port=3306)
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                    self.var_std_id.get(), self.var_std_name.get(), self.var_div.get(), self.var_roll.get(),
                    self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(),
                    self.var_address.get(), self.var_teacher.get(), self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def fetch_data(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="root",database="Face_recognizer",port=3306)
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            data=my_cursor.fetchall()
            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
            conn.commit()
            conn.close()
        except Exception as es:
            print(f"Database Connection Error: {es}")

    def get_cursor(self,event=""):
        try:
            cursor_focus=self.student_table.focus()
            content=self.student_table.item(cursor_focus)
            if not content.get("values"): return
            data=content["values"]
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.var_std_id.set(data[4])
            self.var_std_name.set(data[5])
            self.var_div.set(data[6])
            self.var_roll.set(data[7])
            self.var_gender.set(data[8])
            self.var_dob.set(data[9])
            self.var_email.set(data[10])
            self.var_phone.set(data[11])
            self.var_address.set(data[12])
            self.var_teacher.set(data[13])
            self.var_radio1.set(data[14])
        except (IndexError, TclError):
            print("Could not get cursor values. Table might be empty or has a different structure.")

    def update_data(self):
        if (self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()==""):
            messagebox.showerror("Error","Student Name and ID are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student detail",parent=self.root)
                if Update:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="Face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s ,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(),
                        self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(),
                        self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(),
                        self.var_teacher.get(), self.var_radio1.get(), self.var_std_id.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Students details successfully updated",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete","Do you want to delete this student",parent=self.root)
                if delete:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="Face_recognizer",port=3306)
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete","Successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("A")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("NO")

    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select a search option and enter text",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root',host='localhost',database='face_recognizer',port=3306)
                my_cursor = conn.cursor()
                query = "SELECT * FROM student where " + str(self.var_searchTX.get()) + " LIKE '%" + str(self.var_search.get()) + "%'"
                my_cursor.execute(query)
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                else:
                    messagebox.showinfo("Not Found","No data matching your search was found.",parent=self.root)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # =====================================================================
# <<< REPLACE your old generate_dataset function with these TWO new ones
# =====================================================================

    def generate_dataset(self):
        # --- Pre-capture Checks ---
        if (self.var_dep.get() == "Select Department" or self.var_std_id.get() == ""):
            messagebox.showerror("Error", "All fields are required, especially Student ID.", parent=self.root)
            return
        if self.var_radio1.get() == "NO":
            messagebox.showinfo("Information", "Photo Sample status is 'NO'. Please change to 'Yes' to capture photos.", parent=self.root)
            return

        # --- Setup for Capturing ---
        try:
            # Load the classifier ONCE
            cascade_path = "haarcascade_frontalface_default.xml"
            if not os.path.exists(cascade_path):
                # Try to find it in the same directory as the script
                script_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "haarcascade_frontalface_default.xml")
                if os.path.exists(script_dir_path):
                    cascade_path = script_dir_path
                else:
                    messagebox.showerror("Error", "Could not find haarcascade_frontalface_default.xml.", parent=self.root)
                    return
            
            self.face_classifier = cv2.CascadeClassifier(cascade_path)

            # Open the camera
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                messagebox.showerror("Error", "Could not open camera.", parent=self.root)
                return

            self.img_id = 0
            self.student_id = self.var_std_id.get()
            self.photo_dir = "photodata"
            if not os.path.exists(self.photo_dir):
                os.makedirs(self.photo_dir)

            # Start the capture loop using Tkinter's .after() method
            self._capture_frame()

        except Exception as es:
            messagebox.showerror("Error", f"An error occurred during setup: {str(es)}", parent=self.root)


    def _capture_frame(self):
        """Captures a single frame, processes it, and schedules the next frame capture."""
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to grab frame")
            return

        # --- Face Detection and Cropping ---
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_classifier.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            # Draw a rectangle around the face on the original frame
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            # Save the cropped face
            if self.img_id < 100:
                self.img_id += 1
                cropped_face = gray[y:y+h, x:x+w]
                face_resized = cv2.resize(cropped_face, (450, 450))
                
                img_name = f"{self.student_id}_{self.img_id}.jpg"
                img_path = os.path.join(self.photo_dir, img_name)
                cv2.imwrite(img_path, face_resized)
            break # Only process the first face found

        # --- Update and Display the Frame ---
        cv2.putText(frame, f"Images Captured: {self.img_id}", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Capturing Faces...", frame)

        # --- Loop or Stop Condition ---
        if self.img_id >= 100:
            self.cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Complete", f"Dataset generation completed. {self.img_id} images saved.", parent=self.root)
        else:
            # Schedule the next frame capture in 15ms
            self.root.after(15, self._capture_frame)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()