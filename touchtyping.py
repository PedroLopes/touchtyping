from Getch import getch
from sys import argv
import argparse

def insert_separator(words, char):
    words_spaces = []
    for w in words:
        words_spaces.append(w)
        words_spaces.append(char)
    return words_spaces[:-1]

parser = argparse.ArgumentParser(description='touch typing training in python')
parser.add_argument('--strict', action="store_true", default=False)
parser.add_argument('--exercise', action="store", dest="exercise", type=int)
parser.add_argument('--study', action="store", dest="study")

vals = parser.parse_args()

if vals.exercise != None:
    print("exercises/"+str(vals.exercise)+".txt")
    file = open("exercises/"+str(vals.exercise)+".txt", "r") 
    words = file.read().split(" ")[:-1]
else:
    words = ["hello", "world", "this", "is", "a", "touch", "typing", "tutorial"]

words = insert_separator(words, " ")
print(''.join(words))

typos = 0
max_typos = 3

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
print('\nFinished with {} typos (max is {})'.format(typos,max_typos))
if vals.strict:
    if typos > max_typos:
        print('Too many typos. Try again')

