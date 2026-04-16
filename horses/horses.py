import turtle
import random
from config import configure

def create_horses(image_paths):
    horses = [
    Horse("Red", image_paths[2], -100),
    Horse("Blue", image_paths[0], -50),
    Horse("Orange", image_paths[1], 0),
    Horse("Yellow", image_paths[3], 50)]

    return horses

class Horse:
    def __init__(self, name, shape, y_position):
        self.name = name
        self.turtle = turtle.Turtle()
        self.turtle.shape(shape)
        self.turtle.penup()
        self.turtle.goto(-350, y_position)

    def move(self):
        self.turtle.forward(random.randint(1,10))

    def stop(self):
        if self.turtle.xcor() >= 350:
            print(f"{self.name} wins!")
            return True
        return False

folder = r"C:\BCOG\BCOG200-final-project\images"
image_paths = []
for image in sorted(os.listdir(folder)):
    if image.endswith(".gif"):
        path = os.path.join(folder, image)
        turtle.register_shape(path)
        image_paths.append(path)