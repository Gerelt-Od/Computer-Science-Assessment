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
            
def letter_guesses():
    play_again = True
    while play_again:
        WORDLIST = ["apple",  "anaconda", "biology", "bankrupt",  "catastrophic", "candy", "dangerous", "discussions", "entrepreneur",  "equal", "football", "function", "ghetto", "galactophorous", "hangman", "honduras", "income", "infrastructure", "joules", "jargon", "kiwibank", "kazakhstan", "landlocked", "luxembourg", "manipulate", "managing", "netherlands", "net", "orange", "open", "paraguay", "pants", "quick", "qatar", "russia", "rwanda", "switzerland", "santa", "turkmenistan", "unicorn", "vietnam", "wallaby", "xylophone", "yemen", "zimbabwe"]
        chosen_word = random.choice(WORDLIST).lower()
        lettersGeussed = []
        word_geussed = []
        for letter in chosen_word:
            word_geussed.append("-")
    joined_word = None
    attempts = lives
    while (attempts != 0 and "-" in word_geussed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_word = "".join(word_geussed)
            print(joined_word)

            try:
                geussesOfPlayer = str(input("\nPlease select a letter between a to z" + "\n> ")).lower()
            except:
                print("That is not valid input. Please try again.")
                continue
            else:
                if not geussesOfPlayer.isalpha():
                    print("That is not a letter. Do it again")
                    continue
                elif geussesOfPlayer in guessed_letters:
                    print("You have already guessed that letter. Do it again.")
                    continue
                else:
                    pass

            lettersGeussed.append(geussesOfPlayer)

            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    word_guessed[letter] = player_guess # replace all letters in the chosen word that match the players guess

            if geussesOfPlayer not in chosen_word:
                attempts -= 1
            

            if "-" not in word_guessed: # no blanks remaining
                print(("\nCongratulations! {} was the word").format(chosen_word))
            else: # loop must have ended because attempts reached 0
                print(("\nUnlucky! The word was {}.").format(chosen_word))


            print("\nWould you like to play again?")

            response = input("> ").lower()
            if response not in ("yes", "y"):
                play_again = False

            

lifes()
letter_guesses()



#i = -1
#while i < 45:
 #   i = i + 1
  #  print(WORDLIST[i])
