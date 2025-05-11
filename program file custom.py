import tkinter as tk
from tkinter import ttk, messagebox

from PIL import Image, ImageTk  # Import Pillow for image handling
import cv2
import customtkinter


# Function to handle login
def login():
    name = name_entry.get()
    roll_number = roll_entry.get()
    role = role_var.get()
    if not name or not roll_number or not role:
        
        open_language_selection()


    else:
        open_language_selection()










# Function to open the language selection page
def open_language_selection():
    clear_window()
    tk.Label(root, text="Select Your Language", font=("Times New Roman", 28, "bold"), width=20,bg="#0077b6", fg="white").pack(pady=50)
    tk.Button(root, text="English", font=("Times New Roman", 22), bg="#00B4D8", fg="white", width=15, command=open_class_selection).pack(pady=10)
    tk.Button(root, text="Urdu", font=("Times New Roman", 22), bg="#00B4D8", fg="white", width=15, command=lambda: messagebox.showinfo("Coming Soon", "Urdu is under development.")).pack(pady=10)
    tk.Button( root, text="BACK", font=("Times New Roman", 22), bg="#00B4D8", fg="white",width=15, command=open_login_page).pack( pady=30)  # Specify the position and siz
 




# Function to open the class selection page
def open_class_selection():
    clear_window()
    tk.Label(root, text="Select Your CLASS", font=("Times New Roman", 28, "bold"), width=20,bg="#0077b6", fg="white").pack(pady=50)
    tk.Button(root, text="CLASS 9", font=("Times New Roman", 18), bg="#00B4D8", fg="white", width=15, command=open_board_selection).pack(pady=10)
    tk.Button(root, text="CLASS 10", font=("Times New Roman", 18), bg="#00B4D8", fg="white", width=15, command=lambda: messagebox.showinfo("Coming Soon", " under development.")).pack(pady=10)
    tk.Button(root, text="CLASS 11", font=("Times New Roman", 18), bg="#00B4D8", fg="white", width=15, command=lambda: messagebox.showinfo("Coming Soon", " under development.")).pack(pady=10)
    tk.Button(root, text="CLASS 12", font=("Times New Roman", 18), bg="#00B4D8", fg="white", width=15, command=lambda: messagebox.showinfo("Coming Soon", " under development.")).pack(pady=10)
    tk.Button( root, text="BACK", font=("Times New Roman", 18), bg="#00B4D8", fg="white",width=15, command=open_language_selection).pack( pady=30)  # Specify the position and siz
    #tk.Button( root, text="QUIT", font=("Times New Roman", 18), bg="#00B4D8", fg="white",width=15, command=open_login_page).pack( pady=30)  # Specify the position and siz




    #tk.Label(root, text="Select Your Class", font=("Times New Roman", 16, "bold"), bg="#e6f7ff", fg="#333").pack(pady=20)
    #classes = ["Class 9", "Class 10", "Class 11", "Class 12"]
    #for c in classes:
       # tk.Button(root, text=c, font=("Times New Roman", 14), bg="#28a745", fg="white", width=15, command=lambda cl=c: open_experiment_selection(cl)).pack(pady=5)
    #tk.Button(root, text="Back", font=("Times New Roman", 12), bg="#d9534f", fg="white", command=open_language_selection).pack(pady=20)



def open_board_selection():
    clear_window()


    tk.Label(root, text="Select Your BOARD", font=("Times New Roman", 28, "bold"), width=20,bg="#0077b6", fg="white").pack(pady=50)
    tk.Button(root, text=" LAHORE BOARD ",font=("Times New Roman", 18), bg="#00B4D8", fg="white", width=15, command=open_topic_selection).pack(pady=10)
    tk.Button(root, text="KPK BOARD",font=("Times New Roman", 18), bg="#00B4D8", fg="white", width=15, command=lambda: messagebox.showinfo("Coming Soon", " under development.")).pack(pady=10)
    tk.Button(root, text="SINDH BOARD", font=("Times New Roman", 18), bg="#00B4D8", fg="white", width=15, command=lambda: messagebox.showinfo("Coming Soon", " under development.")).pack(pady=10)
    tk.Button(root, text="FEDRAL BOARD", font=("Times New Roman", 18), bg="#00B4D8", fg="white", width=15, command=lambda: messagebox.showinfo("Coming Soon", " under development.")).pack(pady=10)
    
    tk.Button(root, text="BACK", font=("Times New Roman", 18), bg="#00B4D8", fg="white",width=15, command=open_class_selection).pack( pady=30)  # Specify the position and siz
    #tk.Button( root, text="QUIT",font=("Times New Roman", 18), bg="#00B4D8", fg="white",width=15, command=open_login_page).pack( pady=30)  # Specify the position and siz




