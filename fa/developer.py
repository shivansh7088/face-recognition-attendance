from tkinter import *
from tkinter import ttk  
from PIL import Image, ImageTk
import os 
from pathlib import Path


class Developer:
    # --- Corrected constructor name from _init_ to __init__ ---
    def __init__(self, root):
        self.root = root
        
        BASE_DIR = Path(__file__).resolve().parent
        IMAGE_DIR = BASE_DIR / "college_images"
        # --- Make the window more responsive and centered ---
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 1280
        window_height = 720
        
        # Calculate position for centering the window
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
        self.root.title("About the Developer - Face Recognition System")
        self.root.configure(bg="#2c3e50") # A dark background for the root window

        # --- Main Title Label ---
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
        # NOTE: Make sure you have an 'assets' folder with 'developer_bg.jpg' inside.
        try:
            img_bg = Image.open(bg_image_path)
            img_bg = img_bg.resize((window_width, window_height - 50), Image.Resampling.LANCZOS)
            self.photoimg_bg = ImageTk.PhotoImage(img_bg)

            # Use a Label to hold the background image
            background_label = Label(self.root, image=self.photoimg_bg)
            background_label.pack(fill=BOTH, expand=True)

        except FileNotFoundError:
            # If the image is not found, show an error message on the label
            background_label = Label(self.root, text="Background Image Not Found\n(Place 'developer_bg.jpg' in 'assets' folder)", font=("Arial", 16))
            background_label.pack(fill=BOTH, expand=True)


        # --- Main Frame for the Developer Info Card (centered on the background) ---
        # Using pack with expand=True will center this frame.
        main_frame = ttk.Frame(background_label, style='Card.TFrame', padding=20)
        main_frame.place(relx=0.5, rely=0.5, anchor=CENTER) # A more robust centering method

        # Define a style for the card frame
        style = ttk.Style()
        style.configure('Card.TFrame', background='rgba(255, 255, 255, 0.9)', relief=RIDGE, borderwidth=2)


        # --- Developer Photo ---
        # NOTE: Make sure you have 'developer_photo.jpg' in the 'assets' folder.
        try:
            dev_photo_path = asset_path("developer_photo.jpg")
            img_dev = Image.open(dev_photo_path)
            img_dev = img_dev.resize((180, 180), Image.Resampling.LANCZOS)
            self.photoimg_dev = ImageTk.PhotoImage(img_dev)

            # Using a LabelFrame to give the photo a nice border and title
            photo_frame = ttk.LabelFrame(main_frame, text="Developer", style='Card.TFrame')
            photo_frame.pack(pady=(0, 20), padx=20)
            
            dev_photo_label = Label(photo_frame, image=self.photoimg_dev, borderwidth=0)
            dev_photo_label.pack(padx=5, pady=5)
        
        except FileNotFoundError:
            dev_photo_label = ttk.Label(main_frame, text="Dev Photo Not Found", font=("Arial", 12))
            dev_photo_label.pack(pady=(0, 20))


        # --- Developer Info Labels ---
        # Using .pack() for a clean, vertical, and responsive layout
        name_label = ttk.Label(
            main_frame,
            text="Urvashi Singh",
            font=("Segoe UI", 22, "bold"),
            style='Card.TLabel'
        )
        name_label.pack(pady=(0, 5))

        role_label = ttk.Label(
            main_frame,
            text="Aspiring Software Developer",
            font=("Segoe UI", 14, "italic"),
            style='Card.TLabel'
        )
        role_label.pack(pady=(0, 20))
        
        # --- A separator for better visual structure ---
        separator = ttk.Separator(main_frame, orient='horizontal')
        separator.pack(fill='x', padx=30, pady=10)

        # --- A brief description ---
        description_text = "I am a passionate developer with a focus on creating efficient and user-friendly applications using Python. This face recognition system is one of my key projects, showcasing skills in computer vision and GUI development."
        
        description_label = ttk.Label(
            main_frame,
            text=description_text,
            font=("Segoe UI", 11),
            wraplength=450,  # The text will wrap if it exceeds this width
            justify="center",
            style='Card.TLabel'
        )
        description_label.pack(pady=10, padx=20)
        
        # Style for labels inside the card
        style.configure('Card.TLabel', background=main_frame.cget('background'))


# --- Corrected main execution block ---
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()