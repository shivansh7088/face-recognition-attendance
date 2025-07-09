from tkinter import * 
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "college_images"

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("New User Registration")
        self.root.state('zoomed')

        # --- Style Configuration ---
        self.font_title = ("Segoe UI", 24, "bold")
        self.font_label = ("Segoe UI", 12, "bold")
        self.font_entry = ("Segoe UI", 12)
        self.font_button = ("Segoe UI", 14, "bold")
        self.color_bg = "#F0F0F0"
        self.color_card = "#FFFFFF"
        self.color_text = "#333333"
        self.color_label = "#555555"
        self.color_button = "#27AE60" # Green for success
        self.color_button_hover = "#2ECC71"

        # --- Variables (Unchanged) ---
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_cnum = StringVar()
        self.var_email = StringVar()
        self.var_ssq = StringVar()
        self.var_sa = StringVar()
        self.var_pwd = StringVar()
        self.var_cpwd = StringVar()
        self.var_check = IntVar()

        # --- Background ---
        try:
            bg_img = Image.open(IMAGE_DIR / "registrationbg.jpg").resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(bg_img)
            Label(self.root, image=self.bg_photo).place(x=0, y=0, relwidth=1, relheight=1)
        except Exception:
            self.root.config(bg=self.color_bg)

        # --- Main Registration Card ---
        main_card = Frame(self.root, bg=self.color_card)
        main_card.place(relx=0.5, rely=0.5, anchor=CENTER, width=1100, height=650)

        # --- Left Side (Image) ---
        left_frame = Frame(main_card)
        left_frame.place(x=0, y=0, width=450, relheight=1)
        try:
            side_img = Image.open(IMAGE_DIR / "face_detector1.jpg").resize((450, 650), Image.Resampling.LANCZOS)
            self.side_photo = ImageTk.PhotoImage(side_img)
            Label(left_frame, image=self.side_photo).pack(fill=BOTH, expand=True)
        except Exception:
            left_frame.config(bg="#CCCCCC")

        # --- Right Side (Form) ---
        form_frame = Frame(main_card, bg=self.color_card)
        form_frame.place(x=450, y=0, relwidth=1, relheight=1, width=-450)

        Label(form_frame, text="Create an Account", font=self.font_title, bg=self.color_card, fg=self.color_text).pack(pady=(30, 20))

        # --- Form Fields in two columns ---
        fields_container = Frame(form_frame, bg=self.color_card)
        fields_container.pack(fill=X, padx=40)

        col1 = Frame(fields_container, bg=self.color_card)
        col1.pack(side=LEFT, fill=X, expand=True, padx=(0, 20))
        
        col2 = Frame(fields_container, bg=self.color_card)
        col2.pack(side=LEFT, fill=X, expand=True, padx=(20, 0))

        # Column 1
        self._create_entry(col1, "First Name:", self.var_fname)
        self._create_entry(col1, "Last Name:", self.var_lname)
        self._create_combobox(col1, "Security Question:", self.var_ssq, ["Select", "Your Date of Birth", "Your Nick Name", "Your Favorite Book"])
        self._create_entry(col1, "Security Answer:", self.var_sa)

        # Column 2
        self._create_entry(col2, "Contact No:", self.var_cnum)
        self._create_entry(col2, "Email Address:", self.var_email)
        self._create_entry(col2, "Password:", self.var_pwd, show="*")
        self._create_entry(col2, "Confirm Password:", self.var_cpwd, show="*")
        
        # --- Terms and Conditions ---
        check_frame = Frame(form_frame, bg=self.color_card)
        check_frame.pack(fill=X, padx=40, pady=15)
        Checkbutton(check_frame, variable=self.var_check, text="I Agree to the Terms & Conditions",
                    font=("Segoe UI", 10), bg=self.color_card, fg=self.color_label,
                    activebackground=self.color_card, activeforeground=self.color_text).pack(anchor=W)

        # --- Register Button ---
        reg_btn = Button(form_frame, command=self.reg, text="REGISTER NOW", font=self.font_button,
                         bd=0, bg=self.color_button, fg="white",
                         activebackground=self.color_button_hover, activeforeground="white", cursor="hand2")
        reg_btn.pack(fill=X, padx=40, ipady=10, pady=(0, 10))

        # --- Login Link ---
        login_link_frame = Frame(form_frame, bg=self.color_card)
        login_link_frame.pack(pady=10)
        Label(login_link_frame, text="Already have an account?", font=("Segoe UI", 10), bg=self.color_card, fg=self.color_label).pack(side=LEFT)
        Button(login_link_frame, text="Login Now", command=self.go_to_login, font=("Segoe UI", 10, "bold"),
               bd=0, bg=self.color_card, fg=self.color_button,
               activebackground=self.color_card, activeforeground=self.color_button_hover, cursor="hand2").pack(side=LEFT)

    def _create_entry(self, parent, label_text, var, show=None):
        """Helper to create a label and an entry."""
        Label(parent, text=label_text, font=self.font_label, bg=self.color_card, fg=self.color_label).pack(anchor=W)
        entry = ttk.Entry(parent, textvariable=var, font=self.font_entry, show=show)
        entry.pack(fill=X, pady=(5, 10), ipady=4)
        return entry

    def _create_combobox(self, parent, label_text, var, values):
        """Helper to create a label and a combobox."""
        Label(parent, text=label_text, font=self.font_label, bg=self.color_card, fg=self.color_label).pack(anchor=W)
        combo = ttk.Combobox(parent, textvariable=var, font=self.font_entry, state="readonly", values=values)
        combo.current(0)
        combo.pack(fill=X, pady=(5, 10), ipady=4)
        return combo

    def go_to_login(self):
        """Closes the registration window."""
        self.root.destroy()

    # ================= BACKEND FUNCTION (BILKUL BHI CHANGE NAHI KIYA GAYA) =================
    def reg(self):
        if (self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_cnum.get() == "" or self.var_email.get() == "" or self.var_ssq.get() == "Select" or self.var_sa.get() == "" or self.var_pwd.get() == "" or self.var_cpwd.get() == ""):
            messagebox.showerror("Error", "All Fields Required!", parent=self.root)
        elif (self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error", "Password & Confirm Password must be the same!", parent=self.root)
        elif (self.var_check.get() == 0):
            messagebox.showerror("Error", "Please agree to the Terms & Conditions!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='root', host='localhost', database='face_recognizer', port=3306)
                mycursor = conn.cursor()
                query = ("select * from regteach where email=%s")
                value = (self.var_email.get(),)
                mycursor.execute(query, value)
                row = mycursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User with this email already exists.", parent=self.root)
                else:
                    mycursor.execute("insert into regteach values(%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_cnum.get(),
                        self.var_email.get(),
                        self.var_ssq.get(),
                        self.var_sa.get(),
                        self.var_pwd.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Registered Successfully!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()