def open_topic_selection():
    clear_window()


    tk.Label(root, text="Select Your Topic", font=("Times New Roman", 28, "bold"), width=20,bg="#0077b6", fg="white").pack(pady=50)
    tk.Button(root, text=" Structure and Number of Stomata  ", font=("Times New Roman", 18), bg="#00B4D8", fg="white", command=open_experiment_selection).pack(pady=10)
    tk.Button(root, text="TOPIC 2", font=("Times New Roman", 18), bg="#00B4D8", fg="white", width=15, command=lambda: messagebox.showinfo("Coming Soon", " under development.")).pack(pady=10)
    tk.Button(root, text="TOPIC 3", font=("Times New Roman", 18), bg="#00B4D8", fg="white", width=15, command=lambda: messagebox.showinfo("Coming Soon", " under development.")).pack(pady=10)
    tk.Button(root, text="TOPIC 4", font=("Times New Roman", 18), bg="#00B4D8", fg="white", width=15, command=lambda: messagebox.showinfo("Coming Soon", " under development.")).pack(pady=10)
    
    tk.Button(root, text="BACK", font=("Times New Roman", 18), bg="#00B4D8", fg="white",width=15, command=open_board_selection).pack( pady=30)  # Specify the position and siz
    #tk.Button( root, text="QUIT", font=("Times New Roman", 22), bg="#00B4D8", fg="white",width=15, command=open_login_page).pack( pady=30)  # Specify the position and siz






## Function to open the experiment selection page
def open_experiment_selection():
    clear_window()


    tk.Label(root, text="Select Your EXPERIMENT", font=("Times New Roman", 28, "bold"), width=20,bg="#0077b6", fg="white").pack(pady=50)
    tk.Button(root, text=" Describe the Structure and Number of Stomata Present on the Epidermal Peel of a Leaf ", font=("Times New Roman", 18), bg="#00B4D8", fg="white", command=summary_of_stomata  ).pack(pady=10)
    tk.Button(root, text="EXPERIMENT 2", font=("Times New Roman", 18), bg="#00B4D8", fg="white", width=15, command=lambda: messagebox.showinfo("Coming Soon", " under development.")).pack(pady=10)
    tk.Button(root, text="EXPERIMENT 3", font=("Times New Roman", 18), bg="#00B4D8", fg="white", width=15, command=lambda: messagebox.showinfo("Coming Soon", " under development.")).pack(pady=10)
    tk.Button(root, text="EXPERIMENT 4", font=("Times New Roman", 18), bg="#00B4D8", fg="white", width=15, command=lambda: messagebox.showinfo("Coming Soon", " under development.")).pack(pady=10)
    
    tk.Button(root, text="BACK", font=("Times New Roman", 18), bg="#00B4D8", fg="white",width=15, command=open_topic_selection).pack( pady=30)  # Specify the position and siz
   # tk.Button( root, text="QUIT", font=("Times New Roman", 22), bg="#00B4D8", fg="white",width=15, command=open_login_page).pack( pady=30)  # Specify the position and siz
  




def summary_of_stomata():
    clear_window()



import tkinter as tk
from tkinter import messagebox
import customtkinter

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
    text="SUMMARY",
    font=("Times New Roman", 35),
    fg_color="#0077B6",  # Background color
    text_color="white",
    width=15,
      # Text color
    #corner_radius=8,                           # Rounded corner radius
       # Button height

)

