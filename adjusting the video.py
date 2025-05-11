import cv2
import customtkinter as ctk
from PIL import Image, ImageTk

class VideoCaptureApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Configure grid layout for responsiveness
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=4)
        self.window.grid_rowconfigure(2, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=1)

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

# Create the main window
root = ctk.CTk()
app = VideoCaptureApp(root, "Live Video Capture")

root.geometry("1000x530")
root.mainloop()