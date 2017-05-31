#Gerelt-Od Zundui 2017
#Hangman assesment (91373)
#Explaining about the game rules lives and choices.

import random
nameOfUser = str(input("Hello user please eneter your name before you start playing hangman"))
print("Welcome", nameOfUser, " you have chosen to play hangman,"""
      """You have three choices 1, or 2 or 3,"""
      """ please choose one of these numbers to start the game."""
      """ You will have different lives for each different choices."""
      """ You will carry on until you have run out of lives.""")

#Making a module to choose how many lives the user has
def lifes():
    global lives
    lives = 0
    geuss = True
    while geuss != False:
        lenghtOfGame = int(input("Please choose a number between 1 to 3 to start the game"))
        if lenghtOfGame == 1:
            lives = 5
            print(lives)
            geuss = False
        elif lenghtOfGame == 2:
            lives = 10
            print(lives)
            geuss = False
        elif lenghtOfGame == 3:
            lives = 15
            print(lives)
            geuss = False
        else:
            print("Please choose a number between 1 to 3")
        return(lives)
            
            
def letter_guesses():
    NUMBER_OF_GAMES = ["1", "2", "3"]#list of accepted number of games.
    runGame = False
    gamesWanted = input("How many games do you want to play?")#This saves gamesWanted as the user's input.
    while (runGame == False):
        if gamesWanted in NUMBER_OF_GAMES:#This searchs to see if the number of games inputted is on the list of accepted inputs.
            runGame = True#This breaks the program out of this loop and allows the first game to be run.
        if gamesWanted not in NUMBER_OF_GAMES:#This searchs to see if the number of games inputted is not on the list of accepted inputs.
            print("pick a number between 1 and 3 and don't input a word")
            gamesWanted = input("How many games do you want to play?")#This saves gamesWanted as the user's input.
    WORDLIST = ["apple",  "anaconda", "biology", "bankrupt",  "catastrophic", "candy", "dangerous", "discussions", "entrepreneur",  "equal", "football", "function", "ghetto", "galactophorous", "hangman", "honduras", "income", "infrastructure", "joules", "jargon", "kiwibank", "kazakhstan", "landlocked", "luxembourg", "manipulate", "managing", "netherlands", "net", "orange", "open", "paraguay", "pants", "quick", "qatar", "russia", "rwanda", "switzerland", "santa", "turkmenistan", "unicorn", "vietnam", "wallaby", "xylophone", "yemen", "zimbabwe"]
    chosen_word = random.choice(WORDLIST).lower()
    lettersGeussed = []
    word_geussed = []
    for letter in chosen_word:
        word_geussed.append("-")
    else:
        joined_word = None
        print("Test")
        print(chosen_word)
        global lives
        while (lives != 0 and "-" in word_geussed):
                print(("\nYou have {} attempts remaining").format(lives))
                joined_word = "".join(word_geussed)
                print(joined_word)
                    

                try:
                    geussesOfPlayer = str(input("\nPlease select a letter between a to z" + "\n> ")).lower()
                except:
                    print("That is not valid input. Please try again.")
                else:
                    if not geussesOfPlayer.isalpha():
                        print("That is not a letter. Do it again")
                    elif geussesOfPlayer in lettersGeussed:
                        print("You have already guessed that letter. Do it again.")
                    else:
                        pass

                        lettersGeussed.append(geussesOfPlayer)

                    for letter in range(len(chosen_word)):
                        if geussesOfPlayer == chosen_word[letter]:
                            word_geussed[letter] = geussesOfPlayer # replace all letters in the chosen word that match the players guess

                    if geussesOfPlayer not in chosen_word:
                        lives = lives - 1
                            
            

                    if ("-") not in word_geussed: # no blanks remaining
                        print(("\nCongratulations! {} was the word").format(chosen_word))
                    if lives == 0: # loop must have ended because attempts reached 0
                        print(("\nUnlucky! The word was {}.").format(chosen_word))

                    if gamesWanted != NUMBER_OF_GAMES:
                        runGame = False
                    else gamesWanted != Number_OF_GAMES:
                        runGame = True
                    


                    

                        runGame = False

            

lifes()
letter_guesses()



#i = -1
#while i < 45:
 #   i = i + 1
  #  print(WORDLIST[i])
