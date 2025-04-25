import numpy as np                                                  #import numpy library
from random_word import RandomWords                                 #import random_word library

word_list = RandomWords()                                           #class for random word
random_word = word_list.get_random_word()                           #valuable random word

def display_word(word, correct_guesses):
    return ' '.join([letter if letter in correct_guesses else '_' for letter in word])      #function to display progression, blanks

def game_hangman(random_word):
    correct_guesses = set()
    attempts = 6

    while attempts > 0:
        print("\nWord:", display_word(random_word, correct_guesses))               #print 
        guess = input("Guess a letter: ").lower()                                           #type any letter

        if guess in random_word:                                                            #guess right add letter
            correct_guesses.add(guess)
            print("Correct!!!")
        else:
            attempts -= 1                                                                   #guess wrong decrease attempts number
            print(f"Incorrect!!! you have {attempts} attempts left")
        
        if all(letter in correct_guesses for letter in random_word):                        #guess all right before attempts = 0
            print("\nCongratulations! You've guessed the word:", random_word)
            return
    print(f"\ngame over: the word was {random_word}")                                       #guess wrong after attempts = 0

game_hangman(random_word)                                                                       #running function "game_hangman"