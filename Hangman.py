import random

WORDS = ["first", "second", "third", "fourth", "fifth"]

#This function selects a random word from the WORDS list to be used as the secret word in the game.
def select_word():
    return random.choice(WORDS)

#This function displays the current state of the secret word, showing guessed letters and underscores for unguessed letters.
def display_word(secret_word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])


#This function displays the hangman figure based on the number of lives remaining. 
#The hangman is drawn in stages, with each incorrect guess adding a new part to the figure. 
#The function returns a string representation of the hangman that can be printed to the console.
def display_hangman(lives_remaining):
    parts = [
        "  _______",
        " |       |",
        " |       O" if lives_remaining < 6 else " |",
        " |      /|\\" if lives_remaining < 3
        else " |      /|" if lives_remaining < 4
        else " |       |" if lives_remaining < 5
        else " |",
        " |      / \\" if lives_remaining < 1
        else " |      /" if lives_remaining < 2
        else " |",
        " |",
        "_|_"
    ]
    return "\n".join(parts)

def display_lives(lives_remaining):
    if lives_remaining > 0:
        return f"Lives remaining: {"♥ " * lives_remaining}"
    else:
        return "No lives remaining!"

#This function contains the main game loop for Hangman. 
#It initializes the game state, including selecting a secret word, tracking guessed letters, and managing the number of lives remaining. 
#The player is prompted to guess letters, and the game provides feedback on their guesses, updating the display accordingly. 
#The game continues until the player either guesses the word correctly or runs out of lives.

def play_hangman():
    secret_word = select_word()
    guessed_letters = set()
    lives_remaining = 6

    while lives_remaining > 0:
        print(display_lives(lives_remaining))
        print(display_hangman(lives_remaining))
        print(display_word(secret_word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in secret_word.lower():
            guessed_letters.add(guess)
            if all(letter.lower() in guessed_letters for letter in secret_word):
                print(display_lives(lives_remaining))
                print(display_hangman(lives_remaining))
                print(display_word(secret_word, guessed_letters))
                print(f"Congratulations! You won with {lives_remaining} lives remaining!")
                print(f"The word was: {secret_word}")
                return
        else:
            lives_remaining -= 1
            print(f"Wrong guess!")

    print(display_lives(lives_remaining))
    print(display_hangman(lives_remaining))
    print(f"Game over! The word was {secret_word}.")

if __name__ == "__main__":
    play_hangman()