import turtle
import tkinter as tk
from horses.horses import create_horses, Horse
from config.configure import Config
from src.gui import Gui
from src.race import Race


def main():
    root = tk.Tk()
    gui = Gui(root)
    race = Race(gui)
    gui.setup(race)
    root.mainloop()
    



if __name__ == "__main__":
    main()