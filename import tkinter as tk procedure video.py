import tkinter as tk
from tkinter import messagebox, Label
import customtkinter
from PIL import Image, ImageTk
import cv2

# Initialize the root window
root = customtkinter.CTk()
root.title("Experiment Program")
root.geometry("1000x530")
root.config(bg="#CAF0F8")

# Configure grid layout for responsiveness
root.grid_rowconfigure(0, weight=1)  # Header row
root.grid_rowconfigure(1, weight=4)  # Content row
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)

# Header Button
summary_label = customtkinter.CTkLabel(
    root,
    text="OBSERVATION",
    font=("Times New Roman", 35),
    fg_color="#0077B6",
    text_color="white",
    corner_radius=4,
)
summary_label.grid(row=0, column=0, sticky="w", pady=20, padx=20)


# Live Camera Feed
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 380)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 380)

def show_camera():
    def update_frame():
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img_tk = ImageTk.PhotoImage(image=img)
            video_label.img_tk = img_tk
            video_label.config(image=img_tk)
        video_label.after(10, update_frame)

    update_frame()

video_label = tk.Label(root, bg="#CAF0F8")
video_label.grid(row=1, column=2, rowspan=2, columnspan=3,sticky="ns", padx=30, pady=10)
show_camera()

# Footer Buttons
previous_button = customtkinter.CTkButton(
    root,
    text="QUIT",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",
    text_color="white",
    corner_radius=10,
    command=root.quit,
)
previous_button.grid(row=3, column=0, padx=20, sticky="w")

steps_label = customtkinter.CTkLabel(
    root,
    text="STEPS",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",
    text_color="white",
    corner_radius=4,
)
steps_label.grid(row=0, column=4,pady=10, padx=20)

next_button = customtkinter.CTkButton(
    root,
    text="NEXT",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",
    text_color="white",
    corner_radius=10,
)
next_button.grid(row=3, column=4,sticky="w" ,pady=10, padx=20)

quit_button = customtkinter.CTkButton(
    root,
    text="PREVIOUS",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",
    text_color="white",
    corner_radius=10,
)
quit_button.grid(row=3, column=3,sticky="e", pady=10)

# Release resources on close
def on_closing():
    cap.release()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the Tkinter event loop
root.mainloop()
