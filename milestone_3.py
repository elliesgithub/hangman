import random 

# list of words to be chosen from
word_list = [ "Raspberry", "Strawberry", "Mango", "Passionfruit", "Orange" ]
# randomly selects a word from the word_list
word = random.choice(word_list)

# check_guess function to check if user input is in random word selected 
def check_guess(guess):
    guess = guess.lower()
    
    # responses to whether or not letter is in word
    if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
    else:
            print(f"Sorry, '{guess}' is not in the word. Try again.")



def ask_for_input():
    while True:
     # asks user for input 
     guess = input("Enter a single letter: ")
    
    # runs check_guess function and prints invalid if input is not a single alphabet letter
     if len(guess) == 1 and guess.isalpha():
      check_guess(guess)
      break 
     else:
      print("Invalid letter. Please, enter a single alphabetical character.")

# calling function ask_for_input
ask_for_input()