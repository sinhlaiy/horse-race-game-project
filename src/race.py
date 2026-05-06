import turtle
import tkinter as tk
from horses.horses import create_horses, Horse
from config.configure import Config


class Race:
    def __init__(self, gui):
        self.gui = gui
        Horse.load_horses(gui.screen)
        self.horses = create_horses(gui.screen)
        self.race_on = False

    def start_race(self):
        self.race_on = True
        self.race_go()

    def race_go(self):
        if not self.race_on:
            return

        for horse in self.horses:
            horse.move_horse()
            if horse.stop():
                self.gui.result(horse.name)
                #print("horse has stopped")
                self.race_on = False
                return
            
        #print("made it here")
        self.gui.root.after(100, self.race_go)

    def reset_race(self):
        self.race_on = False
        for horse in self.horses:
            horse.reset_horses()

        self.gui.screen.update()
        #Horse.load_horses(self.screen)
        #self.horses = create_horses(self.screen)
    