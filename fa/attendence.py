from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from pathlib import Path

class Developer:
    def __init__(self, root):
        self.root = root

        # --- Setup File Paths using pathlib ---
        BASE_DIR = Path(__file__).resolve().parent
        self.IMAGE_DIR = BASE_DIR / "college_images"
        
        # --- Window Configuration ---
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 1280
        window_height = 720
        
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        self.root.title("About the Developer - Face Recognition System")
        self.root.configure(bg="#2c3e50")

        # --- Title Label ---
        title_lbl = ttk.Label(
            self.root, 
            text="ABOUT THE DEVELOPER", 
            font=("Segoe UI", 28, "bold"), 
            background="#34495e", 
            foreground="white",
            anchor="center"
        )
        title_lbl.pack(side=TOP, fill=X, pady=(0, 10))

        # --- Background Image ---
        try:
            bg_image_path = self.IMAGE_DIR / "developer1.jpg"
            img_bg = Image.open(bg_image_path)
            img_bg = img_bg.resize((window_width, window_height), Image.Resampling.LANCZOS)
            self.photoimg_bg = ImageTk.PhotoImage(img_bg)
            background_label = Label(self.root, image=self.photoimg_bg)
            background_label.pack(fill=BOTH, expand=True)
        except FileNotFoundError:
            background_label = Label(self.root, text="Background Image Not Found\n(Place 'developer1.jpg' in 'college_images' folder)", font=("Arial", 16))
            background_label.pack(fill=BOTH, expand=True)

        # --- Developer Info Card ---
        style = ttk.Style()
        style.configure('Card.TFrame', background='white', relief=RIDGE, borderwidth=2)
        
        main_frame = ttk.Frame(background_label, style='Card.TFrame', padding=25)
        main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # --- Developer Photo ---
        try:
            dev_photo_path = self.IMAGE_DIR / "shivansh.jpg"
            img_dev = Image.open(dev_photo_path)
            img_dev = img_dev.resize((180, 180), Image.Resampling.LANCZOS)
            self.photoimg_dev = ImageTk.PhotoImage(img_dev)

            photo_frame = ttk.LabelFrame(main_frame, text="Developer", style='Card.TFrame')
            photo_frame.pack(pady=(0, 20), padx=20)
            
            dev_photo_label = Label(photo_frame, image=self.photoimg_dev, borderwidth=0)
            dev_photo_label.pack(padx=5, pady=5)
        except FileNotFoundError:
            dev_photo_label = ttk.Label(main_frame, text="Developer Photo Not Found\n(Place 'shivansh' in 'college_images' folder)", font=("Arial", 12))
            dev_photo_label.pack(pady=(0, 20))

        # --- Developer Information Text ---
        style.configure('Card.TLabel', background='white')

        name_label = ttk.Label(
            main_frame,
            text="Shiavansh Dhakare",
            font=("Segoe UI", 22, "bold"),
            style='Card.TLabel'
        )
        name_label.pack(pady=(0, 5))

        role_label = ttk.Label(
            main_frame,
            text="Software Developer",
            font=("Segoe UI", 14, "italic"),
            style='Card.TLabel'
        )
        role_label.pack(pady=(0, 20))
        
        separator = ttk.Separator(main_frame, orient='horizontal')
        separator.pack(fill='x', padx=30, pady=10)

        description_text = "I am a Software developer focused on building intuitive and efficient software solutions. This project showcases my skills in GUI development with Tkinter and computer vision."
        
        description_label = ttk.Label(
            main_frame,
            text=description_text,
            font=("Segoe UI", 11),
            wraplength=450,
            justify="center",
            style='Card.TLabel'
        )
        description_label.pack(pady=10, padx=20)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()