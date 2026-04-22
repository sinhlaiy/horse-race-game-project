#this is where the code for window will go
import tkinter as tk
import turtle
import os
from horses.horses import Horse
from config import configure

class Config:
    #set constants
    window_height = 800
    window_width = 1600

    instructions_bg_color = "white"
    instructions_font_color = "black"
    instructions_font_size = 18
    instructions_font = "times new roman"
    instructions_file = "instructions.txt"

    #def __init__(self, root):
        #self.root = root
        #self.interface_frame = tk.Frame(root)
        #self.interface_frame.pack()
        #self.create_buttons()
    
    #def create_buttons(self):
        #3go_button = tk.Button(self.interface_frame, text = "Go", command = self.go)
        #go_button.pack()

        #quit_button = tk.Button(self.interface_frame, text = "Exit Game", command = self.root.quit)
        #quit_button.pack()

    #def go(self):
        #Horse.move_horse(self)
        

#separate window class that uses Config
#class Window:
    #window = Window(Config.width, Config.height)