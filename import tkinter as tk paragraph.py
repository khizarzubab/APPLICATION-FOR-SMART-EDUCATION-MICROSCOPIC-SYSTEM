import customtkinter as ctk
from tkinter import messagebox
import customtkinter

from PIL import Image, ImageTk  # Import Pillow for image handling

import tkinter as tk
from tkinter import ttk, messagebox
import cv2
from PIL import Image, ImageTk
import threading
import time

import customtkinter
import tkinter as tk
from tkinter import ttk, messagebox
import cv2
from PIL import Image, ImageTk
import threading
import time
import customtkinter


# Function to handle login
def login():
    name = name_entry.get()
    roll_number = roll_entry.get()
    role = role_var.get()
    if not name or not roll_number or not role:
        messagebox.showwarning("Login Failed", "Please fill in all fields!")
    else:
        open_language_selection()

# Function to open the language selection page
def open_language_selection():
    clear_window()
    ctk.CTkLabel(root, text="Select Your Language", font=("Times New Roman", 28, "bold"), fg_color="#0077b6", text_color="white").grid(row=0, column=0, columnspan=2, pady=30, sticky="nsew")
    ctk.CTkButton(root, text="English", font=("Times New Roman", 22), fg_color="#00B4D8", text_color="white", command=open_class_selection).grid(row=1, column=0, padx=20, pady=10, sticky="ew")
    ctk.CTkButton(root, text="Urdu", font=("Times New Roman", 22), fg_color="#00B4D8", text_color="white", command=lambda: messagebox.showinfo("Coming Soon", "Urdu is under development.")).grid(row=1, column=1, padx=20, pady=10, sticky="ew")
    ctk.CTkButton(root, text="BACK", font=("Times New Roman", 22), fg_color="#00B4D8", text_color="white", command=open_login_page).grid(row=2, column=0, columnspan=2, pady=20, sticky="nsew")

