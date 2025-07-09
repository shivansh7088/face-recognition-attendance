from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from pathlib import Path

# Use the existing path logic from your file
base_dir = Path(__file__).resolve().parent
IMAGE_DIR = base_dir / "college_images"
# If the images are in 'Secure-Attend-main/fa/college_images' and this file is in 'Secure-Attend-main/fa'
# then the above path is correct.

class Help:
    def __init__(self, root):
        self.root = root
        
        # Make the window start maximized to fit the screen
        self.root.state('zoomed')
        self.root.title("Help Desk - Face Recognition System")

        # --- Modern UI Style Configuration ---
        BG_COLOR = "#F5F5F5"      # A soft, light gray for the background
        CARD_COLOR = "#FFFFFF"    # White for the content card
        TITLE_COLOR = "#2C3E50"   # A professional dark slate blue for the main title
        TEXT_COLOR = "#34495E"    # A slightly softer dark color for body text
        ACCENT_COLOR = "#3498DB"  # A nice blue for the email address to make it stand out

        TITLE_FONT = ("Segoe UI", 35, "bold")
        HEADER_FONT = ("Segoe UI", 22, "bold")
        BODY_FONT = ("Segoe UI", 16)
        
        # --- Main Background ---
        self.root.config(bg=BG_COLOR)

        # --- Top Title Label ---
        title_lbl = Label(self.root, text="Help Desk", font=TITLE_FONT, fg=TITLE_COLOR, bg=BG_COLOR)
        title_lbl.pack(pady=(20, 30))

        # --- Main Content Card (This is the central white box) ---
        # We use a container frame with place to easily center the card.
        container = Frame(self.root, bg=BG_COLOR)
        container.pack(fill=BOTH, expand=True)

        help_card = Frame(container, bg=CARD_COLOR, bd=2, relief=RIDGE)
        # Using place with relative coordinates is great for centering a main element.
        help_card.place(relx=0.5, rely=0.45, anchor=CENTER)

        # --- Image Banner inside the Card ---
        # Using the IMAGE_DIR variable instead of a hardcoded path
        try:
            img_top = Image.open(IMAGE_DIR / "helpPage1.jpeg")
            # Resized to be a banner, not a full-screen background
            img_top = img_top.resize((800, 300), Image.Resampling.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top)
            
            img_label = Label(help_card, image=self.photoimg_top, bg=CARD_COLOR)
            img_label.pack(pady=20, padx=20)
        except FileNotFoundError:
            # If the image is not found, show an error message instead of crashing
            img_label = Label(help_card, text="Image not found", font=BODY_FONT, bg=CARD_COLOR, fg="red")
            img_label.pack(pady=20, padx=20)


        # --- Text Section inside the Card ---
        # A header for the contact info
        contact_header_lbl = Label(help_card, text="Contact Information", font=HEADER_FONT, bg=CARD_COLOR, fg=TEXT_COLOR)
        contact_header_lbl.pack(pady=(10, 5))

        # Frame to hold the email labels on one line
        email_frame = Frame(help_card, bg=CARD_COLOR)
        email_frame.pack(pady=(5, 30))

        email_intro_lbl = Label(email_frame, text="For support, please email:", font=BODY_FONT, bg=CARD_COLOR, fg=TEXT_COLOR)
        email_intro_lbl.pack(side=LEFT, padx=(0, 5))

        email_address_lbl = Label(email_frame, text="shivanshdhakare70@gmail.com", font=BODY_FONT, bg=CARD_COLOR, fg=ACCENT_COLOR)
        email_address_lbl.pack(side=LEFT)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()