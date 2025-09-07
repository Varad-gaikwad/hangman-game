import tkinter as tk
import random

word = ""
guessed_word = []
chances = 6

def start_game():
    global word, guessed_word, chances
    words_input = entry_words.get().strip()
    if not words_input:
        label_status.config(text="⚠️ Please enter some words first!")
        return

    words = words_input.split()
    word = random.choice(words).lower()
    guessed_word = ["_"] * len(word)
    chances = 6

    label_word.config(text=" ".join(guessed_word))
    label_chances.config(text=f"Chances left: {chances}")
    label_status.config(text="🎯 Game started! Guess a letter.")

def guess_letter():
    global word, guessed_word, chances
    guess = entry_guess.get().lower()
    entry_guess.delete(0, tk.END)

    if not guess or len(guess) != 1 or not guess.isalpha():
        label_status.config(text="⚠️ Enter a single alphabet letter.")
        return

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        label_status.config(text=f" Correct! '{guess}' is in the word.")
    else:
        chances -= 1
        label_status.config(text=f" Wrong guess! '{guess}' not in word.")

    label_word.config(text=" ".join(guessed_word))
    label_chances.config(text=f"Chances left: {chances}")

    # Win or lose
    if "_" not in guessed_word:
        label_status.config(text=f"You win! Word was: {word}")
    elif chances == 0:
        label_status.config(text=f"You lose! Word was: {word}")

# Tkinter window
root = tk.Tk()
root.title("Hangman Game")

# Input words
tk.Label(root, text="Enter words (space-separated):").pack()
entry_words = tk.Entry(root, width=40)
entry_words.pack()

tk.Button(root, text="Start Game", command=start_game).pack(pady=5)

# Word display
label_word = tk.Label(root, text="_ _ _ _", font=("Arial", 16))
label_word.pack(pady=10)

# Guess input
tk.Label(root, text="Enter a letter:").pack()
entry_guess = tk.Entry(root, width=5)
entry_guess.pack()

tk.Button(root, text="Guess", command=guess_letter).pack(pady=5)

# Status + chances
label_chances = tk.Label(root, text="Chances left: 6")
label_chances.pack()

label_status = tk.Label(root, text="Game not started yet.")
label_status.pack(pady=10)

root.mainloop()
