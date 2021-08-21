import random
from HangmanArt import stages, logo
from HangmanWords import word_list

word = random.choice(word_list)
print(logo)

print("Welcome to Hangman!")
msg = []
for i in range(len(word)):
    msg.append("_")

lives = 6
wrongGuess = []
while lives != 0 and "".join(msg) != word:
    print(stages[lives])
    print("Incorrect Letters Guessed: " + "".join(wrongGuess))
    print("".join(msg))
    guess = input("Guess a letter: ").lower()

    for i in range(len(word)):
      if guess == word[i]:
        msg[i] = guess

    if guess not in word and guess not in wrongGuess:
        wrongGuess.append(guess)
        wrongGuess.append(" ")
        lives -= 1


if lives == 0:
    print("You Lost")
    print(f"The word was {word}")
else:
    print("You Won!")