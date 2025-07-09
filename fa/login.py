import pathlib
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
from main import Face_Recoginition_System

# Aapke baaki imports
from train import Train
from student import Student
from attendence import Attendance
from developer import Developer
from help import Help

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Face Recognition System")
        self.root.state('zoomed')

        # --- Modern UI Style Configuration ---
        self.style_config = {
            "bg_color": "#212121",
            "card_color": "#2C2C2C",
            "text_color": "#FFFFFF",
            "placeholder_color": "#A0A0A0",
            "accent_color": "#0D94F5",
            "button_color": "#E53935",
            "button_hover_color": "#C62828",
            "title_font": ("Segoe UI", 24, "bold"),
            "body_font": ("Segoe UI", 12),
            "button_font": ("Segoe UI", 14, "bold"),
            "link_font": ("Segoe UI", 10, "underline")
        }

        BASE_DIR = pathlib.Path(__file__).resolve().parent
        IMAGE_DIR = BASE_DIR / "college_images"

        # --- Variables ---
        self.var_ssq = StringVar()
        self.var_sa = StringVar()
        self.var_pwd = StringVar()

        # --- Background ---
        self.root.config(bg=self.style_config["bg_color"])

        # --- Login Card ---
        # Card ko screen ke bahar se start karenge animation ke liye
        self.login_card = Frame(self.root, bg=self.style_config["card_color"], bd=1, relief=SOLID)
        self.login_card.place(relx=1.5, rely=0.5, anchor=CENTER, width=400, height=480)
        
        # --- Widgets ---
        self.setup_widgets(IMAGE_DIR)

        # --- TTK Widget Styling (for focus highlight) ---
        self.setup_styles()
        
        # --- Start Animation ---
        self.animate_card()

    def setup_widgets(self, IMAGE_DIR):
        """Helper function to create all widgets inside the card."""
        # Login Icon
        try:
            icon_img = Image.open(IMAGE_DIR / "LoginIconAppl.png").resize((80, 80), Image.Resampling.LANCZOS)
            self.icon_photo = ImageTk.PhotoImage(icon_img)
            Label(self.login_card, image=self.icon_photo, bg=self.style_config["card_color"]).pack(pady=(40, 10))
        except FileNotFoundError:
            pass

        Label(self.login_card, text="User Login", font=self.style_config["title_font"], fg=self.style_config["text_color"], bg=self.style_config["card_color"]).pack(pady=(0, 30))

        # --- Username Entry with Icon ---
        user_frame = Frame(self.login_card, bg=self.style_config["card_color"])
        user_frame.pack(pady=(5, 15), padx=40)
        try:
            user_icon = Image.open(IMAGE_DIR / "user_icon.png").resize((24, 24), Image.Resampling.LANCZOS)
            self.user_icon_photo = ImageTk.PhotoImage(user_icon)
            Label(user_frame, image=self.user_icon_photo, bg=self.style_config["card_color"]).pack(side=LEFT, padx=5)
        except: pass
        self.txtuser = ttk.Entry(user_frame, font=self.style_config["body_font"], width=30, style="Modern.TEntry")
        self.txtuser.pack(side=LEFT, ipady=5)
        self.add_placeholder(self.txtuser, "Enter Username")

        # --- Password Entry with Icon ---
        pwd_frame = Frame(self.login_card, bg=self.style_config["card_color"])
        pwd_frame.pack(pady=(5, 25), padx=40)
        try:
            pwd_icon = Image.open(IMAGE_DIR / "lock_icon.png").resize((24, 24), Image.Resampling.LANCZOS)
            self.pwd_icon_photo = ImageTk.PhotoImage(pwd_icon)
            Label(pwd_frame, image=self.pwd_icon_photo, bg=self.style_config["card_color"]).pack(side=LEFT, padx=5)
        except: pass
        self.txtpwd = ttk.Entry(pwd_frame, font=self.style_config["body_font"], width=30, style="Modern.TEntry")
        self.txtpwd.pack(side=LEFT, ipady=5)
        self.add_placeholder(self.txtpwd, "Enter Password", show_char=True)

        # Login Button
        loginbtn = Button(self.login_card, command=self.login, text="LOGIN", font=self.style_config["button_font"], bd=0, relief=FLAT,
                          fg="white", bg=self.style_config["button_color"], activeforeground="white",
                          activebackground=self.style_config["button_hover_color"], cursor="hand2")
        loginbtn.pack(fill=X, padx=40, ipady=10)

        # Links Frame
        links_frame = Frame(self.login_card, bg=self.style_config["card_color"])
        links_frame.pack(fill=X, padx=40, pady=20)
        Button(links_frame, command=self.reg, text="New User Register", font=self.style_config["link_font"], bd=0, fg=self.style_config["accent_color"], bg=self.style_config["card_color"], activeforeground="white", activebackground=self.style_config["card_color"], cursor="hand2").pack(side=LEFT)
        Button(links_frame, command=self.forget_pwd, text="Forget Password", font=self.style_config["link_font"], bd=0, fg=self.style_config["accent_color"], bg=self.style_config["card_color"], activeforeground="white", activebackground=self.style_config["card_color"], cursor="hand2").pack(side=RIGHT)

    def setup_styles(self):
        """Configure ttk styles for a modern look."""
        s = ttk.Style()
        s.configure("Modern.TEntry",
                    fieldbackground=self.style_config["card_color"],
                    foreground=self.style_config["text_color"],
                    bordercolor=self.style_config["text_color"],
                    insertcolor=self.style_config["text_color"],
                    borderwidth=2,
                    relief=FLAT)
        s.map("Modern.TEntry",
              bordercolor=[('focus', self.style_config["accent_color"])],
              relief=[('focus', 'solid')])
    
    def add_placeholder(self, entry, placeholder, show_char=False):
        """Adds placeholder functionality to a an entry widget."""
        entry.insert(0, placeholder)
        entry.config(foreground=self.style_config["placeholder_color"])
        entry.original_show = entry.cget("show") if show_char else ""
        
        def on_focus_in(event):
            if entry.get() == placeholder:
                entry.delete(0, "end")
                entry.config(show=entry.original_show, foreground=self.style_config["text_color"])
        
        def on_focus_out(event):
            if not entry.get():
                entry.config(show="", foreground=self.style_config["placeholder_color"])
                entry.insert(0, placeholder)

        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)

    def animate_card(self, current_x=1.5, target_x=0.5, step=0.03):
        """Animates the card sliding into view."""
        if current_x > target_x:
            current_x -= step
            self.login_card.place(relx=current_x, rely=0.5, anchor=CENTER)
            self.root.after(10, self.animate_card, current_x, target_x, step)
        else:
            self.login_card.place(relx=target_x, rely=0.5, anchor=CENTER)

    # ================= BACKEND FUNCTIONS (BILKUL BHI CHANGE NAHI KIYA GAYA) =================
    
    def reg(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        # Placeholder check
        user = self.txtuser.get() if self.txtuser.cget('foreground') == self.style_config['text_color'] else ""
        pwd = self.txtpwd.get() if self.txtpwd.cget('foreground') == self.style_config['text_color'] else ""

        if (user == "" or pwd == ""):
            messagebox.showerror("Error", "All Fields Required!")
        elif (user == "admin" and pwd == "admin"):
            messagebox.showinfo("Successfully", "Welcome to Attendance Management System")
            self.new_window = Toplevel(self.root)
            self.app = Face_Recoginition_System(self.new_window)
            self.root.withdraw()
        else:
            conn = mysql.connector.connect(username='root', password='root', host='localhost', database='face_recognizer', port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where email=%s and pwd=%s", (user, pwd))
            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Username or Password!")
            else:
                open_min = messagebox.askyesno("YesNo", "Access only Admin")
                if open_min:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recoginition_System(self.new_window)
                    self.root.withdraw()
            conn.commit()
            conn.close()

    def reset_pass(self):
        if self.var_ssq.get() == "Select":
            messagebox.showerror("Error", "Select the Security Question!", parent=self.root2)
        elif self.var_sa.get() == "":
            messagebox.showerror("Error", "Please Enter the Answer!", parent=self.root2)
        elif self.var_pwd.get() == "":
            messagebox.showerror("Error", "Please Enter the New Password!", parent=self.root2)
        else:
            conn = mysql.connector.connect(username='root', password='root', host='localhost', database='face_recognizer', port=3306)
            mycursor = conn.cursor()
            query = "select * from regteach where email=%s and ss_que=%s and s_ans=%s"
            value = (self.txtuser.get() if self.txtuser.cget('foreground') == self.style_config['text_color'] else "", self.var_ssq.get(), self.var_sa.get())
            mycursor.execute(query, value)
            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Incorrect Answer!", parent=self.root2)
            else:
                query = "update regteach set pwd=%s where email=%s"
                value = (self.var_pwd.get(), self.txtuser.get() if self.txtuser.cget('foreground') == self.style_config['text_color'] else "")
                mycursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Password reset successfully!", parent=self.root2)
                self.root2.destroy()

    def forget_pwd(self):
        user_email = self.txtuser.get() if self.txtuser.cget('foreground') == self.style_config['text_color'] else ""
        if user_email == "":
            messagebox.showerror("Error", "Please enter your Email address first!")
            return
        
        self.root2 = Toplevel()
        # (Forget Password window ka UI bhi attractive banaya ja sakta hai, lekin abhi ke liye functional rakhte hain)
        self.root2.title("Forget Password")
        self.root2.geometry("400x400+610+170")
        self.root2.configure(bg=self.style_config["card_color"])
        Label(self.root2, text="Forget Password", font=self.style_config["title_font"], fg=self.style_config["text_color"], bg=self.style_config["card_color"]).pack(pady=20)
        # (Yahan ke baaki widgets bhi style kiye ja sakte hain, for consistency)
        ssq = Label(self.root2, text="Select Security Question:", font=self.style_config["body_font"], fg=self.style_config["text_color"], bg=self.style_config["card_color"]).pack(pady=5)
        self.combo_security = ttk.Combobox(self.root2, textvariable=self.var_ssq, font=self.style_config["body_font"], state="readonly")
        self.combo_security["values"] = ("Select", "Your Date of Birth", "Your Nick Name", "Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.pack(pady=5, padx=20, fill=X)
        # ... baaki backend logic ...
        sa_label = Label(self.root2, text="Security Answer:", font=self.style_config["body_font"], fg=self.style_config["text_color"], bg=self.style_config["card_color"]).pack(pady=5)
        self.txt_sec_ans = ttk.Entry(self.root2, textvariable=self.var_sa, font=self.style_config["body_font"]).pack(pady=5, padx=20, fill=X)
        new_pwd_label = Label(self.root2, text="New Password:", font=self.style_config["body_font"], fg=self.style_config["text_color"], bg=self.style_config["card_color"]).pack(pady=5)
        self.new_pwd_entry = ttk.Entry(self.root2, textvariable=self.var_pwd, show="*", font=self.style_config["body_font"]).pack(pady=5, padx=20, fill=X)
        reset_btn = Button(self.root2, command=self.reset_pass, text="Reset Password", font=self.style_config["button_font"], bd=0, relief=FLAT, fg="white", bg=self.style_config["button_color"], activeforeground="white", activebackground=self.style_config["button_hover_color"], cursor="hand2").pack(pady=20, padx=20, fill=X, ipady=5)

if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()