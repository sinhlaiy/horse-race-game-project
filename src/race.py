import turtle
import tkinter as tk
from horses.horses import create_horses, Horse
from config.configure import Config
#Attribution: utilized ChatGPT for debugging purposes and proofreading
#was able to catch syntax and spelling errors that would have caused the project to crash
#defines how the race starts and ends; draws the finish line and loads all objects needed
class Race:
    def __init__(self, gui):
        self.gui = gui
        self.draw_finish()
        Horse.load_horses(gui.screen)
        self.horses = create_horses(gui.screen)
        self.race_on = False

    def draw_finish(self):
        line = turtle.RawTurtle(self.gui.screen)
        line.hideturtle()
        line.penup()
        line.pensize(10)
        line.speed(0)

        x = 550
        line.goto(x, -400)
        line.color("black", "white")
        line.begin_fill()
        line.pendown()
        line.goto(x, 400)
        line.goto(600,400)
        line.goto(600, -400)
        line.goto(x, -400)
        line.end_fill()

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
                #print("horse has stopped") == was used to make sure this ran
                self.race_on = False
                return
            
        #print("made it here") == was used to track how far code will go without crashing
        self.gui.root.after(100, self.race_go)

    def reset_race(self):
        self.race_on = False
        for horse in self.horses:
            horse.reset_horses()

        self.gui.screen.update()
    