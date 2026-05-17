import turtle
import random
import os
from pathlib import Path

#create horse objects
def create_horses(screen):
    horses = [
    Horse("Red", Horse.image_paths[2], -250, screen),
    Horse("Blue", Horse.image_paths[0], -125, screen),
    Horse("Orange", Horse.image_paths[1], 25, screen),
    Horse("Yellow", Horse.image_paths[3], 150, screen)]

    return horses

#This defines the Horse class with relevant functions like moving and stopping
#Attribution: used ChatGPT to find the best method to soft code the file path
#suggested Path from PathLib
class Horse:
    folder = Path(__file__).parent.parent / "images"
    image_paths = []
    @classmethod
    def load_horses(cls, screen):
        for image in sorted(os.listdir(cls.folder)):
            if image.endswith(".gif"):
                path = cls.folder / image
                screen.addshape(str(path))
                cls.image_paths.append(str(path))

    def __init__(self, name, shape, y_position, screen):
        self.name = name
        self.y_position = y_position
        self.turtle = turtle.RawTurtle(screen)
        self.turtle.shape(shape)
        self.turtle.penup()
        self.turtle.goto(-350, y_position)

    def reset_horses(self):
        self.turtle.penup()
        self.turtle.goto(-350, self.y_position)

    def move_horse(self):
        self.turtle.forward(random.randint(5,20))

    def stop(self):
        if self.turtle.xcor() >= 550:
            print(f"{self.name} wins!")
            return True
        return False