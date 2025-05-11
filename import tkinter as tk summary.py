import tkinter as tk
from tkinter import messagebox
import customtkinter 

import cv2
import os
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Initialize the customtkinter root window


# Initialize the root window
root = customtkinter.CTk()
root.title("Experiment Program")
root.geometry("1000x530")
root.config(bg="#CAF0F8")

# Configure grid layout for responsiveness
root.grid_rowconfigure(0, weight=1)  # Header row
root.grid_rowconfigure(1, weight=4)  # Content row
root.grid_rowconfigure(2, weight=1) 
 

                                               # Footer row
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)




# Header Button


summary_label= customtkinter.CTkLabel(
    root,
    text="OBSERVATION",
    font=("Times New Roman", 35),
    fg_color="#0077B6",  # Background color
    text_color="white",
    width=15,
      # Text color
    #corner_radius=8,                           # Rounded corner radius
       # Button height

)

summary_label.grid(row=0, column=0,sticky= "w",pady=20, padx=20)  # Stretch horizontally





# Footer Buttons
previous_button = customtkinter.CTkButton(
    root,
    text="QUIT",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",  # Text color
    corner_radius=10
)
previous_button.grid(row=2, column=0, padx=20, sticky="w")


steps_label = customtkinter.CTkLabel(
    root,
    text="STEPS",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",
      # Text color
   # corner_radius=8,  
      width=20  # Rounded corner radius    # Button height

)
steps_label.grid(row=0, column=2, sticky= "e", padx=20 )

next_button = customtkinter.CTkButton(
    root,
    text="NEXT",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",  # Text color
    corner_radius=10,
    width=15        # Rounded corner radiu
)
next_button.grid(row=2, column=2, pady=10,sticky="e",padx=20)

quit_button = customtkinter.CTkButton(
    root,
    text="PREVIOUS",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",  # Text color
    corner_radius=10,
    width=15
)
quit_button.grid(row=2, column=2,padx=10)

# Run the Tkinter event loop
import cv2
import os
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Initialize the customtkinter root window


# Function to calculate similarity and highlight differences
def compare_images(image1_path, image2):
    # Read the saved image
    saved_image = cv2.imread(image1_path, cv2.IMREAD_COLOR)
    if saved_image is None:
        messagebox.showerror("Error", "Saved image not found.")
        return None, None, None, None

    # Resize the camera-captured image to match the saved image
    image2_resized = cv2.resize(image2, (saved_image.shape[1], saved_image.shape[0]))

    # Convert both images to grayscale
    gray1 = cv2.cvtColor(saved_image, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2_resized, cv2.COLOR_BGR2GRAY)

    # Compute SSIM (Structural Similarity Index)
    score, diff = compare_ssim(gray1, gray2, full=True)
    diff = (diff * 255).astype("uint8")

    # Threshold the difference image to find contours
    thresh = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around the differences
    result_image = saved_image.copy()
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(result_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    return score * 100, saved_image, image2_resized, result_image

# Function to capture an image from the camera and compare it
def capture_and_compare():
    # Open the camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not access the camera.")
        return

    # Capture a frame
    ret, frame = cap.read()
    cap.release()
    if not ret:
        messagebox.showerror("Error", "Failed to capture image.")
        return

    # Load the saved image path
    saved_image_path = filedialog.askopenfilename(
        title="Select the saved image to compare",
        filetypes=(("Image Files", "*.jpg;*.jpeg;*.png"), ("All Files", "*.*")),
    )
    if not saved_image_path:
        return

    # Compare the images and display results
    similarity, saved_image, captured_image, result_image = compare_images(saved_image_path, frame)
    if similarity is None:
        return

    # Convert images to Tkinter-compatible format
    saved_image_tk = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(saved_image, cv2.COLOR_BGR2RGB)))
    captured_image_tk = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(captured_image, cv2.COLOR_BGR2RGB)))
    result_image_tk = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)))

    # Display images in the GUI
    saved_image_label.configure(image=saved_image_tk)
    saved_image_label.image = saved_image_tk
    captured_image_label.configure(image=captured_image_tk)
    captured_image_label.image = captured_image_tk
    result_image_label.configure(image=result_image_tk)
    result_image_label.image = result_image_tk

    # Update similarity label
    similarity_label.configure(text=f"Similarity: {similarity:.2f}%")

# Layout for the interface
# Labels for displaying images
saved_image_label = ctk.CTkLabel(root, text="Saved Image")
saved_image_label.grid(row=0, column=0, padx=20, pady=20)

captured_image_label = ctk.CTkLabel(root, text="Captured Image")
captured_image_label.grid(row=0, column=1, padx=20, pady=20)

result_image_label = ctk.CTkLabel(root, text="Difference Highlighted")
result_image_label.grid(row=0, column=2, padx=20, pady=20)

# Button to capture and compare images
capture_button = ctk.CTkButton(
    root,
    text="Capture and Compare Images",
    font=("Arial", 16),
    fg_color="#0077B6",
    text_color="white",
    command=capture_and_compare
)
capture_button.grid(row=1, column=1, pady=20)

# Label to display similarity percentage
similarity_label = ctk.CTkLabel(root, text="Similarity: N/A", font=("Arial", 20), text_color="black")
similarity_label.grid(row=2, column=1, pady=20)

# Run the customtkinter event loop
root.mainloop()

