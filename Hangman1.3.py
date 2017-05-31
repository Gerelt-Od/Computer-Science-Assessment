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
        # set up the game loop
           global WORDLIST
           WORDLIST = ["apple",  "anaconda", "biology", "bankrupt",  "catastrophic", "candy", "dangerous", "discussions", "entrepreneur",  "equal", "football", "function", "ghetto", "galactophorous", "hangman", "honduras", "income", "infrastructure", "joules", "jargon", "kiwibank", "kazakhstan", "landlocked", "luxembourg", "manipulate", "managing", "netherlands", "net", "orange", "open", "paraguay", "pants", "quick", "qatar", "russia", "rwanda", "switzerland", "santa", "turkmenistan", "unicorn", "vietnam", "wallaby", "xylophone", "yemen", "zimbabwe"]
           chosen_word = random.choice(WORDLIST).lower()
           global player_guess
           player_guess = 0 # will hold the players guess
           global geussed_letters
           guessed_letters = [] # a list of letters guessed so far
           global word_guessed
           word_guessed = []
           for letter in chosen_word:
               word_guessed.append("-") # create an unguessed, blank version of the word
               joined_word = 0 # joins the words in the list word_guessed
               print(WORDLIST)
               play_again = False

letter_guesses()



#i = -1
#while i < 45:
 #   i = i + 1
  #  print(WORDLIST[i])
