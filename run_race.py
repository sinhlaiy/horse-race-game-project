import turtle
from horses import create_horses
from config.configure import Configure

def main():
    start_page = turtle.Screen()
    start_page.bgcolor("lightgreen")
    start_page.title("Horse Race Game")
    start_page.setup(width= Configure.window_width, height= Configure.window_height)

    race = True
    horses = create_horses()
    while race:
        for horse in horses:
            horse.move()
            if horse.stop():
                race = False
                break

if __name__ == "__main__":
    main()