summary_label.grid(row=0, column=0,sticky= "w",pady=20, padx=20)  # Stretch horizontally





# Paragraph Label
paragraph_text = (
    "1. INTRODUCTION\n\n"
    "2. APPARATUS\n\n"
    "3. PROCEDURE\n\n"
    "4. OBSERVATION\n\n"
    "5. RESULT\n"
)



paragraph_label = customtkinter.CTkLabel(
    root,
    text=paragraph_text,
    font=("Times New Roman", 24),
    fg_color="#90E0EF",  # Background color
    text_color="white",
    wraplength=700,  # Wrap text after 700 pixels
    justify="left",
    width=30,
    height=12

)
paragraph_label.grid(row=1, column=0, sticky="wnse", padx=25)

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







   
def introduction():
    clear_window()













def Apparatus():
    clear_window()

   













def procedure():
    clear_window()


















 
def microscopic_observation():
    clear_window()







   
def results():
    clear_window()
     


     







##tk.Label(root, text=f"Select Experiment for {selected_class}", font=("Arial", 16, "bold"), bg="#e6f7ff", fg="#333").pack(pady=20)
  #  experiments = {
   #     "Class 9": ["Experiment 1: Stomata Observation", "Experiment 2: Food Test"],
    #    "Class 10": ["Experiment 1: Dissection", "Experiment 2: Photosynthesis"],
     #   "Class 11": ["Experiment 1: Animal Cell Observation", "Experiment 2: Plant Cell Observation"],
      #  "Class 12": ["Experiment 1: DNA Extraction", "Experiment 2: Blood Group Testing"]
    
    #for exp in experiments.get(selected_class, []):
     #   tk.Button(root, text=exp, font=("Arial", 14), bg="#ffc107", fg="black", width=25, command=lambda e=exp: messagebox.showinfo("Experiment Selected", f"You selected: {e}")).pack(pady=5)
    #tk#.Button(root, text="Back", font=("Arial", 12), bg="#d9534f", fg="white", command=open_class_selection).pack(pady=20)


















# Function to return to the login page
def open_login_page():
    clear_window()
    global name_entry, roll_entry, role_var  # Define widgets locally
    tk.Label(root, text="Login Page", font=("Times New Roman", 28, "bold"), bg="#CAF0F8", fg="#333").pack(pady=35)
    tk.Label(root, text="Enter Your Name:", font=("Times New Roman", 14), bg="#CAF0F8", fg="#333").pack()
    name_entry = tk.Entry(root, font=("Times New Roman", 16))
    name_entry.pack(pady=10)
    tk.Label(root, text="Enter Your Roll Number:", font=("Times New Roman", 16), bg="#CAF0F8", fg="#333").pack()
    roll_entry = tk.Entry(root, font=("Times New Roman", 16))
    roll_entry.pack(pady=10)
    tk.Label(root, text="Are you a Student or Teacher?", font=("Times New Roman", 16), bg="#CAF0F8", fg="#333").pack()
    role_var = tk.StringVar()
    tk.Radiobutton(root, text="Student", variable=role_var, value="Student", font=("Times New Roman", 12), bg="#CAF0F8").pack()
    tk.Radiobutton(root, text="Teacher", variable=role_var, value="Teacher", font=("Times New Roman", 12), bg="#CAF0F8").pack()
    tk.Button(root, text="Login", font=("Times New Roman", 20), bg="#03045E", fg="white",width="15", height="1", command=login ).pack(pady=25)





# Helper function to clear the current window
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()




# Create main Tkinter window
root = customtkinter.CTk()
root.title("experiment program ")
root.geometry("1000x530")
root.config(bg="#CAF0F8")


# Initialize the root window
#root = customtkinter.CTk()
#root.title("Experiment Program")
#root.geometry("1000x530")
#root.config(bg="#CAF0F8")


# Configure grid layout for responsiveness

# Start with the login page
open_login_page()

# Run the Tkinter event loop
root.mainloop()                                      