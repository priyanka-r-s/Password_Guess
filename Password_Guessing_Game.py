import random

easy_word = ["apple", "banana", "train", "india", "monkey", "tiger",
    "chair", "table", "pen", "book", "dog", "cat", "ball"]

medium_word = ["python", "bottle", "money", "laptop", "mountain", "sky",
    "garden", "mobile", "window", "school", "camera", "forest"]

hard_word = ["guava", "diamond", "computer", "elephant", "berry", "coin",
    "strawberry", "pineapple", "watermelon", "microphone",
    "programming", "technology", "environment"]

print("Welcome to the Password Guessing Game!")
print("Choose the difficulty level: easy, medium or hard")

level = input("Enter difficulty: ").lower()

if level == "easy":
    secret = random.choice(easy_word)
elif level == "medium":
    secret = random.choice(medium_word)
elif level == "hard":
    secret = random.choice(hard_word)
else:
    print("Invalid choice. Defaulting to EASY level.")
    secret = random.choice(easy_word)

attempts = 0
print("\nGuess the secret password")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"\nCongratulations! You guessed it in {attempts} attempts.")
        break

    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += secret[i] + " "
        else:
            hint += "_ "

    print("Wrong guess")
    print("Hint:", hint)

print("Game Over")