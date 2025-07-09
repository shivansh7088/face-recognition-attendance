# =====================================================================
#             COMPLETE AND CORRECTED train.py CODE
# =====================================================================

from cProfile import label
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import os
import cv2
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "college_images"

class Train:
    # constructor call
    def __init__(self, root):
        self.root = root
        # <<< FIX: Use 'zoomed' state for a responsive, full-screen window
        self.root.state('zoomed')
        self.root.title("Face Recognition System - Train Model")
        self.root.configure(bg="white")

        # <<< FIX: Using .pack() for a robust and responsive vertical layout
        
        # --- Title Label ---
        title_lbl = Label(self.root, text="TRAIN DATASET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.pack(side=TOP, fill=X, pady=(10, 20))

        # --- Top Image ---
        img_top = Image.open(IMAGE_DIR / "facialrecognition.png")
        # Resize based on a fraction of screen width to be responsive
        screen_width = self.root.winfo_screenwidth()
        img_width = int(screen_width * 0.9)
        img_height = int(img_width / 4.7) # Maintain aspect ratio
        img_top = img_top.resize((img_width, img_height), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        Label(self.root, image=self.photoimg_top).pack(side=TOP, pady=10)

        # --- Train Button ---
        # Make the button visually appealing and centered
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 20, "bold"), bg="blue", fg="white")
        b1_1.pack(side=TOP, pady=20, padx=50, ipady=10, fill=X)

        # <<< NEW: Added a status label for user feedback ---
        self.status_label = Label(self.root, text="Click the 'TRAIN DATA' button to start the training process.", font=("arial", 12, "italic"), bg="white", fg="black")
        self.status_label.pack(side=TOP, pady=5)

        # --- Bottom Image ---
        img_bottom = Image.open(IMAGE_DIR / "opencv_face_reco_more_data.jpg")
        img_bottom = img_bottom.resize((img_width, img_height), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        Label(self.root, image=self.photoimg_bottom).pack(side=TOP, pady=10)


    def train_classifier(self):
        # <<< ENHANCED: Added status updates using the new label
        self.status_label.config(text="[INFO] Reading image data... Please wait.", fg="blue")
        self.root.update_idletasks() # Force the GUI to update immediately

        data_dir = "photodata"
        classifier_save_path = os.path.join("classifier.xml") # Save in the main directory

        if not os.path.exists(data_dir) or not os.listdir(data_dir):
            messagebox.showerror("Error", "Dataset directory 'photodata' is empty or not found.", parent=self.root)
            self.status_label.config(text="[ERROR] Dataset directory not found or empty.", fg="red")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.jpg')]
        
        if not path:
            messagebox.showerror("Error", "No .jpg files found in the 'photodata' directory.", parent=self.root)
            self.status_label.config(text="[ERROR] No .jpg files found to train.", fg="red")
            return

        faces = []
        ids = []

        total_images = len(path)
        for i, image_path in enumerate(path):
            # Update status for each image being processed
            self.status_label.config(text=f"[INFO] Processing image {i+1}/{total_images}...", fg="blue")
            self.root.update_idletasks()

            try:
                img = Image.open(image_path).convert('L')  # Convert to grayscale
                imageNp = np.array(img, 'uint8')
                
                # Extract ID from filename (e.g., "1_10.jpg" -> ID is 1)
                filename = os.path.basename(image_path)
                id_str = filename.split('_')[0]
                id = int(id_str)

                faces.append(imageNp)
                ids.append(id)
            except (ValueError, IndexError) as e:
                print(f"Skipping file with invalid name format: {filename}. Error: {e}")
                continue
            except Exception as e:
                print(f"Error processing file {image_path}: {e}")
                continue

        if not ids or len(set(ids)) < 2:
            messagebox.showerror("Training Error", "Training requires at least two different people (IDs) in the dataset.", parent=self.root)
            self.status_label.config(text="[ERROR] Not enough different IDs to train. Need at least 2.", fg="red")
            return

        ids = np.array(ids)
        
        # --- Train the classifier ---
        self.status_label.config(text="[INFO] Training model on collected faces... This may take a moment.", fg="blue")
        self.root.update_idletasks()
        
        try:
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write(classifier_save_path)

            self.status_label.config(text=f"[SUCCESS] Training complete! Model saved to {classifier_save_path}", fg="green")
            messagebox.showinfo("Result", f"Training completed successfully!\nModel saved as {classifier_save_path}", parent=self.root)

        except cv2.error as e:
            self.status_label.config(text=f"[ERROR] OpenCV training error.", fg="red")
            messagebox.showerror("Training Error", f"An OpenCV error occurred during training: {e}", parent=self.root)
        except Exception as e:
            self.status_label.config(text=f"[ERROR] An unexpected error occurred.", fg="red")
            messagebox.showerror("Training Error", f"An unexpected error occurred: {e}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()