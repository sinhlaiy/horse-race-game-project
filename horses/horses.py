import turtle
import random
import os

def create_horses(screen):
    horses = [
    Horse("Red", Horse.image_paths[2], -200, screen),
    Horse("Blue", Horse.image_paths[0], -75, screen),
    Horse("Orange", Horse.image_paths[1], 75, screen),
    Horse("Yellow", Horse.image_paths[3], 200, screen)]

    return horses

class Horse:
    folder = r"C:\BCOG\BCOG200-final-project\images"
    image_paths = []
    @classmethod
    def load_horses(cls, screen):
        for image in sorted(os.listdir(cls.folder)):
            if image.endswith(".gif"):
                path = os.path.join(cls.folder, image)
                screen.addshape(path)
                cls.image_paths.append(path)

    def __init__(self, name, shape, y_position, screen):
        self.name = name
        self.turtle = turtle.RawTurtle(screen)
        self.turtle.shape(shape)
        self.turtle.penup()
        self.turtle.goto(-350, y_position)

    def move_horse(self):
        self.turtle.forward(random.randint(5,20))

    def stop(self):
        if self.turtle.xcor() >= 550:
            print(f"{self.name} wins!")
            return True
        return False