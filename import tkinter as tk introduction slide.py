import tkinter as tk
from tkinter import messagebox
import customtkinter

from PIL import Image, ImageTk  # Import Pillow for image handling

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

                                               # Footer row
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)





# Header Button


summary_label= customtkinter.CTkLabel(
    root,
    text="INTRODUCTION",
    font=("Times New Roman", 35),
    fg_color="#0077B6",  # Background color
    text_color="white",
    width=15,
      # Text color
    corner_radius=4,                           # Rounded corner radius
       # Button height

)

summary_label.grid(row=0, column=0,sticky= "w",pady=20, padx=20)  # Stretch horizontally





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



paragraph_label = customtkinter.CTkLabel(
    root,
    text=paragraph_text,
    font=("Times New Roman", 18),
    fg_color="#90E0EF",  # Background color
    text_color="white",
    wraplength=500,  # Wrap text after 700 pixels
    justify="left",
   # width=30,
    #height=12

)
paragraph_label.grid(row=1, column=0,rowspan=2, sticky="wnse", padx=25)





# Add an image using Pillow
try:
    # Load image using Pillow (replace 'image.gif' with your image path)
    pil_image = Image.open("sample.png").resize((350, 350))  # Resize if needed
    image = ImageTk.PhotoImage(pil_image)

    # Image label
    image_label = tk.Label(root, image=image, bg="#CAF0F8")
    image_label.grid(row=1, column=1,columnspan=3,sticky="nswe", pady=10,padx=40)
except FileNotFoundError:
    # Display an error if the image file is not found
    error_label = tk.Label(
        root,
        text="Image not found!",
        font=("Arial", 16),
        fg="red",
        bg="#CAF0F8",
    )
    error_label.grid(row=1, column=1)


# Footer Buttons
    customtkinter.CTkButton(
    root,
    text="QUIT",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",  # Text color
    corner_radius=10
).grid(row=3, column=0, padx=20, sticky="w")


steps_label = customtkinter.CTkLabel(
    root,
    text="STEPS",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",
      # Text color
   corner_radius=4,  
      # Rounded corner radius    # Button height

)
steps_label.grid(row=0, column=3,pady=10, padx=20 )

next_button = customtkinter.CTkButton(
    root,
    text="NEXT",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",  # Text color
    corner_radius=10,
    width=15        # Rounded corner radiu
)
next_button.grid(row=3, column=3,sticky="w",pady=10,padx=20)

quit_button = customtkinter.CTkButton(
    root,
    text="PREVIOUS",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",  # Background color
    text_color="white",  # Text color
    corner_radius=10,
    width=15
)
quit_button.grid(row=3, column=2,sticky="e",pady=10,padx=10)

# Run the Tkinter event loop
root.mainloop()
