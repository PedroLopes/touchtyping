from Getch import getch
from sys import argv

def insert_separator(words, char):
    words_spaces = []
    for w in words:
        words_spaces.append(w)
        words_spaces.append(char)
    return words_spaces[:-1]

words = ["hello", "world", "this", "is", "a", "touch", "typing", "tutorial"]
words = insert_separator(words, " ")
print(''.join(words))

typos = 0
threshold = 3

for word in words:
    char = ""
    i = 0
    while(i<len(word)):
        char = getch()
        if char == word[i]:
            print(char, end='',flush=True)
            i+=1
        else:
            typos+=1

print('\nFinished with {} typos'.format(typos))

