import tkinter as tk
from tkinter import filedialog, ttk
import pygame
import cv2
import os

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player with Pygame")

        # Create a tkinter canvas for embedding the pygame surface
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        # Buttons for controls
        self.start_live_button = ttk.Button(root, text="Start Live Video", command=self.start_live_video)
        self.start_live_button.pack(side=tk.LEFT, padx=5)

        self.open_file_button = ttk.Button(root, text="Open Video File", command=self.open_video_file)
        self.open_file_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = ttk.Button(root, text="Stop Video", command=self.stop_video, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.quit_button = ttk.Button(root, text="Quit", command=self.close_app)
        self.quit_button.pack(side=tk.LEFT, padx=5)

        # Initialize pygame
        pygame.init()

        # Variables
        self.running = False
        self.cap = None
        self.pygame_surface = None
        self.file_video_mode = False

    def start_live_video(self):
        """Start live video from the webcam."""
        if not self.running:
            self.running = True
            self.file_video_mode = False
            self.stop_button.config(state=tk.NORMAL)
            self.start_live_button.config(state=tk.DISABLED)
            self.open_file_button.config(state=tk.DISABLED)

            # Set up environment for embedding pygame in tkinter
            os.environ['SDL_WINDOWID'] = str(self.canvas.winfo_id())
            os.environ['SDL_VIDEODRIVER'] = 'windib'

            # Create a pygame surface
            self.pygame_surface = pygame.display.set_mode((800, 450))

            # Start capturing video from the webcam
            self.cap = cv2.VideoCapture(0)

            # Run the video loop
            self.video_loop()

    def open_video_file(self):
        """Open a video file and play it."""
        video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")])
        if video_path:
            self.running = True
            self.file_video_mode = True
            self.stop_button.config(state=tk.NORMAL)
            self.start_live_button.config(state=tk.DISABLED)
            self.open_file_button.config(state=tk.DISABLED)

            # Set up environment for embedding pygame in tkinter
            os.environ['SDL_WINDOWID'] = str(self.canvas.winfo_id())
            os.environ['SDL_VIDEODRIVER'] = 'windib'

            # Create a pygame surface
            self.pygame_surface = pygame.display.set_mode((800, 600))

            # Open the video file
            self.cap = cv2.VideoCapture("video.mp4")

            # Run the video loop
            self.video_loop()

    def video_loop(self):
        """Display frames from live video or video file in real-time."""
        if self.running and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # Convert the frame from BGR (OpenCV) to RGB (Pygame)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Flip the frame horizontally if in live mode
                if not self.file_video_mode:
                    frame = cv2.flip(frame, 1)

                # Create a pygame surface from the frame
                frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
                self.pygame_surface.blit(frame_surface, (0, 0))

                # Update the pygame display
                pygame.display.update()
            else:
                # Stop playback if video file ends
                if self.file_video_mode:
                    self.stop_video()
                    return

            # Call this function again after 10ms
            self.root.after(10, self.video_loop)

    def stop_video(self):
        """Stop the live video or video file playback."""
        self.running = False
        self.stop_button.config(state=tk.DISABLED)
        self.start_live_button.config(state=tk.NORMAL)
        self.open_file_button.config(state=tk.NORMAL)

        # Release the video capture object
        if self.cap:
            self.cap.release()
            self.cap = None

        # Clear the pygame surface
        if self.pygame_surface:
            self.pygame_surface.fill((0, 0, 0))
            pygame.display.update()

    def close_app(self):
        """Close the application."""
        self.stop_video()
        pygame.quit()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)



    root.mainloop()
