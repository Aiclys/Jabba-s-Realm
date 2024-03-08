import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from pygame import mixer
from PIL import *

class LoginScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.title("Login Screen")
        self.geometry("500x300")

        # Set background image
        bg_image = PhotoImage(file=r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\Background_stern.png")
        bg_label = tk.Label(self, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        # Add a yellow title
        title_label = ttk.Label(self, text="Jabba's Realm", font=("Arial", 24, "bold"), foreground="#ffcc00")
        title_label.pack(pady=10)

        # Create and add username input field
        self.username_input = ttk.Entry(self, font=("Arial", 12), width=20)
        self.username_input.pack(pady=5)

        # Create and add password input field
        self.password_input = ttk.Entry(self, font=("Arial", 12), width=20, show="*")
        self.password_input.pack(pady=5)

        # Create and add login button
        self.login_button = ttk.Button(self, text="Login", command=self.open_new_screen)
        self.login_button.pack(pady=10)

        # Play background music
        self.play_background_music()

    # Method to open the new screen
    def open_new_screen(self):
        self.new_screen = MainScreen()
        self.new_screen.attributes("-fullscreen", True)
        self.new_screen.mainloop()

    # Method to play background music
    def play_background_music(self):
        mixer.init()
        mixer.music.load(r"C:\Users\quent\OneDrive\Desktop\App_Programming\Audio\cantina.mp3")
        mixer.music.set_volume(0.3)
        mixer.music.play()


class MainScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.title("Main Screen")
        self.geometry("1920x1080")

        # Set background image
        bg_image = PhotoImage(file="background_image.png")
        bg_label = tk.Label(self, image=bg_image)
        bg_label.place(relwidth=1, relheight=1)

        # Create and add buttons
        button_names = ["Marketplace", "Jabba's Stocks", "Jabba's Hangout", "Jabba's Playground"]
        for name in button_names:
            button = ttk.Button(self, text=name, command=lambda n=name: self.button_clicked(n))
            button.pack(pady=10)
            button.config(width=20, height=2)

    # Method to handle button clicks
    def button_clicked(self, name):
        # Show corresponding placeholder image based on button clicked
        pass  # Placeholder for image

if __name__ == "__main__":
    login_screen = LoginScreen()
    login_screen.mainloop()
