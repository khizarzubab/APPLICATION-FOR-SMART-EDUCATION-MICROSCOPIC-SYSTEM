import cv2
import customtkinter as ctk
from PIL import Image, ImageTk
import threading
import time
import os

class VideoPlayer:
    def __init__(self, window, video_source):
        self.window = window
        self.window.title("Experiment Program")
        self.window.geometry("1000x530")
        self.window.config(bg="#CAF0F8")

        # Video properties
        self.video_source = video_source
        self.cap = cv2.VideoCapture(self.video_source)
        self.video_running = False
        self.video_paused = False
        self.current_frame = 0

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

        # Video label
        self.video_label = ctk.CTkLabel(window, fg_color="#CAF0F8")  # Use fg_color instead of bg
        self.video_label.place(relx=0.5, rely=0.2, relwidth=0.45, relheight=0.4)

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

        # Video control buttons
        self.play_button = ctk.CTkButton(window, text="Play", font=("Times New Roman", 18), command=self.play_video)
        self.play_button.place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.05)

        self.pause_button = ctk.CTkButton(window, text="Pause", font=("Times New Roman", 18), command=self.pause_video)
        self.pause_button.place(relx=0.7, rely=0.65, relwidth=0.1, relheight=0.05)

        self.stop_button = ctk.CTkButton(window, text="Stop", font=("Times New Roman", 18), command=self.stop_video)
        self.stop_button.place(relx=0.8, rely=0.65, relwidth=0.1, relheight=0.05)

        self.forward_button = ctk.CTkButton(window, text="Forward", font=("Times New Roman", 18), command=self.forward_video)
        self.forward_button.place(relx=0.9, rely=0.65, relwidth=0.1, relheight=0.05)

        self.rewind_button = ctk.CTkButton(window, text="Rewind", font=("Times New Roman", 18), command=self.rewind_video)
        self.rewind_button.place(relx=0.5, rely=0.65, relwidth=0.1, relheight=0.05)

    def play_video(self):
        """Play the video."""
        if not self.video_running:
            self.video_running = True
            self.video_paused = False
            thread = threading.Thread(target=self.update_frame)
            thread.daemon = True
            thread.start()

    def pause_video(self):
        """Pause the video."""
        self.video_paused = True

    def stop_video(self):
        """Stop the video."""
        self.video_running = False
        self.video_paused = False
        self.current_frame = 0
        self.video_label.configure(image="")  # Clear the video frame

    def forward_video(self):
        """Skip forward 5 seconds."""
        self.current_frame += int(self.cap.get(cv2.CAP_PROP_FPS)) * 5  # Skip 5 seconds

    def rewind_video(self):
        """Rewind 5 seconds."""
        self.current_frame -= int(self.cap.get(cv2.CAP_PROP_FPS)) * 5  # Go back 5 seconds
        self.current_frame = max(0, self.current_frame)  # Prevent negative frames

    def update_frame(self):
        """Update video frames in the CustomTkinter interface."""
        while self.video_running:
            if self.video_paused:
                time.sleep(0.1)
                continue

            self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame)
            ret, frame = self.cap.read()

            if not ret:
                self.stop_video()
                break

            # Resize frame to fit in the window
            frame = cv2.resize(frame, (800, 450))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB for Tkinter

            # Convert frame to ImageTk
            img = Image.fromarray(frame)
            img_tk = ImageTk.PhotoImage(image=img)

            # Display the frame
            self.video_label.img_tk = img_tk
            self.video_label.configure(image=img_tk)

            self.current_frame += 1
            time.sleep(1 / self.cap.get(cv2.CAP_PROP_FPS))  # Control frame rate

    def on_closing(self):
        """Handle the window closing event."""
        self.cap.release()
        self.window.destroy()

if __name__ == "__main__":
    video_path = "video_stomata2.mp4"  # Replace with your video file path
    root = ctk.CTk()  # Create the main window
    player = VideoPlayer(root, video_path)  # Create the video player instance
    root.mainloop()  # Run the CustomTkinter event loop