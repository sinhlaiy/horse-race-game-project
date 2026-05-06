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
        #self.interface_frame = tk.Frame(root)
        #self.interface_frame.pack()
        self.canvas = tk.Canvas(
            root,
            width=Config.window_width,
            height=Config.window_height
        )
        self.canvas.pack()
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("lightgreen")
        self.betting = Betting()
        
    

    def setup(self, race):
        self.race = race
        self.create_buttons()

    def place_bet(self):
        try:
            amount = int(self.bet_entry.get())
        except ValueError:
            print("Invalid bet")
            return

        horse = self.horse_var.get()
        if amount > self.betting.balance:
            print("Not enough balance")
            return
        self.betting.place_bet(horse, amount)
        self.update_balance_display()
        print(f"Bet placed on {horse} for ${amount}")

    def create_buttons(self):
        go_button = tk.Button(self.button_frame, width = 12, text = "GO", command = self.race.start_race, bg = "green")
        go_button.pack(side = "left", padx = 150)

        quit_button = tk.Button(self.button_frame, width= 12, text = "EXIT", command = self.root.quit, bg = "red")
        quit_button.pack(side = "right", padx = 150)

        play_again_button = tk.Button(self.button_frame, width = 12, text = "PLAY AGAIN", command = self.race.reset_race)
        play_again_button.pack()

        #Betting
        self.balance_label = tk.Label(
            self.button_frame,
            text = f"Balance: ${self.betting.balance}",
            font = ("Arial", 12),
            bg = "light grey"
        )
        self.balance_label.pack()

        place_bet_button = tk.Button(self.button_frame, text= "PLACE BET", command = self.place_bet)
        place_bet_button.pack()

        bet_label = tk.Label(self.button_frame, text="Bet:")
        bet_label.pack(side="left", padx=5)
        self.horse_var = tk.StringVar(value="Red")

        horse_menu = tk.OptionMenu(
            self.button_frame,
            self.horse_var,
            "Red", "Blue", "Orange", "Yellow"
        )
        horse_menu.pack(side="left", padx= 50)

        self.bet_entry = tk.Entry(self.button_frame, width=10)
        self.bet_entry.pack(side="left", padx=10)
        self.bet_entry.insert(0, "50")

    def result(self, winner):
        won = self.betting.award(winner)

        if won:
            print("You won!")
        else:
            print("You lost!")

        self.update_balance_display()

    def update_balance_display(self):
        self.balance_label.config(text=f"Balance: ${self.betting.balance}")

    def show_instructions(self, instructions):
        self.instructions_text_label.configure(text=instructions)
        self.instructions_text_label.pack()
        self.instructions_text_label.pack_propagate(False)
        self.root.update()


class Betting:
    def __init__(self):
        self.balance = 500
        self.selected_horse = None
        self.bet_amount = 0

    def place_bet(self, horse, amount):
        self.selected_horse = horse
        self.bet_amount = amount
        self.balance -= amount 

    def award(self, winner):
        if winner == self.selected_horse:
            winnings = self.bet_amount * 2
            self.balance += winnings
            return True
        return False