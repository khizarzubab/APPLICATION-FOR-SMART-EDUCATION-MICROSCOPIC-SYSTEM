import tkinter as tk
from tkinter import messagebox, filedialog
import cv2
from PIL import Image, ImageTk
import os
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim


def start_camera():
    global cap
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera
    if not cap.isOpened():
        messagebox.showerror("Error", "Cannot access the camera")
        return
    update_frame()


def capture_image():
    global captured_image_path, captured_image
    if cap and cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # Save the captured image
            captured_image_path = "captured_image.jpg"
            cv2.imwrite(captured_image_path, frame)
            messagebox.showinfo("Success", f"Image saved as {captured_image_path}")
            show_captured_image(captured_image_path)
        else:
            messagebox.showerror("Error", "Failed to capture image")
    else:
        messagebox.showerror("Error", "Camera not running")


def show_captured_image(image_path):
    """Display the captured image in the GUI."""
    img = Image.open(image_path)
    img = img.resize((320, 240))  # Resize for display
    img_tk = ImageTk.PhotoImage(img)
    captured_image_label.img_tk = img_tk
    captured_image_label.config(image=img_tk)


def compare_with_folder_image():
    """Compare captured image with an image in a folder."""
    if not captured_image_path:
        messagebox.showerror("Error", "No captured image to compare")
        return

    file_path = filedialog.askopenfilename(title="Select Image to Compare", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if not file_path:
        return

    # Load the images
    captured_img = cv2.imread(captured_image_path, cv2.IMREAD_GRAYSCALE)
    folder_img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

    if captured_img is None or folder_img is None:
        messagebox.showerror("Error", "Failed to load one or both images")
        return

    # Resize the images to the same size
    captured_img = cv2.resize(captured_img, (320, 240))
    folder_img = cv2.resize(folder_img, (320, 240))

    # Compute Structural Similarity Index (SSIM)
    score, _ = compare_ssim(captured_img, folder_img, full=True)
    messagebox.showinfo("Comparison Result", f"Similarity Score: {score:.2f}")


def update_frame():
    """Update video frames in the Tkinter interface."""
    if cap and cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # Convert the frame to RGB for Tkinter
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (440, 480))
            img = Image.fromarray(frame)
            img_tk = ImageTk.PhotoImage(image=img)
            video_label.img_tk = img_tk
            video_label.config(image=img_tk)
        video_label.after(10, update_frame)  # Update frame every 10ms


def stop_camera():
    if cap and cap.isOpened():
        cap.release()
        video_label.config(image="")  # Clear the video frame
        messagebox.showinfo("Info", "Camera stopped")


# Create the main window
root = tk.Tk()
root.title("Camera Capture with Comparison")
root.geometry("1000x530")
root.resizable(True, True)

captured_image_path = None

# Video display label
video_label = tk.Label(root, bg="black")
video_label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Captured image display label
captured_image_label = tk.Label(root, text="Captured Image will appear here", bg="#d3d3d3", relief="solid")
captured_image_label.pack(padx=10, pady=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

start_button = tk.Button(btn_frame, text="Start Camera", font=("Arial", 14), bg="#0077B6", fg="white", command=start_camera)
start_button.grid(row=0, column=1, padx=5, pady=5)

capture_button = tk.Button(btn_frame, text="Capture Image", font=("Arial", 14), bg="#00B4D8", fg="white", command=capture_image)
capture_button.grid(row=0, column=2, padx=5, pady=5)

compare_button = tk.Button(btn_frame, text="Compare Image", font=("Arial", 14), bg="#0077B6", fg="white", command=compare_with_folder_image)
compare_button.grid(row=0, column=3, padx=5, pady=5)

stop_button = tk.Button(btn_frame, text="Stop Camera", font=("Arial", 14), bg="#00B4D8", fg="white", command=stop_camera)
stop_button.grid(row=0, column=4, padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
