import random

# list of words to be chosen from
word_list = [ "Raspberry", "Strawberry", "Mango", "Passionfruit", "Orange" ]
# randomly selects a word from the word_list
word = random.choice(word_list)

#class name
class Hangman: 
   
    #class constructor
    def __init__ (self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.num_letters = len(self.word)
        self.word_guessed = ['_'] * len(self.word)
        self.list_of_guesses = []
        
    def check_guess(self,guess):
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


Hangman(word_list).ask_for_input()
