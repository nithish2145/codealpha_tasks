#HANGMAN GAME

import random

word_list = ["apple", "robot", "chair", "tiger", "brain"]
secret_word = random.choice(word_list)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

def display_word():
    return ' '.join([letter if letter in guessed_letters else '_' for letter in secret_word])
print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

while wrong_guesses < max_attempts:
    print("\nWord:", display_word())
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!")
        if all(letter in guessed_letters for letter in secret_word):
            print("\n🎉 You won! The word was:", secret_word)
            break
    else:
        wrong_guesses += 1
        print("❌ Incorrect guess. Remaining attempts:", max_attempts - wrong_guesses)

if wrong_guesses == max_attempts:
    print("\n💀 Game Over! The word was:", secret_word)
