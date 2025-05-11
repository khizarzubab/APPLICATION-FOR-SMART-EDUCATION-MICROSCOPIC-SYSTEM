 
def open_procedure_stomata():
    clear_window()

import cv2
import customtkinter as ctk
from PIL import Image, ImageTk
import os

import tkinter as tk
from tkinter import ttk, messagebox
import cv2

class VideoPlayer:



   





    def __init__(self, window, video_source):
        self.window = window
        self.window.title("Video Player")
        
        # Load the video
        if not os.path.isfile(video_source):
            print(f"Error: Video file '{video_source}' not found.")
            self.window.destroy()
            return
        
        self.video_source = video_source
        self.vid = cv2.VideoCapture(self.video_source)

        # Create a label to display the video frames
        self.label = ctk.CTkLabel(window,text="play_video", fg_color="#90e0ef",text_color="white",width=580, height=580)  # Set the size of the video display
        self.label.place(relx=0.5, rely=0.2, relwidth=0.45, relheight=0.4)  # Center the label

        # Control buttons
        self.play_button = ctk.CTkButton(window, text="Play", command=self.play_video)
        self.play_button.place(relx=0.7, rely=0.65, relwidth=0.1, relheight=0.05)

        self.pause_button = ctk.CTkButton(window, text="Pause", command=self.pause_video)
        self.pause_button.place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.05)

        self.resume_button = ctk.CTkButton(window, text="Resume", command=self.resume_video)
        self.resume_button.place(relx=0.8, rely=0.65, relwidth=0.1, relheight=0.05)

        self.forward_button = ctk.CTkButton(window, text="Forward", command=self.forward_video)
        self.forward_button.place(relx=0.9, rely=0.65, relwidth=0.1, relheight=0.05)

        self.previous_button = ctk.CTkButton(window, text="Previous", command=self.previous_video)
        self.previous_button.place(relx=0.5, rely=0.65, relwidth=0.1, relheight=0.05)

        #self.stop_button = ctk.CTkButton(window, text="Stop", command=self.stop_video)
       # self.stop_button.place(relx=0.5, rely=0.65,relwidth=0.1, relheight=0.05 )
        

        
        # Add a paragraph using a Label
        paragraph_text = (
            "This is a sample paragraph. It demonstrates how you can display a "
            "block of text in a Tkinter application. The Label widget is best "
            "used for static text that doesn't need user interaction."
        )

        self.paragraph_label = ctk.CTkLabel(
            window,
            text=paragraph_text,
            font=("Times New Roman", 18),
            fg_color="#90e0ef",  # Use fg_color instead of bg
            wraplength=300,
            justify="left",
        )
        self.paragraph_label.place(relx=0.05, rely=0.2, relwidth=0.4, relheight=0.6)


        # Buttons
        ctk.CTkLabel(
            window,
            text="PROCEDURE",
            font=("Times New Roman", 35),
            fg_color="#0077B6",  # Background color
            text_color="white",  # Text color
        ).place(relx=0.05, rely=0.05, relwidth=0.3, relheight=0.1)

        ctk.CTkLabel(
            window,
            text="STEPS",
            font=("Times New Roman", 22),
            fg_color="#00B4D8",  # Background color
            text_color="white",
            corner_radius=4,
        ).place(relx=0.8, rely=0.05, relwidth=0.15, relheight=0.08)

        ctk.CTkButton(
            window,
            text="NEXT",
            font=("Times New Roman", 22),
            fg_color="#00B4D8",  # Background color
            text_color="white",  # Text color
            corner_radius=10,
        ).place(relx=0.8, rely=0.85)

        ctk.CTkButton(
            window,
            text="PREVIOUS",
            font=("Times New Roman", 22),
            fg_color="#00B4D8",  # Background color
            text_color="white",  # Text color
            corner_radius=8,
        ).place(relx=0.65, rely=0.85)

        ctk.CTkButton(
            window,
            text="QUIT",
            font=("Times New Roman", 22),
            fg_color="#00B4D8",  # Background color
            text_color="white",  # Text color
            corner_radius=10,
            command=self.on_closing
        ).place(relx=0.05, rely=0.85)

        
        self.is_playing = False
        self.is_paused = False

        # Start the video playback
        self.update()

        # Close the video when the window is closed
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def play_video(self):
        self.is_playing = True
        self.is_paused = False

    def pause_video(self):
        self.is_paused = True

    def resume_video(self):
        if self.is_paused:
            self.is_paused = False

    def forward_video(self):
        # Skip forward by 5 seconds (adjust as needed)
        current_pos = self.vid.get(cv2.CAP_PROP_POS_MSEC)
        self.vid.set(cv2.CAP_PROP_POS_MSEC, current_pos + 5000)

    def previous_video(self):
        # Skip backward by 5 seconds (adjust as needed)
        current_pos = self.vid.get(cv2.CAP_PROP_POS_MSEC)
        self.vid.set(cv2.CAP_PROP_POS_MSEC, max(0, current_pos - 5000))

    def update(self):
        if self.is_playing and not self.is_paused:
            # Get the next frame from the video
            ret, frame = self.vid.read()
            if ret:
                # Convert the frame from BGR to RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Resize the frame to fit the label
                frame = cv2.resize(frame, (580, 580))  # Resize to match label size
                # Convert the frame to a PhotoImage
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.label.imgtk = imgtk
                self.label.configure(image=imgtk)
            else:
                self.stop_video()  # Stop if the video ends

        # Call this function again after a short delay
        self.window.after(10, self.update)

    def stop_video(self):
        self.is_playing = False
        self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset to the beginning






    def on_closing(self):
        # Release the video capture object and destroy the window
        self.vid.release()
        self.window.destroy()





if __name__ == "__main__":
    # Set the appearance mode and color theme
    ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

    # Create a Tk window
    root = ctk.CTk()  # Use CTk for a custom appearance
    # Create a VideoPlayer object
    video_player = VideoPlayer(root, "video_stomata2.mp4")

    root.geometry("1000x530")
    
    root.config(bg="#CAF0F8")

    # Start the CTk event loop
    root.mainloop()