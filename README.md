# horse-race-game-project
My first idea for my final project is to create a replication of the game "Horse Race". This will be a depiction of an actual horse race, with horse image objects. I will be implementing a betting system and I will ask the player to bet on a horse. Then whichever horse wins, the player will get the money back and will be given the option to play again or to exit. This will be a gambling game.

My first function will open the game and set up the horses with their colors, names, numbers, etc.
  This function will need to open the game and read a file that contains the information for the horses. So I might be utilizing a text file for this function.
My second function will handle the player side of the game, like starting the game.
  In this function I will ask the player to choose a horse and to bet money. Then pressing the "GO" button will start the race at their own choice.
My third function includes what happens when the horse wins.
  It will basically code for a screen that shows the horse that won and the money won/lost in the account. The race will stop at the finish line and a print statement will be in the terminal that states which horse won.

# What is this game?
This will be an iteration of the horse race game. Players will be allotted $500 to use to bet on a horse, with the starting bet being $25. If the horse wins, the player gets double the amount that was betted. If the horse loses, the player just loses the money that they bet.
All odds are random, each horse moves at random increments each time so no one horse has an advantage. This is the fun of the game.

The functions involved in this game include: 
- moving each horse (each have their own function) 
- the initialization of the game by the player (press 'go')
- stopping the race when a horse reaches the end
- taking/giving money

The organization of this program will be split up, since the horses will be they're own thing and the window another. This is so that the files used are not enormous. I will be taking inspo from the pygame version and also follow a similar set up to Lab 7 and Lab 8.

Someone would use this program so that they can gamble without actually losing any money (yay!).
Data could be collected based off how much a player bets on a horse and its relationship with the outcome of the previous race.

# Testing
Individuals can test this operation by playing one round. 
If the game works as it is intended:
- The horses will stop by themselves
- The money will be withdrawn/deposited into the bank account
- They would be able to change the amount of money they want to bet
- Be able to exit from the game when they desire
If all of these parameters are met, the game works as it should. 
If one or more don't perform correctly, there would be errors in the code at any of these points that prevent the game from working as intended.

# How to run the game
Please download the ZIP file onto your local storage and extract all files. Then, in your terminal, navigate to the extratced folder. To launch the game, type "uv run python run_race.py":
  - Use the appropriate buttons to bet, start the race, restart the race, and exit the game.
