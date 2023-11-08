import random 

#list of words to be chosen from
word_list = [ "Raspberry", "Strawberry", "Mango", "Passionfruit", "Orange" ]
# randomly selects a word from the word_list
word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()
    
    if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
    else:
            print(f"Sorry, {guess} is not in the word. Try again.")



def ask_for_input():
    while True:
     guess = input("Enter a single letter: ")
    
     if len(guess) == 1 and guess.isalpha():
      check_guess(guess)
        
     else:
      print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()