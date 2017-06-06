#Gerelt-Od Zundui 2017
#Hangman assesment (91373)
#Explaining about the game rules lives and choices.

import random
nameOfUser = str(input("Hello user please eneter your name before you start playing hangman "))
print("Welcome", nameOfUser, " you have chosen to play hangman,"
       """You have three choices 1, or 2 or 3,"""
       """please choose one of these numbers to start the game."""
       """You will have different lives for each different choices."""
       """Choose 1 or 2 or 3 to choose how many games you want to play"""
       """ You will carry on until 3 games max""")

#Making a module to choose how many lives the user has
def lifes():
    global lives #to get my lives for my module of letter_guesses
    lives = 0 
    geuss = True
    
    while geuss != False: #start a while loop to ask the user amount of lives they want
        lenghtOfGame = int(input("Please choose a number between 1 to 3 to start the game ")) #asks the user for how many lives they want
        if lenghtOfGame == 1: #if they choose 1 lives will equal 5
            lives = 5
            print("You have {} attempts".format(lives))
            geuss = False
        elif lenghtOfGame == 2:
            lives = 10
            print("You have {} attempts".format(lives))#if they choose 2 lives will equal 10
            geuss = False
        elif lenghtOfGame == 3:
            lives = 15
            print("You have {} attempts".format(lives))#if they choose 3 lives will equal 15
            geuss = False
        else:
            print("Please choose a number between 1 to 3 ")
            lenghtOfGame = int(input("Please choose a number between 1 to 3 to start the game "))
            if lenghtOfGame == 1: #if they choose 1 lives will equal 5
                lives = 5
                print("You have {} attempts".format(lives))
                geuss = False
            elif lenghtOfGame == 2:
                lives = 10
                print("You have {} attempts".format(lives))#if they choose 2 lives will equal 10
                geuss = False
            elif lenghtOfGame == 3:
                lives = 15
                print("You have {} attempts".format(lives))#if they choose 3 lives will equal 15
                geuss = False
            
            
            
def letter_guesses():
    global playedGames
    global gamesWanted
    global wrongGuesses
    while int(playedGames) != int(gamesWanted):#This creates new games until the wanted amount has been played.
        WORDLIST = ["apple",  "anaconda", "biology", "bankrupt",  "catastrophic", "candy", "dangerous", "discussions", "entrepreneur",  "equal", "football", "function", "ghetto", "galactophorous", "hangman", "honduras", "income", "infrastructure", "joules", "jargon", "kiwibank", "kazakhstan", "landlocked", "luxembourg", "manipulate", "managing", "netherlands", "net", "orange", "open", "paraguay", "pants", "quick", "qatar", "russia", "rwanda", "switzerland", "santa", "turkmenistan", "unicorn", "vietnam", "wallaby", "xylophone", "yemen", "zimbabwe", "fox", "carrot", "kumara", "clock", "alphabet", "chimpanze", "umbrella"]
        chosen_word = random.choice(WORDLIST).lower()#lower my chosen word to have the users guess easear
        lettersGeussed = []#make an empty list for guessed letters
        word_geussed = []#make an empty list for the word guessed
        for letter in chosen_word:
            word_geussed.append("-")#replaces each letter with -
        else:
            joined_word = None #this is to join the - in word_geussed
            global lives
            while (lives != 0 and "-" in word_geussed):#to loop until lives or - run out
                    print(("\nYou have guessed {} wrong ").format(wrongGuesses))#to print 
                    joined_word = "".join(word_geussed)
                    print(joined_word)
                    

                    try:
                        geussesOfPlayer = str(input("\nPlease select a letter between a to z" + "\n> ")).lower()
                    except:
                        print("That is not valid input. Please try again. ")
                    else:
                        if not geussesOfPlayer.isalpha():
                            print("That is not a letter. Do it again ")
                        elif geussesOfPlayer in lettersGeussed:
                            print("You have already guessed that letter. Do it again. ")
                        else:
                            pass

                            lettersGeussed.append(geussesOfPlayer)

                        for letter in range(len(chosen_word)):
                            if geussesOfPlayer == chosen_word[letter]:
                                word_geussed[letter] = geussesOfPlayer # replace all letters in the chosen word that match the players guess

                        if geussesOfPlayer not in chosen_word:
                            wrongGuesses += 1 

                        if ("-") not in word_geussed: # no blanks remaining
                            print(("\nCongratulations! {} was the word").format(chosen_word))
                            wrongGuesses -= wrongGuesses
                            playedGames = int(playedGames) + 1#This increases gamesPlayed by 1.
                            print("You have played", playedGames, "out of", gamesWanted, "games")#This tells the user how many games they have played.
                            break
                        if wrongGuesses == lives: # loop must have ended because attempts reached 0
                            print(("\nUnlucky! The word was {}.").format(chosen_word))
                            wrongGuesses -= lives
                            playedGames = int(playedGames) + 1#This increases gamesPlayed by 1.
                            print("You have played", playedGames, "out of", gamesWanted, "games")#This tells the user how many games they have played.
                            break
            
            if int(playedGames) == int(gamesWanted):#If the wanted number of games have been played, this causes the program to end.
                print("Thank You for playing") 



    
    

                       
lifes()
playedGames = 0
wrongGuesses = 0
NUMBER_OF_GAMES = ["1", "2", "3"]#list of accepted number of games.
runGame = False
gamesWanted = input("How many games do you want to play? ")#This saves gamesWanted as the user's input.
while (runGame == False):
        if gamesWanted in NUMBER_OF_GAMES:#This searchs to see if the number of games inputted is on the list of accepted inputs.
            runGame = True#This breaks the program out of this loop and allows the first game to be run.
        if gamesWanted not in NUMBER_OF_GAMES:#This searchs to see if the number of games inputted is not on the list of accepted inputs.
            print("pick a number between 1 and 3 and don't input a word ")
            gamesWanted = input("How many games do you want to play? ")#This saves gamesWanted as the user's input.
letter_guesses()



#i = -1
#while i < 45:
 #   i = i + 1
  #  print(WORDLIST[i])
