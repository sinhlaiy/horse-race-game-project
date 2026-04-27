import turtle
import tkinter as tk
from horses.horses import create_horses, Horse
from config.configure import Config


class Race:
    def __init__(self, root):
        self.root = root
        self.root.title("Sinh Lai's Horse Race")
        self.root.configure(bg = "grey")
        self.interface_frame = tk.Frame(root)
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side="top", fill="x")
        self.interface_frame.pack()
        self.canvas = tk.Canvas(root, width=Config.window_width, height=Config.window_height)
        self.canvas.pack()

        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("lightgreen")
        self.create_buttons()
        Horse.load_horses(self.screen)
        self.horses = create_horses(self.screen)
        self.race_on = False

    
    def create_buttons(self):
        go_button = tk.Button(self.button_frame, width = 12, text = "GO", command = self.start_race, bg = "green")
        go_button.pack(side = "left", padx = 150)

        quit_button = tk.Button(self.button_frame, width= 12, text = "EXIT", command = self.root.quit, bg = "red")
        quit_button.pack(side = "right", padx = 150)

        play_again_button = tk.Button(self.button_frame, width = 12, text = "PLAY AGAIN", command = self.reset_race)
        play_again_button.pack()

    def show_instructions(self, instructions):
        self.instructions_text_label.configure(text=instructions)
        self.instructions_text_label.pack()
        self.instructions_text_label.pack_propagate(False)
        self.root.update()

    def start_race(self):
        self.race_on = True
        self.run_race()

    def run_race(self):
        if not self.race_on:
            return

        for horse in self.horses:
            horse.move_horse()
            if horse.stop():
                self.race_on = False
                return
            
        self.root.after(100, self.run_race)

    def reset_race(self):
        Horse.load_horses(self.screen)
        self.horses = create_horses(self.screen)


def main():
    root = tk.Tk()
    race = Race(root)
    root.mainloop()
    



if __name__ == "__main__":
    main()