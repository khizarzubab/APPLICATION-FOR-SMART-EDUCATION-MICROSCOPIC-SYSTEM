import tkinter as tk
from tkinter import messagebox, Label
import customtkinter
from PIL import Image, ImageTk
import cv2
import customtkinter as ctk

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
customtkinter.CTkLabel(
    root,
    text="PROCEDURE",
    font=("Times New Roman", 35),
    fg_color="#0077B6",
    text_color="white",
    corner_radius=4,
).grid(row=0, column=0, sticky="w", pady=20, padx=20)

# Paragraph Label
paragraph_text = (
    "This is a sample paragraph. It demonstrates how you can display a "
    "block of text in a Tkinter application. The Label widget is best "
    "used for static text that doesn't need user interaction.\n\n"
    "This is another sample text block for demonstration purposes."
)
paragraph_label = Label(
    root,
    text=paragraph_text,
    font=("Times New Roman", 18),
    bg="#90E0EF",
    fg="white",
    wraplength=400,
    justify="left",
)
paragraph_label.grid(row=1, column=0, rowspan=2, sticky="wnse", padx=25)

# Live Camera Feed
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 380)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 380)
 # Create a label to display the video feed
        self.video_label = ctk.CTkLabel(window)
        self.video_label.grid(row=0, column=0, columnspan=3, sticky="nsew")

        # Create a button to capture the image
        self.capture_button = ctk.CTkButton(window, text="Capture Image", command=self.capture_image)
        self.capture_button.grid(row=1, column=0, padx=20, pady=10)

        # Create a label to display the captured image
        self.captured_image_label = ctk.CTkLabel(window)
        self.captured_image_label.grid(row=0, column=1, sticky="nsew")

        # Create a button to clear the captured image
        self.clear_button = ctk.CTkButton(window, text="Clear Image", command=self.clear_image)
        self.clear_button.grid(row=1, column=1, padx=20, pady=10)

        # Initialize video capture
        self.vid = cv2.VideoCapture(0)
        self.captured_image_path = "captured_image.jpg"  # Path to save the captured image
        self.captured_image = None  # Variable to hold the captured image

        self.update_video()

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_video(self):
        ret, frame = self.vid.read()
        if ret:
            # Convert the frame to RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert the frame to ImageTk format
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)

        # Call this function again after 10 milliseconds
        self.video_label.after(10, self.update_video)

    def capture_image(self):
        ret, frame = self.vid.read()
        if ret:
            cv2.imwrite(self.captured_image_path, frame)
            self.captured_image = frame  # Store the captured image
            print(f"Image captured and saved as '{self.captured_image_path}'")
            self.display_captured_image()  # Display the captured image in the same window

    def display_captured_image(self):
        if self.captured_image is not None:
            # Convert the captured image to RGB format
            img = Image.fromarray(cv2.cvtColor(self.captured_image, cv2.COLOR_BGR2RGB))
            imgtk = ImageTk.PhotoImage(image=img)

            # Update the label to show the captured image
            self.captured_image_label.imgtk = imgtk
            self.captured_image_label.configure(image=imgtk)

    def clear_image(self):
        self.captured_image = None  # Clear the captured image variable
        self.captured_image_label.configure(image='')  # Clear the label displaying the image
        print("Captured image cleared.")

    def on_closing(self):
        self.vid.release()
        self.window.destroy()


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