# Function to open the class selection page
def open_class_selection():
    clear_window()
    ctk.CTkLabel(root, text="Select Your CLASS", font=("Times New Roman", 28, "bold"), fg_color="#0077b6", text_color="white").grid(row=0, column=0, columnspan=2, pady=30, sticky="nsew")
    classes = ["CLASS 9", "CLASS 10", "CLASS 11", "CLASS 12"]
    for i, cls in enumerate(classes):
        ctk.CTkButton(root, text=cls, font=("Times New Roman", 18), fg_color="#00B4D8", text_color="white", command=(open_board_selection if cls == "CLASS 9" else lambda: messagebox.showinfo("Coming Soon", "Under development."))).grid(row=i+1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
    ctk.CTkButton(root, text="BACK", font=("Times New Roman", 18), fg_color="#00B4D8", text_color="white", command=open_language_selection).grid(row=len(classes)+1, column=0, columnspan=2, pady=20, sticky="nsew")

# Function to open the board selection page
def open_board_selection():
    clear_window()
    ctk.CTkLabel(root, text="Select Your BOARD", font=("Times New Roman", 28, "bold"), fg_color="#0077b6", text_color="white").grid(row=0, column=0, columnspan=2, pady=30, sticky="nsew")
    boards = ["LAHORE BOARD", "KPK BOARD", "SINDH BOARD", "FEDERAL BOARD"]
    for i, board in enumerate(boards):
        ctk.CTkButton(root, text=board, font=("Times New Roman", 18), fg_color="#00B4D8", text_color="white", command=(open_topic_selection if board == "LAHORE BOARD" else lambda: messagebox.showinfo("Coming Soon", "Under development."))).grid(row=i+1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
    ctk.CTkButton(root, text="BACK", font=("Times New Roman", 18), fg_color="#00B4D8", text_color="white", command=open_class_selection).grid(row=len(boards)+1, column=0, columnspan=2, pady=20, sticky="nsew")

# Function to open the topic selection page
def open_topic_selection():
    clear_window()
    ctk.CTkLabel(root, text="Select Your Topic", font=("Times New Roman", 28, "bold"), fg_color="#0077b6", text_color="white").grid(row=0, column=0, columnspan=2, pady=30, sticky="nsew")
    topics = ["Structure and Number of Stomata", "TOPIC 2", "TOPIC 3", "TOPIC 4"]
    for i, topic in enumerate(topics):
        ctk.CTkButton(root, text=topic, font=("Times New Roman", 18), fg_color="#00B4D8", text_color="white", command=(open_experiment_selection if topic == "Structure and Number of Stomata" else lambda: messagebox.showinfo("Coming Soon", "Under development."))).grid(row=i+1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
    ctk.CTkButton(root, text="BACK", font=("Times New Roman", 18), fg_color="#00B4D8", text_color="white", command=open_board_selection).grid(row=len(topics)+1, column=0, columnspan=2, pady=20, sticky="nsew")

# Function to open the experiment selection page
def open_experiment_selection():
    clear_window()
    ctk.CTkLabel(root, text="Select Your EXPERIMENT", font=("Times New Roman", 28, "bold"), fg_color="#0077b6", text_color="white").grid(row=0, column=0, columnspan=2, pady=30, sticky="nsew")
    experiments = ["Describe the Structure and Number of Stomata", "EXPERIMENT 2", "EXPERIMENT 3"]
    for i, exp in enumerate(experiments):
        ctk.CTkButton(root, text=exp, font=("Times New Roman", 18), fg_color="#00B4D8", text_color="white", command=(summary_of_stomata if exp == "Describe the Structure and Number of Stomata" else lambda: messagebox.showinfo("Coming Soon", "Under development."))).grid(row=i+1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
    ctk.CTkButton(root, text="BACK", font=("Times New Roman", 18), fg_color="#00B4D8", text_color="white", command=open_topic_selection).grid(row=len(experiments)+1, column=0, columnspan=2, pady=20, sticky="nsew")

# Function to display the summary of stomata
def summary_of_stomata():
    clear_window()



      
# Configure grid layout for responsiveness
    root.grid_rowconfigure(0, weight=1)  # Header row
    root.grid_rowconfigure(1, weight=4)  # Content row
    root.grid_rowconfigure(2, weight=1) 
 

                                               # Footer row
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)



    

    ctk.CTkLabel(
    root,
    text="SUMMARY",
    font=("Times New Roman", 35),
    fg_color="#0077B6",  # Background color
    text_color="white",
    width=15,
      # Text color
    #corner_radius=8,                           # Rounded corner radius
       # Button height

).grid(row=0, column=0,sticky= "w",pady=20, padx=20)  # Stretch horizontally



    ctk.CTkLabel(
    root,
    text="SUMMARY",
    font=("Times New Roman", 35),
    fg_color="#0077B6",  # Background color
    text_color="white",
    width=15,
      # Text color
    #corner_radius=8,                           # Rounded corner radius
       # Button height

).grid(row=0, column=0,sticky= "w",pady=20, padx=20)  # Stretch horizontally





# Paragraph Label
    paragraph_text = (
    "1. INTRODUCTION\n\n"
    "2. APPARATUS\n\n"
    "3. PROCEDURE\n\n"
    "4. OBSERVATION\n\n"
    "5. RESULT\n"
)



    ctk.CTkLabel(
    root,
    text=paragraph_text,
    font=("Times New Roman", 24),
    fg_color="#90E0EF",  # Background color
    text_color="white",
    wraplength=700,  # Wrap text after 700 pixels
    justify="left",
    width=30,
    height=12

).grid(row=1, column=0, sticky="wnse", padx=25)

# Footer Buttons
    ctk.CTkButton(
    root,
    text="QUIT",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",  # Text color
    corner_radius=10
).grid(row=2, column=0, padx=20, sticky="w")


    customtkinter.CTkLabel(
    root,
    text="STEPS",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",
      # Text color
   # corner_radius=8,  
      width=20  # Rounded corner radius    # Button height

).grid(row=0, column=2, sticky= "e", padx=20 )

    customtkinter.CTkButton(
    root,
    text="NEXT",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",  # Text color
    corner_radius=10,
    width=15  ,
    command=open_introduction_stometa ,    # Rounded corner radiu
).grid(row=2, column=2, pady=10,sticky="e",padx=20)

    customtkinter.CTkButton(
    root,
    text="PREVIOUS",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",  # Text color
    corner_radius=10,
    width=15
).grid(row=2, column=2,padx=10)








def open_introduction_stometa():
    clear_window()


# Configure grid layout for responsiveness
    root.grid_rowconfigure(0, weight=1)  # Header row
    root.grid_rowconfigure(1, weight=4)  # Content row
    root.grid_rowconfigure(2, weight=1) 
    root.grid_rowconfigure(3, weight=1) 

                                               # Footer row
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_columnconfigure(3, weight=1)





# Header Button


    customtkinter.CTkLabel(
    root,
    text="INTRODUCTION",
    font=("Times New Roman", 35),
    fg_color="#0077B6",  # Background color
    text_color="white",
    width=15,
      # Text color
    corner_radius=4,                           # Rounded corner radius
       # Button height

).grid(row=0, column=0,sticky= "w",pady=20, padx=20)  # Stretch horizontally





# Paragraph Label
    paragraph_text = (
    "This is a sample paragraph. It demonstrates how you can display a "
    "block of text in a Tkinter application. The Label widget is best "
    "used for static text that doesn't need user interaction."
    "\n\n"
    "This is a sample paragraph. It demonstrates how you can display a "
    "block of text in a Tkinter application. The Label widget is best "
    "used for static text that doesn't need user interaction."

    "This is a sample paragraph. It demonstrates how you can display a "
    "block of text in a Tkinter application. The Label widget is best "
    "used for static text that doesn't need user interaction."
    "\n\n"
    "This is a sample paragraph. It demonstrates how you can display a "
    "block of text in a Tkinter application. The Label widget is best "
    "used for static text that doesn't need user interaction."
    "This is a sample paragraph. It demonstrates how you can display a "
    "block of text in a Tkinter application. The Label widget is best "
    "used "
)
    ctk.CTkLabel(
    root,
    text=paragraph_text,
    font=("Times New Roman", 18),
    fg_color="#90E0EF",  # Background color
    text_color="white",
    wraplength=500,  # Wrap text after 700 pixels
    justify="left",
   # width=30,
    #height=12

).grid(row=1, column=0,rowspan=2, sticky="wnse", padx=25)





# Add an image using Pillow
    




# Footer Buttons
    customtkinter.CTkButton(
    root,
    text="QUIT",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",  # Text color
    corner_radius=10
).grid(row=3, column=0, padx=20, sticky="w")


    customtkinter.CTkLabel(
    root,
    text="STEPS",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",
      # Text color
   corner_radius=4,  
      # Rounded corner radius    # Button height

).grid(row=0, column=3,pady=10, padx=20 )

    customtkinter.CTkButton(
    root,
    text="NEXT",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",  # Text color
    corner_radius=10,
    width=15,
    command= open_introduction_stometa_full_scren_video,        # Rounded corner radiu
).grid(row=3, column=3,sticky="w",pady=10,padx=20)

    customtkinter.CTkButton(
    root,
    text="PREVIOUS",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",  # Text color
    corner_radius=10,
    width=15
).grid(row=3, column=2,sticky="e",pady=10,padx=10)




# Add an image using Pillow
    try:
    # Load image using Pillow (replace 'sample.png' with your image path)
         pil_image = Image.open("sample.png").resize((250, 250))  # Resize if needed
         image = ctk.CTkImage(pil_image, size=(250, 250))  # Convert to CTkImage for CustomTkinter

    # Image label
         image_label = ctk.CTkLabel(root, image=image, text="", fg_color="#CAF0F8")  # Text is set to empty
         image_label.grid(row=1, column=1, columnspan=3, pady=10, padx=10)

    except FileNotFoundError:
    # Display an error if the image file is not found
        error_label = ctk.CTkLabel(
        root,
        text="Image not found!",
        font=("Arial", 16),
        text_color="red",
        fg_color="#CAF0F8",
    )
    error_label.grid(row=1, column=1, )



# Function to return to the login page
def open_introduction_stometa_full_scren_video():
    # Ensure global variables are declared properly
    global video_running, video_paused, current_frame, cap, video_label

    # Reset window
    clear_window()

    # Configure grid layout for responsiveness
    root.grid_rowconfigure(0, weight=1)  # Header row
    root.grid_rowconfigure(1, weight=4)  # Video display row
    root.grid_rowconfigure(2, weight=1)  # Footer row
    root.grid_columnconfigure(0, weight=1)  # First column (Left side)
    root.grid_columnconfigure(1, weight=2)  # Video display area (Center)
    root.grid_columnconfigure(2, weight=1)  # Right side for controls

    # Header Label
    ctk.CTkLabel(
        root,
        text="Introduction with Video",
        font=("Times New Roman", 35),
        fg_color="#0077B6",
        text_color="white",
        corner_radius=3,
    ).grid(row=0, column=0, columnspan=3, pady=20, padx=20, sticky="nsew")

    # "QUIT" Button
    ctk.CTkButton(
        root,
        text="QUIT",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=10,
        command=root.quit,
    ).grid(row=3, column=0, padx=20, sticky="w")



    customtkinter.CTkButton(
    root,
    text="PREVIOUS",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",  # Text color
    corner_radius=10,
    width=15
).grid(row=3, column=2,sticky="e",pady=10,padx=10)

    # "NEXT" Button
    ctk.CTkButton(
        root,
        text="NEXT",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=10,
        command=open_apparatus_stometa,  # Placeholder for next function
    ).grid(row=3, column=3,sticky="w",pady=10,padx=20)


    # Video Properties
    video_path = "video.mp4"
    cap = cv2.VideoCapture(video_path)
    video_running = False
    video_paused = False
    current_frame = 0

    # Functions for video control
    def play_video():
        """Play the video."""
        global video_running, video_paused
        video_running = True
        video_paused = False
        thread = threading.Thread(target=update_frame)
        thread.daemon = True
        thread.start()

    def pause_video():
        """Pause the video."""
        global video_paused
        video_paused = True

    def stop_video():
        """Stop the video."""
        global video_running, video_paused, current_frame
        video_running = False
        video_paused = False
        current_frame = 0
        video_label.configure(image=None)  # Clear the video frame

    def forward_video():
        """Skip forward 5 seconds."""
        global current_frame
        current_frame += int(cap.get(cv2.CAP_PROP_FPS)) * 5  # Skip 5 seconds

    def rewind_video():
        """Rewind 5 seconds."""
        global current_frame
        current_frame -= int(cap.get(cv2.CAP_PROP_FPS)) * 5  # Go back 5 seconds
        current_frame = max(0, current_frame)  # Prevent negative frames

    def update_frame():
        """Update video frames in the Tkinter interface."""
        global video_running, video_paused, current_frame
        while video_running:
            if video_paused:
                time.sleep(0.1)
                continue

            cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
            ret, frame = cap.read()

            if not ret:
                stop_video()
                break

            # Resize frame to fit in the window
            frame = cv2.resize(frame, (800, 400))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB for Tkinter

            # Convert frame to ImageTk
            img = Image.fromarray(frame)
            img_tk = ImageTk.PhotoImage(image=img)

            # Display the frame
            video_label.img_tk = img_tk
            video_label.configure(image=img_tk)

            current_frame += 1
            time.sleep(1 / cap.get(cv2.CAP_PROP_FPS))  # Control frame rate

    # Video Display Label
    video_label = ctk.CTkLabel(root, text="", fg_color="#CAF0F8", corner_radius=10)
    video_label.grid(row=1, column=0, columnspan=3, sticky="nsew", pady=10, padx=10)

    # Footer Buttons Frame
    footer_frame = ctk.CTkFrame(root, fg_color="#CAF0F8", corner_radius=10)
    footer_frame.grid(row=2, column=0, columnspan=3, sticky="ew", pady=10, padx=10)

    # Video control buttons
    ctk.CTkButton(footer_frame, text="Play", font=("Times New Roman", 14), fg_color="#00B4D8", text_color="white", command=play_video).grid(row=0, column=0, padx=6, pady=6)
    ctk.CTkButton(footer_frame, text="Pause", font=("Times New Roman", 14), fg_color="#00B4D8", text_color="white", command=pause_video).grid(row=0, column=1, padx=6, pady=6)
    ctk.CTkButton(footer_frame, text="Stop", font=("Times New Roman", 14), fg_color="#00B4D8", text_color="white", command=stop_video).grid(row=0, column=2, padx=6, pady=6)
    ctk.CTkButton(footer_frame, text="Forward", font=("Times New Roman", 14), fg_color="#00B4D8", text_color="white", command=forward_video).grid(row=0, column=3, padx=6, pady=6)
    ctk.CTkButton(footer_frame, text="Rewind", font=("Times New Roman", 14), fg_color="#00B4D8", text_color="white", command=rewind_video).grid(row=0, column=4, padx=6, pady=6)



def open_apparatus_stometa():
    clear_window()

# Configure grid layout for responsiveness
    root.grid_rowconfigure(0, weight=1)  # Header row
    root.grid_rowconfigure(1, weight=1)  # Content rows
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_columnconfigure(3, weight=1)
    root.grid_columnconfigure(4, weight=1)

# Header
    ctk.CTkLabel(
    root,
    text="APPARATUS",
    font=("Times New Roman", 35),
    fg_color="#023EBA",
    text_color="white",
    corner_radius=4,
).grid(row=0, column=0, pady=20, padx=20, sticky="nw")

    ctk.CTkLabel(
    root,
    text="STEPS",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",
    text_color="white",
    corner_radius=4,
).grid(row=0, column=4, pady=10, padx=20)

# Buttons
    ctk.CTkButton(
    root,
    text="QUIT",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",
    text_color="white",
    corner_radius=10,
    command=root.quit,  # Exits the app
).grid(row=5, column=0, pady=10, padx=10, sticky="w")

    ctk.CTkButton(
    root,
    text="PREVIOUS",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",
    text_color="white",
    corner_radius=10,
).grid(row=5, column=3, pady=10, padx=10, sticky="e")

    ctk.CTkButton(
    root,
    text="NEXT",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",
    text_color="white",
    corner_radius=10,
    command=open_procedure_stomata ,
).grid(row=5, column=4, pady=10, padx=10, sticky="w")


# Function to load images and add labels
    def add_image_with_label(row, column, image_path, label_text):
        try:
        # Load and resize the image
            pil_image = Image.open(image_path).resize((60, 60))
            image = ImageTk.PhotoImage(pil_image)

        # Create image label
            image_label = ctk.CTkLabel(root, image=image, text="", fg_color="#CAF0F8", corner_radius=10)
            image_label.image = image  # Keep a reference to avoid garbage collection
            image_label.grid(row=row, column=column, pady=2, padx=2)

        # Create text label
            ctk.CTkLabel(
            root,
            text=label_text,
            font=("Times New Roman", 18),
            text_color="white",
            fg_color="#0077B6",
            corner_radius=10,
            padx=10,
        ).grid(row=row + 1, column=column, pady=2, padx=6)
        except FileNotFoundError:
        # Handle missing image
            ctk.CTkLabel(
            root,
            text=f"Image '{image_path}' not found!",
            font=("Arial", 14),
            text_color="white",
            fg_color="#FF6B6B",
            corner_radius=10,
            padx=2,
        ).grid(row=row, column=column, pady=2, padx=2)


# Add multiple images with labels
    add_image_with_label(1, 0, "sample.png", "Sample Image")
    add_image_with_label(1, 1, "microscope.png", "Microscope")
    add_image_with_label(1, 2, "components.png", "Components") 
    add_image_with_label(1, 3, "water.png", "Water")
    add_image_with_label(3, 0, "slides.png", "Slides")
    add_image_with_label(3, 1, "pedri dish.png", "Pedri Dish")
    add_image_with_label(3, 2, "cover slips.png", "Cover Slips")



def open_procedure_stomata():
    clear_window()

    # Paragraph Label
    paragraph_text = (
        "This is a sample paragraph. It demonstrates how you can display a "
        "block of text in a CustomTkinter application. The Label widget is best "
        "used for static text that doesn't need user interaction."
    )

    ctk.CTkLabel(
        root,
        text=paragraph_text,
        font=("Times New Roman", 18),
        fg_color="#90e0ef",
        text_color="black",
        corner_radius=10,
        justify="left",
        wraplength=300,
    ).place(relx=0.05, rely=0.2, relwidth=0.4, relheight=0.6)

    # Video Label
    video_label = ctk.CTkLabel(root, text="", fg_color="#CAF0F8", corner_radius=10)
    video_label.place(relx=0.5, rely=0.2, relwidth=0.45, relheight=0.4)

    # Titles and Buttons
    ctk.CTkLabel(
        root,
        text="PROCEDURE",
        font=("Times New Roman", 35),
        fg_color="#0077B6",
        text_color="white",
        corner_radius=10,
    ).place(relx=0.05, rely=0.05, relwidth=0.3, relheight=0.1)

    ctk.CTkLabel(
        root,
        text="STEPS",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=4,
    ).place(relx=0.8, rely=0.05, relwidth=0.15, relheight=0.08)

    ctk.CTkButton(
        root,
        text="NEXT",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=10,
        command=open_procedure_withlive_video_stometa,
    ).place(relx=0.8, rely=0.85)

    ctk.CTkButton(
        root,
        text="PREVIOUS",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=8,
    ).place(relx=0.65, rely=0.85)

    ctk.CTkButton(
        root,
        text="QUIT",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=10,
        command=root.quit,
    ).place(relx=0.05, rely=0.85)

    # Video Playback Variables
    video_path = "video.mp4"  # Replace with your video file path
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    global video_running, video_paused, current_frame
    video_running = False
    video_paused = False
    current_frame = 0

    def play_video():
        """Play the video."""
        global video_running, video_paused
        video_running = True
        video_paused = False
        thread = threading.Thread(target=update_frame)
        thread.daemon = True
        thread.start()

    def pause_video():
        """Pause the video."""
        global video_paused
        video_paused = True

    def stop_video():
        """Stop the video."""
        global video_running, video_paused, current_frame
        video_running = False
        video_paused = False
        current_frame = 0
        video_label.configure(image=None)  # Clear the video frame

    def forward_video():
        """Skip forward 5 seconds."""
        global current_frame
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        current_frame += fps * 5  # Skip 5 seconds

    def rewind_video():
        """Rewind 5 seconds."""
        global current_frame
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        current_frame -= fps * 5  # Go back 5 seconds
        current_frame = max(0, current_frame)  # Prevent negative frames

    def update_frame():
        """Update video frames in the CustomTkinter interface."""
        global video_running, video_paused, current_frame
        while video_running:
            if video_paused:
                time.sleep(0.1)
                continue

            cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
            ret, frame = cap.read()

            if not ret:
                stop_video()
                break

            # Resize frame to fit in the window
            frame = cv2.resize(frame, (800, 450))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB for Tkinter

            # Convert frame to ImageTk
            img = Image.fromarray(frame)
            img_tk = ImageTk.PhotoImage(image=img)

            # Display the frame
            video_label.img_tk = img_tk
            video_label.configure(image=img_tk)

            current_frame += 1
            time.sleep(1 / cap.get(cv2.CAP_PROP_FPS))  # Control frame rate

    # Video Control Buttons
    ctk.CTkButton(
        root,
        text="Play",
        font=("Times New Roman", 18),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=5,
        command=play_video,
    ).place(relx=0.6, rely=0.65, relwidth=0.1, relheight=0.05)

    ctk.CTkButton(
        root,
        text="Pause",
        font=("Times New Roman", 18),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=5,
        command=pause_video,
    ).place(relx=0.7, rely=0.65, relwidth=0.1, relheight=0.05)

    ctk.CTkButton(
        root,
        text="Stop",
        font=("Times New Roman", 18),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=5,
        command=stop_video,
    ).place(relx=0.8, rely=0.65, relwidth=0.1, relheight=0.05)

    ctk.CTkButton(
        root,
        text="Forward",
        font=("Times New Roman", 18),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=5,
        command=forward_video,
    ).place(relx=0.9, rely=0.65, relwidth=0.1, relheight=0.05)

    ctk.CTkButton(
        root,
        text="Rewind",
        font=("Times New Roman", 18),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=5,
        command=rewind_video,
    ).place(relx=0.5, rely=0.65, relwidth=0.1, relheight=0.05)







import cv2
import customtkinter as ctk
from PIL import Image, ImageTk

def open_procedure_withlive_video_stometa():
    # Assuming clear_window is defined somewhere else
    clear_window()

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

    # Header Label
    ctk.CTkLabel(
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
    ctk.CTkLabel(
        root,
        text=paragraph_text,
        font=("Times New Roman", 18),
        fg_color="#90E0EF",
        text_color="white",
        corner_radius=4,
        wraplength=400,
        justify="left",
    ).grid(row=1, column=0, rowspan=2, sticky="wnse", padx=25)

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
                video_label.configure(image=img_tk)
            video_label.after(10, update_frame)

        update_frame()

    video_label = ctk.CTkLabel(root, text="", fg_color="#CAF0F8")
    video_label.grid(row=1, column=2, rowspan=2, columnspan=3, sticky="ns", padx=30, pady=10)
    show_camera()

    # Footer Buttons
    ctk.CTkButton(
        root,
        text="QUIT",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=10,
        command=root.quit,
    ).grid(row=3, column=0, padx=20, sticky="w")

    ctk.CTkLabel(
        root,
        text="STEPS",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=4,
    ).grid(row=0, column=4, pady=10, padx=20)

    ctk.CTkButton(
        root,
        text="NEXT",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=10,
        command=open_observation_stometa,
    ).grid(row=3, column=4, sticky="w", pady=10, padx=20)

    ctk.CTkButton(
        root,
        text="PREVIOUS",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=10,
    ).grid(row=3, column=3, sticky="e", pady=10)

    # Release resources on close
    def on_closing():
        cap.release()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)






def open_observation_stometa():
    clear_window()





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

    # Header Label
    ctk.CTkLabel(
        root,
        text="OBSERVATION",
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
    ctk.CTkLabel(
        root,
        text=paragraph_text,
        font=("Times New Roman", 18),
        fg_color="#90E0EF",
        text_color="white",
        corner_radius=4,
        wraplength=400,
        justify="left",
    ).grid(row=1, column=0, rowspan=2, sticky="wnse", padx=25)

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
                video_label.configure(image=img_tk)
            video_label.after(10, update_frame)

        update_frame()

    video_label = ctk.CTkLabel(root, text="", fg_color="#CAF0F8")
    video_label.grid(row=1, column=2, rowspan=2, columnspan=3, sticky="ns", padx=30, pady=10)
    show_camera()

    # Footer Buttons
    ctk.CTkButton(
        root,
        text="QUIT",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=10,
        command=root.quit,
    ).grid(row=3, column=0, padx=20, sticky="w")

    ctk.CTkLabel(
        root,
        text="STEPS",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=4,
    ).grid(row=0, column=4, pady=10, padx=20)

    ctk.CTkButton(
        root,
        text="NEXT",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=10,
    ).grid(row=3, column=4, sticky="w", pady=10, padx=20)

    ctk.CTkButton(
        root,
        text="PREVIOUS",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=10,
    ).grid(row=3, column=3, sticky="e", pady=10)

    # Release resources on close
    def on_closing():
        cap.release()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)












# Function to return to the login page
def open_login_page():
    clear_window()
    global name_entry, roll_entry, role_var
    ctk.CTkLabel(root, text="Login Page", font=("Times New Roman", 28, "bold"), fg_color="#CAF0F8", text_color="#333").grid(row=0, column=1, columnspan=2,sticky="wn" )
    ctk.CTkLabel(root, text="Enter Your Name:", font=("Times New Roman", 16), text_color="#333").grid(row=0, column=1,pady=25, sticky="w")
    name_entry = ctk.CTkEntry(root, font=("Times New Roman", 16))
    name_entry.grid(row=1, column=1, padx=10, sticky="w")
    ctk.CTkLabel(root, text="Enter Your Roll Number:", font=("Times New Roman", 16), text_color="#333").grid(row=2, column=0, padx=10, sticky="e")
    roll_entry = ctk.CTkEntry(root, font=("Times New Roman", 16))
    roll_entry.grid(row=2, column=1, padx=10, sticky="w")
    ctk.CTkLabel(root, text="Are you a Student or Teacher?", font=("Times New Roman", 16), text_color="#333").grid(row=3, column=0, columnspan=2, pady=10, sticky="n")
    role_var = ctk.StringVar()
    ctk.CTkRadioButton(root, text="Student", variable=role_var, value="Student", font=("Times New Roman", 14)).grid(row=4, column=0, padx=10, sticky="e")
    ctk.CTkRadioButton(root, text="Teacher", variable=role_var, value="Teacher", font=("Times New Roman", 14)).grid(row=4, column=1, padx=10, sticky="w")
    ctk.CTkButton(root, text="Login", font=("Times New Roman", 20), fg_color="#03045E", text_color="white", command=login).grid(row=5, column=0, columnspan=2, pady=30, sticky="nsew")

# Helper function to clear the current window
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# Main program
if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Light or Dark mode
    ctk.set_default_color_theme("blue")  # Default theme

    root = ctk.CTk()
    root.geometry("1000x600")
    root.title("CustomTkinter Responsive Example")
    root.config(bg="#CAF0F8")


    open_login_page()
# Configure grid layout for responsiveness
    root.grid_rowconfigure(0, weight=1)  # Header row
    root.grid_rowconfigure(1, weight=4)  # Content row
    root.grid_rowconfigure(2, weight=1) 
 

                                               # Footer row
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)







# Make both columns expandable
 
    root.mainloop()
