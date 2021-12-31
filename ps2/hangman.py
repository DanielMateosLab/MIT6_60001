#!/usr/bin/env python3

# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
from typing import List

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist: List[str]):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word: str, letters_guessed: List[str]) -> bool:
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
        
    return True



def get_guessed_word(secret_word: str, letters_guessed: List[str]) -> str:
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""

    for letter in secret_word:
      if letter in letters_guessed:
        guessed_word += letter
      else:
        if len(guessed_word) > 0 and guessed_word[-1] == "_":
          guessed_word += " "

        guessed_word += "_"
    
    return guessed_word
      



def get_available_letters(letters_guessed: List[str]) -> str:
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = ""

    for letter in string.ascii_lowercase:
      if letter not in letters_guessed:
        available_letters += letter
    
    return available_letters

def get_unique_letters_of_secret_word(secret_word: str) -> int:
  checked_letters: List[str] = []
  unique_letters_count = 0

  for letter in secret_word:
    if letter not in checked_letters:
      unique_letters_count += 1

    checked_letters.append(letter)
  
  return unique_letters_count
    
def guess_is_not_valid(guess: str, letters_guessed: List[str]) -> bool:
  if len(guess) < 1:
    return True

  return not (guess in get_available_letters(letters_guessed))

def hangman(secret_word: str, with_hints: bool = False):
  '''
  secret_word: string, the secret word to guess.
  
  Starts up an interactive game of Hangman.
  
  * At the start of the game, let the user know how many 
    letters the secret_word contains and how many guesses s/he starts with.
    
  * The user should start with 6 guesses

  * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.
  
  * Ask the user to supply one guess per round. Remember to make
    sure that the user puts in a letter!
  
  * The user should receive feedback immediately after each guess 
    about whether their guess appears in the computer's word.

  * After each guess, you should display to the user the 
    partially guessed word so far.
  
  Follows the other limitations detailed in the problem write-up.
  '''
  guesses_remaining = 6
  warnings_remaining = 3
  letters_guessed: List[str] = []

  # Welcome the user
  print("Welcome to the game Hangman!")
  with_hints and \
    print("There are hints available! Type * as letter guess to get all the possibilities")
  print("I am thinking of a word that is " + str(len(secret_word)) + " characters long.")

  while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
    # Give the user info about game state in the current round
    print("------------------------------")
    print("You have " + str(guesses_remaining) + " guesses left.")
    print("Available letters: " + get_available_letters(letters_guessed))

    # Ask for a letter
    new_guess = input("Try to guess a letter of my word:").lower()

    # Show possible matches if hints are enabled and the user asks for it
    if with_hints and new_guess == "*":
      my_word = get_guessed_word(secret_word, letters_guessed)
      show_possible_matches(my_word, letters_guessed)
    else:
      # Validate user input
      while guess_is_not_valid(new_guess, letters_guessed):
        # Remove a warning
        warnings_remaining -= 1

        # Explain the user why the input is invalid
        if new_guess in letters_guessed:
          print("You already tried that letter!")
        else:
          print("I think that is not one letter!")

        # Remove a guess every three warnings
        if warnings_remaining == 0:
          guesses_remaining -= 1
          warnings_remaining = 3
          print("This is the third time I warn you, so you have lost 1 guess!")
          # End the game if the user loses his last guess
          if guesses_remaining < 1:
            print("And it was your last guess, so...")
            break
        
        # Tell the player his remaining warnings and ask for a new guess
        else: 
          print("Three warnings like this and you lose a guess. Currently: ", warnings_remaining)              
        new_guess = input("Give me a letter: ")
      
      letters_guessed.append(new_guess)

      if new_guess in secret_word:
        if is_word_guessed(secret_word, letters_guessed):
          print("You got it! My word was", secret_word + "!")
          print("Score: ", get_unique_letters_of_secret_word(secret_word) * guesses_remaining)
          print("--- THE END ---")
        else:
          print("Amazing, the letter was in my word!", get_guessed_word(secret_word, letters_guessed))
      else:
        print("Sorry! My word lacks that letter >:)", get_guessed_word(secret_word, letters_guessed))
        if new_guess in ["a", "e", "i", "o", "u"]:
          guesses_remaining -= 2
          print("Vowels not in my word remove two attempts!")
        else:
          guesses_remaining -= 1
      
      if guesses_remaining < 1:
        print("HAHAHA! This is the end, my word will be a secret forever!")
        print("--- GAME OVER ----")

      



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


# %%
def match_with_gaps(my_word: str, other_word: str, letters_guesed: List[str]) -> bool:
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word_parsed = my_word.replace(" ", "")

    if (len(my_word_parsed) != len(other_word)):
      return False
    
    for letterIndex in range(len(my_word_parsed)):
      my_word_letter = my_word_parsed[letterIndex]
      other_word_letter = other_word[letterIndex]

      if my_word_letter == "_":
        if other_word_letter in letters_guesed:
          return False
      elif my_word_letter != other_word_letter:
        return False

    return True


def show_possible_matches(my_word: str, letters_guesed: List[str]):
  '''
  my_word: string with _ characters, current guess of secret word
  returns: nothing, but should print out every word in wordlist that matches my_word
            Keep in mind that in hangman when a letter is guessed, all the positions
            at which that letter occurs in the secret word are revealed.
            Therefore, the hidden letter(_ ) cannot be one of the letters in the word
            that has already been revealed.
  '''
  possible_matches: List[str] = []

  for word in wordlist:
    if match_with_gaps(my_word, word, letters_guesed):
      possible_matches.append(word)
  
  print("Possible matches are:")
  for match in possible_matches:
    print(match, end=" ")

# %%

def hangman_with_hints(secret_word: str):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    hangman(secret_word, True)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word, True)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
