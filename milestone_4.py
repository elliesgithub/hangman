import random

# list of words to be chosen from
word_list = [ "Raspberry", "Strawberry", "Mango", "Passionfruit", "Orange" ]
# randomly selects a word from the word_list
word = random.choice(word_list)

#class name
class Hangman: 
    """ 
    This class is the hangman game.

    Attributes:
     word_list (list): A list of words which the random word is chosen from.
     num_lives (int): The number of lives the player has at the start of the game.
     word (str): The word to be guessed, picked randomly from the word_list.
     num_letters (int): The number of UNIQUE letters in the word that have not been guessed yet.
     word_guessed (list): A list of the letters of the word, with _ for each letter not yet guessed. 
     list_of_guesses (list): A list of the guesses that have already been tried. Set this to an empty list initially.
    """
   
    #class constructor
    def __init__ (self, word_list, num_lives=5):
        """ This function inititialises the attributes within the class"""
        
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.num_letters = len(self.word)
        self.word_guessed = ['_'] * len(self.word)
        self.list_of_guesses = []
        
    def check_guess(self,guess):
     """ This function checks if the user guess is in the random word chosen and updates users lives depdening on if they are correct or not  """
     guess = guess.lower()
     if guess in self.word:
      print(f"Good guess! '{guess}' is in the word.")
      for letter in range(len(self.word)):
        if self.word[letter] == guess:
         self.word_guessed[letter] = guess
        self.num_letters -= 1 
     else:
      self.num_lives -= 1
      print(f"Sorry, '{guess}' is not in the word. Try again.")
      print(f"You have {self.num_lives} lives left.")
        
    
    def ask_for_input(self):
     """ 
     This asks the user for an input.

     If the input is not a single aplhabet leter or has already been guessed it will continue to run.
     It appends the list of guesses with each new valid input.
     """
     while True:
     # asks user for input 
      guess = input("Enter a single letter: ")
    
    # runs check_guess function and prints invalid if input is not a single alphabet letter
      if len(guess) != 1 or not guess.isalpha():
       print("Invalid letter. Please, enter a single alphabetical character.")
      elif guess in self.list_of_guesses:
       print("You already tried that letter!")
      else:
         #appends list of guesses to inclue previous user inputs
         self.list_of_guesses.append(guess)
         self.check_guess(guess)


hangman_instance = Hangman(word_list)
hangman_instance.ask_for_input()
