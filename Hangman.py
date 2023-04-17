# Import necessary libraries
from random import choice
from string import ascii_uppercase

# Import your custom dictionary (list of words) here
from dictionary import words

# -Hangman-

# Incorrect selections:
# ========
# ||/
# ||
# ||
# ||
# ||

# _ _ _ _ _


# Letters remaining: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# Enter a letter:
# Function to display hangman gallows based on the number of incorrect guesses
def display_gallows(num_incorrect):
  """A list that show difference progress"""
  hang = [
    "========\n"
    "||/    \n"
    "||      \n"
    "||      \n"
    "||       \n|| \n", "========\n"
    "||/   |\n"
    "||      \n"
    "||      \n"
    "||       \n|| \n", "========\n"
    "||/   |\n"
    "||    o \n"
    "||      \n"
    "||       \n|| \n", "========\n"
    "||/   |\n"
    "||    o \n"
    "||    | \n"
    "||       \n|| \n", "========\n"
    "||/   |\n"
    "||    o \n"
    "||    | \n"
    "||   /   \n|| \n", "========\n"
    "||/   |\n"
    "||   \o \n"
    "||    | \n"
    "||   / \ \n|| \n", "========\n"
    "||/   |\n"
    "||   \o/\n"
    "||    | \n"
    "||   / \ \n|| \n"
  ]
  print(hang[num_incorrect])


# Function to display the correct letters guessed so far
def display_correct(correct):
  # TODO: Implement this function
  print("Correct selections:")
  for letter in correct:
    print(letter, end=" ")
  print()


# Function to display the incorrect letters guessed so far
def display_incorrect(incorrect):
  # input type: list
  # ['A', 'B', 'C', .... ]
  # Sample
  # Incorrect selections: A B C D
  # TODO: Implement this function
  print("Incorrect selections:", end=" ")
  for letter in incorrect:
    print(letter, end=" ")
  print()


# Function to display the letters remaining to be guessed
def display_letters_remaining(incorrect, correct):
  # TODO: Implement this function
  # example: removing a letter using array.remove(element)
  # letter A, alphabet.remove(A)
  print("Letters remaining: ", end=" ")
  alphabet = list(ascii_uppercase)
  for letter in incorrect + correct:
    if letter in alphabet:
      alphabet.remove(letter)
  for letter in alphabet:
    print(letter, end=" ")
  print()


# Main game loop
def main():
  while True:
    # TODO: Choose a random word from a list of words
    word = choice(words)
    # TODO: Initialize the game state
    incorrect_guess = 0
    correct_guess = 0
    correct_letters = ['_'] * 5  # stores 5 blank letters represent the word
    incorrect_letters = list()  #shows incorrect guesses in a list
    # incorrect_letters = ['A', 'B', 'C']

    # -Hangman-

    # Incorrect selections:
    # ========
    # ||/
    # ||
    # ||
    # ||
    # ||

    # _ _ _ _ _
    print("-Hangman-")
    # Game loop
    while True:
      # TODO: Display the game status
      # c. Display the game status (hangman gallows, correct letters, incorrect letters, letters remaining).
      # incorrect_selection
      display_incorrect(incorrect_letters)
      # hangman gallows
      display_gallows(incorrect_guess)
      # correct letter
      display_correct(correct_letters)
      # Letters remaining: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
      display_letters_remaining(incorrect_letters, correct_letters)
      # TODO: Ask the user for a letter guess and handle input validation
      # Enter a letter: Ｅ
      while True:
        letter = input("Enter a letter: ").upper()
        alphabet = list(ascii_uppercase)
        if letter in alphabet:
          break
      if letter in incorrect_letters + correct_letters:
        print("The letter already guessed, please enter another letter")
      elif letter in word:
        correct_guess += 1
        for index in range(5):
          if letter == word[index]:
            correct_letters[index] = letter
      else:
        incorrect_guess += 1
        incorrect_letters.append(letter)
      if incorrect_guess == 5:
        print("YOUR LOSE")
        break
      if correct_guess == 5:
        print("YOUR WIN")
        break
      # TODO: Check the guess against the chosen word and update the game state accordingly
      # letter in incorrect_letters / correct letters # already guess the letter, so chose another letter
      # letter in word, number of guess += 1, correct_letter update
      # correct letters = ['_','_','_','_','_']
      # APPLE
      # P
      # ['A','_','_','_','_']
      # letter not in word but also not in incorrect letters, number of incorrect guess + 1, incorrect letter update
      # TODO: Continue the game loop until the player either wins or loses

      # TODO: Ask the user if they want to play again after each round
    play_again = input("Play again (Y/N)? ")
    if play_again.lower() != "y":
      break


if __name__ == "__main__":
  main()
