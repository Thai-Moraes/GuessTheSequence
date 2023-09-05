import random
from colorama import just_fix_windows_console
just_fix_windows_console()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUM_LETTERS = 5
NUM_GUESSES = 10

color_green = "\033[92m"
color_yellow = "\33[33m"
color_default = "\033[0m"

def askForGuess():
    while True:
        guess = input('> ')

        if guess.isalpha() and len(guess) == NUM_LETTERS:
            return guess.upper()
        print('Por favor informe uma sequência com {} LETRAS'.format(NUM_LETTERS))

def wordle(guess, word):
    for i in range(len(guess)):
        if guess[i] == word[i]:
            print(color_green + guess[i], end="")

        elif guess[i] in word:
            print(color_yellow + guess[i], end="")

        else:
            print(color_default + guess[i], end="")
    print(color_default, end="\n")


print("Wordle, por Thai Moraes")
print(color_green + "VERDE: " + color_default + "Letra na sequência e na posição correta.")
print(color_yellow + "AMARELO: " + color_default + "Letra na sequência, mas na posição incorreta.")
print("BRANCO: " + "Letra não existe na sequência.")
print()
word = ''.join(random.choices(alphabet, k = NUM_LETTERS))

for i in range(NUM_GUESSES):
    print('Você possui {} tentativas. Tente adivinhar a sequência!'.format(NUM_GUESSES - i))

    guess = askForGuess()

    if guess == word:
        break
    else:
        wordle(guess, word)

if guess == word:
    print("Yay! Você adivinhou a sequência de letras! A sequência era", word)
else:
    print("Fim de jogo. A sequência de letras que eu estava pensando era", word)


