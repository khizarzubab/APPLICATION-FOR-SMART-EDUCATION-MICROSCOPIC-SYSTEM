import cv2
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Initialize the customtkinter root window
root = ctk.CTk()
root.title("Image Comparison Interface")
root.geometry("1000x530")
root.config(bg="#CAF0F8")

# Function to calculate pixel-by-pixel similarity
def pixel_similarity(image1, image2):
    if image1.shape != image2.shape:
        return None
    diff = cv2.absdiff(image1, image2)
    total_pixels = image1.shape[0] * image1.shape[1]
    match_count = np.sum(diff == 0)
    similarity = (match_count / (total_pixels * 3)) * 100
    return similarity

# Function to calculate similarity and highlight differences
def compare_images(image1_path, image2):
    saved_image = cv2.imread(image1_path, cv2.IMREAD_COLOR)
    if saved_image is None:
        messagebox.showerror("Error", "Saved image not found.")
        return None, None, None, None, None

    image2_resized = cv2.resize(image2, (saved_image.shape[1], saved_image.shape[0]))
    gray1 = cv2.cvtColor(saved_image, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2_resized, cv2.COLOR_BGR2GRAY)
    ssim_score, diff = compare_ssim(gray1, gray2, full=True)
    diff = (diff * 255).astype("uint8")
    pixel_sim = pixel_similarity(saved_image, image2_resized)

    thresh = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    result_image = saved_image.copy()
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(result_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    return ssim_score * 100, pixel_sim, saved_image, image2_resized, result_image

# Function to capture an image from the camera and compare it
def capture_and_compare():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not access the camera.")
        return

    ret, frame = cap.read()
    if not ret:
        messagebox.showerror("Error", "Failed to capture image.")
        return

    # Show the captured frame to the user
    cv2.imshow("Captured Frame", frame)
    response = messagebox.askyesno("Confirm Capture", "Do you want to proceed with this captured image?")
    cv2.destroyWindow("Captured Frame")

    if not response:
        cap.release()
        return

    cap.release()
    saved_image_path = filedialog.askopenfilename(
        title="Select the saved image to compare",
        filetypes=(("Image Files", "*.jpg;*.jpeg;*.png"), ("All Files", "*.*")),
    )
    if not saved_image_path:
        return

    ssim_similarity, pixel_similarity, saved_image, captured_image, result_image = compare_images(saved_image_path, frame)
    if ssim_similarity is None:
        return

    saved_image_tk = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(saved_image, cv2.COLOR_BGR2RGB)))
    captured_image_tk = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(captured_image, cv2.COLOR_BGR2RGB)))
    result_image_tk = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)))

    saved_image_label.configure(image=saved_image_tk)
    saved_image_label.image = saved_image_tk
    captured_image_label.configure(image=captured_image_tk)
    captured_image_label.image = captured_image_tk
    result_image_label.configure(image=result_image_tk)
    result_image_label.image = result_image_tk

    ssim_label.configure(text=f"SSIM Similarity: {ssim_similarity:.2f}%")
    pixel_label.configure(text=f"Pixel Similarity: {pixel_similarity:.2f}%")

# Grid configuration for layout responsiveness
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Header label
header_label = ctk.CTkLabel(
    root,
    text="OBSERVATION SIMILARITY INDEX",
    font=("Times New Roman", 35),
    fg_color="#0077B6",                
    text_color="white"
)
header_label.grid(row=0, column=0, columnspan=3, pady=10, sticky="w")

# Image labels
saved_image_label = ctk.CTkLabel(root, text="Saved Image")
saved_image_label.grid(row=1, column=0, padx=20, pady=20)

captured_image_label = ctk.CTkLabel(root, text="Captured Image")
captured_image_label.grid(row=1, column=1, padx=20, pady=20)

result_image_label = ctk.CTkLabel(root, text="Difference Highlighted")
result_image_label.grid(row=1, column=2, padx=20, pady=20)

# Footer buttons
quit_button = ctk.CTkButton(
    root,
    text="QUIT",
    font=("Times New Roman", 22),
    fg_color="#00B4D8",
    text_color="white",
    corner_radius=10,
    command=root.quit
)
quit_button.grid(row=4, column=0, padx=20, pady=10, sticky="w")

compare_button = ctk.CTkButton(
    root,
    text="Capture and Compare Images",
    font=("Times New Roman", 16),
    fg_color="#0077B6",
    text_color="white",
    command=capture_and_compare
)
compare_button.grid(row=3, column=1, pady=20)

# Similarity labels
ssim_label = ctk.CTkLabel(root, text="SSIM Similarity: N/A", font=("Times New Roman", 20),fg_color="#0077B6",
    text_color="white")
ssim_label.grid(row=3, column=0, pady=20)

pixel_label = ctk.CTkLabel(root, text="Pixel Similarity: N/A", fg_color="#0077B6",
    font=("Times New Roman", 20), text_color="white")
pixel_label.grid(row=3, column=2, pady=20)











# Function to capture an image from the camera and compare it
def capture_and_compare():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not access the camera.")
        return

    def capture_image():
        """Capture the frame and proceed with comparison."""
        nonlocal frame
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", "Failed to capture image.")
            return
        
        # Release the camera and close the live feed
        cap.release()
        cv2.destroyWindow("Live Camera Feed")
        
        # Ask the user to select a saved image for comparison
        saved_image_path = filedialog.askopenfilename(
            title="Select the saved image to compare",
            filetypes=(("Image Files", "*.jpg;*.jpeg;*.png"), ("All Files", "*.*")),
        )
        if not saved_image_path:
            return
        
        # Perform comparison
        ssim_similarity, pixel_similarity, saved_image, captured_image, result_image = compare_images(saved_image_path, frame)
        if ssim_similarity is None:
            return

        # Update UI with results
        saved_image_tk = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(saved_image, cv2.COLOR_BGR2RGB)))
        captured_image_tk = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(captured_image, cv2.COLOR_BGR2RGB)))
        result_image_tk = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)))

        saved_image_label.configure(image=saved_image_tk)
        saved_image_label.image = saved_image_tk
        captured_image_label.configure(image=captured_image_tk)
        captured_image_label.image = captured_image_tk
        result_image_label.configure(image=result_image_tk)
        result_image_label.image = result_image_tk

        ssim_label.configure(text=f"SSIM Similarity: {ssim_similarity:.2f}%")
        pixel_label.configure(text=f"Pixel Similarity: {pixel_similarity:.2f}%")
    
    # Show live feed in a new window
    while True:
        ret, frame = cap.read()
        if not ret:
            messagebox.showerror("Error", "Failed to access the camera feed.")
            break

        # Display the live feed
        cv2.imshow("Live Camera Feed", frame)

        # Wait for the user to press 'c' to capture or 'q' to quit
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):  # Capture the image
            capture_image()
            break
        elif key == ord('q'):  # Quit without capturing
            cap.release()
            cv2.destroyWindow("Live Camera Feed")
            break

# Run the customtkinter event loop
root.mainloop()
