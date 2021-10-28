import string
import random

"""WELCOME TO THE PYTHON MYSTERY WORD GAME! A word is randomly selected from
a read-in text file and the user has to submit letters in order to correctly
guess the word. The word is stored in a list, there is also a list of blanks
which displays and updates based on correct guesses, and there is a third
list which stores guessed letters. The user gets 8 guesses."""

STOP_WORDS = [
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "he",
    "i",
    "in",
    "is",
    "it",
    "its",
    "of",
    "on",
    "that",
    "the",
    "to",
    "were",
    "will",
    "with",
]

def mystery_word_game(file):

    """This function first calls generate_random_word which generates a random word from words.txt.
    It then generates a list full of blanks (blanks_list) which matches the length of the random
    word, a blank list for guessed letters to be stored, and a counter for incorrect guesses."""

        # The user is welcomed to the game.
    print(
        "WELCOME TO THE MYSTERY WORD GAME! A word has randomly been selected from the English language and it is your job to guess what it is!"
    )
    print("Each randomly selected word is in all lower-case.")
    print("At any time, type QUIT to exit.")
    
    user_quit = False

    difficulty = difficulty_selection()
    
    mystery_word_letter_list = list(generate_random_word(file, difficulty))
    blanks_list = ["_" for letter in mystery_word_letter_list]
    guessed_letter_list = []
    incorrect_correct_guess_counter = 0

    # The user is prompted to make a guess. The prompts will continue to come so long as the incorrect_correct_guess_counter
    # is less than 8 or there are still "_" characters in the blanks_list.

    while (
        incorrect_correct_guess_counter < 8
        and "_" in blanks_list
        and user_quit is False
    ):
        guess = input("Please make a guess: ")
        if guess == "QUIT":
            user_quit = True
        # This checks to see if the user input was a letter.
        elif (
            len(guess) != 1
            or guess in string.punctuation
            or guess in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        ):
            print("Ooooooh... I'm so sorry that was not a letter.")
        else:
            # If the user guessed a letter correctly, the blanks list is updated with that letter at corresponding
            # indices.
            if guess.isupper() == True:
                print("Please submit a letter in lower-case.")
            elif guess in mystery_word_letter_list:
                if guess not in guessed_letter_list:
                    for idx in range(len(mystery_word_letter_list)):
                        if mystery_word_letter_list[idx] == guess:
                            blanks_list[idx] = guess
                    guessed_letter_list.append(guess)
                    # The user gets information on how their guessing is going.
                    print(
                        f"Nice Work! You guessed correctly! Here's what you know about the word so far: {blanks_list}"
                    )
                    print(f"Here are the letters you've so far: {guessed_letter_list}")
                else:
                    print("I'm sorry, you've guessed that letter already.")
            else:
                if guess not in guessed_letter_list:
                    guessed_letter_list.append(guess)
                    print(
                        f"Shucks! Not in the word! Here's what you know about the word so far: {blanks_list}"
                    )
                    print(
                        f"Here are the letters you've guessed so far: {guessed_letter_list}"
                    )
                    incorrect_correct_guess_counter += 1
                    print(
                        f"You have {8 - incorrect_correct_guess_counter} guesses left."
                    )
                else:
                    print("I'm sorry, you've guessed that letter already.")
    # These are the scenarios that take place when the game ends.
    if user_quit == True:
        print("Thanks for playing!")
    elif "_" not in blanks_list:
        print("Congratulations! You've guessed the mystery word!")
    else:
        print("Bummer!! You ran out of guesses!")

def difficulty_selection():
    """This function returns the difficulty the user has selected, or quits them out of the game
    or prompts them to provide input again."""
    
    selector_flag = True
    while selector_flag == True:
        difficulty_selector = input('Please select either HARD, NORMAL, or EASY difficulty: ')

        if difficulty_selector in ['QUIT', 'HARD', 'NORMAL', 'EASY']:
            selector_flag = False
            return difficulty_selector
        else:
            print("I'm sorry, I didn't recognize that input.")
            print("Please enter difficulty ('HARD', 'NORMAL', 'EASY') or 'QUIT'.")

def generate_random_word(text_file, difficulty):

    """This function opens the text file, removes all punctuation, converts it
    to lowercase, creates a list where each word is an index, and selects a random
    word from the list."""

    with open(file) as text:
        content = text.read()
        formatted_content = content.replace(string.punctuation, "")
        word_list = (
            formatted_content.replace("-", " ")
            .replace("—", " ")
            .replace(".", "")
            .replace(",", "")
            .replace(":", "")
            .replace("'", "")
            .replace('"', "")
            .replace("-\n", "")
            .lower()
            .split()
        )

    if difficulty == 'QUIT':
        print("Thanks for playing!")
        quit()
    elif difficulty == 'EASY':
        easy_list = []
        for word in word_list:
            if len(word) > 3 and len(word) < 6:
                easy_list.append(word)
        return random.choice(easy_list)
    elif difficulty == 'NORMAL':
        normal_list = []
        for word in word_list:
            if len(word) >= 6 and len(word) <= 8:
                normal_list.append(word)
        return random.choice(normal_list)
    elif difficulty == 'HARD':
        hard_list = []
        for word in word_list:
            if len(word) > 8:
                hard_list.append(word)
        return random.choice(hard_list)

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description="Get the word frequency in a text file."
    )
    parser.add_argument("file", help="file to read")
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        mystery_word_game(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
