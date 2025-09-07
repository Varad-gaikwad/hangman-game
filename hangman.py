import random

wordsinput = input("Enter words separated by space: ")
words = wordsinput.split()

word = random.choice(words).lower()
guessed_word = ["_"] * len(word)
chances = 6

print("\n🎯 Welcome to Hangman!")
print("Word: ", " ".join(guessed_word))

while chances > 0 and "_" in guessed_word:
    guess = input("\nGuess a letter: ").lower()

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        chances =chances - 1

    print("Word: ", " ".join(guessed_word))
    print("Chances left:", chances)

if "_" not in guessed_word:
    print("\n You win! The word was:", word)
else:
    print("\n You lose! The word was:", word)
