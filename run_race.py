import turtle
import tkinter as tk
from horses import horses
from config.configure import Config


class Race:
    def __init__(self, root):
        start_page = turtle.Screen()
        start_page.bgcolor("lightgreen")
        start_page.title("Horse Race Game")
        start_page.setup(width= Config.window_width, height= Config.window_height)

        self.root = root
        self.interface_frame = tk.Frame(root)
        self.interface_frame.pack()
        self.create_buttons()
        self.horses = horses.create_horses()

    
    def create_buttons(self):
        go_button = tk.Button(self.interface_frame, text = "Go", command = self.start_race)
        go_button.pack()

        quit_button = tk.Button(self.interface_frame, text = "Exit Game", command = self.root.quit)
        quit_button.pack()

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

    turtle.mainloop()

def main():
    root = tk.Tk()
    race = Race(root)
    root.mainloop()
    



if __name__ == "__main__":
    main()