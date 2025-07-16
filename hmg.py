import random

# Step 1: Define a list of 5 words
word_list = ["apple", "grape", "peach", "mango", "lemon"]

# Step 2: Randomly choose one word
secret_word = random.choice(word_list)

# Step 3: Initialize variables
guessed_letters = []  # To store guessed letters
tries_left = 6         # Max incorrect guesses allowed
display_word = ["_"] * len(secret_word)  # To show progress

print(" Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You have {tries_left} incorrect guesses.\n")

# Step 4: Game loop
while tries_left > 0 and "_" in display_word:
    print("Word: ", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single alphabetical letter.\n")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter. Try again.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print(" Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        tries_left -= 1
        print(f" Wrong guess! Tries left: {tries_left}\n")

# Step 5: Result
if "_" not in display_word:
    print(" Congratulations! You guessed the word:", secret_word)
else:
    print(" Game Over! The correct word was:", secret_word)
