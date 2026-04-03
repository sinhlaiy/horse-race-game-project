# horse-race-game-project
My first idea for my final project is to create a replication of the game "Horse Race". I am not sure if I want to replicate the card game or create an actual depiction of a horse race. However, I will be implementing a betting system and I will ask the player to bet on a horse. Then whichever horse wins, the player will get the money back and will be given the option to play again or to exit. This will be a gambling-ish game.

My first function will open the game and set up the horses with their colors, names, numbers, etc.
  This function will need to open the game and read a file that contains the information for the horses. So I might be utilizing a text file for this function.
My second function will handle the player side of the game, like starting the game.
  In this function I will ask the player to choose a horse and to bet money. Then I will start the race.
My third function includes what happens when the horse wins.
  It will basically code for a screen that shows the horse that won, the time, and the money won. Yes.

# What is this game?
This will be an iteration of the horse race game. Players will be allotted $500 to use to bet on a horse, with the starting bet being $25. If the horse wins, the player gets double the amount that was betted. If the horse loses, the player just loses the money that they bet.

The functions involved in this game include: 
moving each horse (each have their own function) 
the initialization of the game by the player (press 'go')
stopping the race when a horse reaches the end
taking/giving money

Someone would use this program so that they can gamble without actually losing any money (yay!).
Data will be collected based off how much a player bets on a horse and its relationship with the outcome of the previous race.

# Testing
Individuals can test this operation by playing one round. If the game works as it is intended, the horses will stop by themselves, the money will be withdrawn/deposited into the bank account, they would be able to change the amount of money they want to bet, and be able to exit from the game when they desire. If all of these parameters are met, the game works as it should. If one or more don't perform correctly, there would be errors in the code that prevent the game from working.
