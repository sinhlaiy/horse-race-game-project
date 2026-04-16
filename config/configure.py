#this is where the code for window will go
from instructions import instructions
import tkinter as tk
import turtle
import os
class Config:
    #set constants
    window_height = 800
    window_width = 1600

    instructions_bg_color = "white"
    instructions_font_color = "black"
    instructions_font_size = 18
    instructions_font = "times new roman"
    instructions_file = "instructions.txt"

    folder = r"C:\BCOG\BCOG200-final-project\images"
    image_paths = []
    for image in sorted(os.listdir(folder)):
        if image.endswith(".gif"):
            path = os.path.join(folder, image)
            turtle.register_shape(path)
            image_paths.append(path)

    def create_buttons(self):
        go_button = tk.Button(self.interface_frame, text = "Go", command = self.go)
        go_button.pack()

        quit_button = tk.Button(self.interface_frame, text = "Exit Game", command = self.root.quit)
        quit_button.pack()

#separate window class that uses Config
class Window:
    window = Window(config.width, config.height)