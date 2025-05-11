import pygame  # For sound playback

def open_introduction_stometa_full_scren_video():
    # Ensure global variables are declared properly
    global video_running, video_paused, current_frame, cap, video_label, audio_channel

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
    ).grid(row=0, column=0, columnspan=3, pady=20, padx=20)

    # "QUIT" Button
    ctk.CTkButton(
        root,
        text="QUIT",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=10,
        command=open_login_page,
    ).grid(row=3, column=0, padx=20, sticky="w")

    ctk.CTkButton(
        root,
        text="PREVIOUS",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=10,
        width=15,
        command=open_introduction_stometa,
    ).grid(row=3, column=2, sticky="e", pady=10, padx=10)

    # "NEXT" Button
    ctk.CTkButton(
        root,
        text="NEXT",
        font=("Times New Roman", 22),
        fg_color="#00B4D8",
        text_color="white",
        corner_radius=10,
        command=open_apparatus_stometa,
    ).grid(row=3, column=3, sticky="w", pady=10, padx=20)

    # Video Properties
    video_path = "video.mp4"
    audio_path = "audio.mp3"  # Path to the extracted audio file
    cap = cv2.VideoCapture(video_path)
    video_running = False
    video_paused = False
    current_frame = 0

    # Initialize pygame for audio playback
    pygame.init()
    pygame.mixer.init()
    audio_channel = pygame.mixer.Sound(audio_path)

    # Functions for video control
    def play_video():
        """Play the video and audio."""
        global video_running, video_paused
        video_running = True
        video_paused = False
        pygame.mixer.Sound.play(audio_channel, loops=0)
        thread = threading.Thread(target=update_frame)
        thread.daemon = True
        thread.start()

    def pause_video():
        """Pause the video and audio."""
        global video_paused
        video_paused = True
        pygame.mixer.pause()

    def stop_video():
        """Stop the video and audio."""
        global video_running, video_paused, current_frame
        video_running = False
        video_paused = False
        current_frame = 0
        pygame.mixer.stop()
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
