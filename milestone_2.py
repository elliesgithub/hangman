import random 

#list of words to be chosen from
word_list = [ "Raspberry", "Strawberry", "Mango", "Passionfruit", "Orange" ]
# randomly selects a word from the word_list
word = random.choice(word_list)

#prompt for the user to enter a single letter of their choosing
guess = input("Enter a single letter:")

#check if the guess is a single letter from the alphabet
if len(guess) == 1 and guess.isalpha() :
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")