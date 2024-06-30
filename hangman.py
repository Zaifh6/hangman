import random
word_list = ["apple",
    "house",
    "car",
    "dog",
    "cat",
    "happy",
    "sun",
    "tree",
    "book",
    "shoe",
    "bird",
    "chair",
    "ball",
    "flower",
    "smile",
    "cookie",
    "hat",
    "water",
    "moon",
    "key"]
print(""" _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \\\\ / _` | '_ \\\\ / _` | '_ ` _ \\\\ / _` | '_ \\\\
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\\\__,_|_| |_|\\\\__, |_| |_| |_|\\\\__,_|_| |_|
                    __/ |
                   |___/                       """)
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\\\  |
 / \\\\  |
      |
=========''']

lives = len(HANGMANPICS)
n = 0
chosen_word = word_list[random.randint(0,len(word_list)-1)]
print("Chosen Word: ",chosen_word)
display = []
for letter in chosen_word:
    display.append("_")
while n < lives:
    for position in range(len(chosen_word)):
        guess = input("Guess A Letter: ").lower()
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(HANGMANPICS[n])
            # print(display, end='')
            for i in display:
                print(i, end='')
            print()
            print("Correct Answer!! \\n You Have ", lives , " Left.")
        elif letter != guess:
            lives -= 1
            n += 1
            print("InCorrect Answer!! \\n You Have ", lives , " Left.")
            print(HANGMANPICS[n])

    print("Chosen Word: ",chosen_word)
    if "_" not in display:
        print("You Won!!")
        break
    elif n > lives:
        print("You Lost!!")
        break
