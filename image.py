import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

window = tk.Tk()
window.title("image")
window.geometry("800x600")
photo =PhotoImage(file="online-dhopping.gif") 
label1 =ttk.Label(window,image=photo)
label1.pack()



window.mainloop()