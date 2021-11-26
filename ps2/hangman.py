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
import typing

WORDLIST_FILENAME = "./ps2/words.txt"


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



def choose_word(wordlist: "list[str]"):
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


def is_word_guessed(secret_word: str, letters_guessed: "list[str]") -> bool:
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



def get_guessed_word(secret_word: str, letters_guessed: "list[str]") -> str:
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
      



def get_available_letters(letters_guessed: "list[str]") -> str:
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
  checked_letters: "list[str]" = []
  unique_letters_count = 0

  for letter in secret_word:
    if letter not in checked_letters:
      unique_letters_count += 1

    checked_letters.append(letter)
  
  return unique_letters_count
    
def guess_is_not_valid(guess: str, letters_guessed: "list[str]") -> bool:
  if len(guess) < 1:
    return True

  return not (guess in get_available_letters(letters_guessed))

def hangman(secret_word: str):
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
  letters_guessed: "list[str]" = []

  
  print("Welcome to the game Hangman!")
  print("I am thinking of a word that is " + str(len(secret_word)) + " characters long.")

  while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
    print("------------------------------")
    print("You have " + str(guesses_remaining) + " guesses left.")
    print("Available letters: " + get_available_letters(letters_guessed))

    new_guess = input("Try to guess a letter of my word:").lower()

    while guess_is_not_valid(new_guess, letters_guessed):
      warnings_remaining -= 1

      if new_guess in letters_guessed:
        print("You already tried that letter!")
      else:
        print("I think that is not one letter!")

      if warnings_remaining == 0:
        guesses_remaining -= 1
        warnings_remaining = 3
        print("This is the third time I warn you, so you have lost 1 guess!")
        if guesses_remaining < 1:
          print("And it was your last guess, so...")
          break
        
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



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
