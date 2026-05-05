import tkinter as tk
import turtle
from config.configure import Config

class Gui:
    def __init__(self, root):
        self.root = root
        # moving race down below to initialize_race()
        self.root.title("Sinh Lai's Horse Race")
        self.root.configure(bg="grey")
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side="top", fill="x")
        self.interface_frame = tk.Frame(root)
        self.interface_frame.pack()
        self.canvas = tk.Canvas(
            root,
            width=Config.window_width,
            height=Config.window_height
        )
        self.canvas.pack()
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("lightgreen")
        
    

    def setup(self, race):
        self.race = race
        self.create_buttons()

    def create_buttons(self):
        go_button = tk.Button(self.button_frame, width = 12, text = "GO", command = self.race.start_race, bg = "green")
        go_button.pack(side = "left", padx = 150)

        quit_button = tk.Button(self.button_frame, width= 12, text = "EXIT", command = self.root.quit, bg = "red")
        quit_button.pack(side = "right", padx = 150)

        play_again_button = tk.Button(self.button_frame, width = 12, text = "PLAY AGAIN", command = self.race.reset_race)
        play_again_button.pack()

    def show_instructions(self, instructions):
        self.instructions_text_label.configure(text=instructions)
        self.instructions_text_label.pack()
        self.instructions_text_label.pack_propagate(False)
        self.root.update()