from Getch import getch
from sys import argv
from sys import exit
import argparse

def insert_separator(words, char):
    words_spaces = []
    for w in words:
        words_spaces.append(w)
        words_spaces.append(char)
    return words_spaces[:-1]

parser = argparse.ArgumentParser(description='touch typing training in python (use ESC to quit)')
parser.add_argument('--no-strict', action="store_true", dest="no_strict", default=False)
parser.add_argument('--exercise', action="store", dest="exercise", type=int)
parser.add_argument('--study', action="store", dest="study")

vals = parser.parse_args()

if vals.study != None:
    with open("study_sessions.log") as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        for line in content:
            if line.find(vals.study) != -1:
                vals.exercise=int(line.split(":")[1])
        print("Loaded username {} with exercise no. {}".format(vals.study,vals.exercise))
if vals.exercise != None:
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
        if char == '\x1b':
            exit()
        if char == word[i]:
            print(char, end='',flush=True)
            i+=1
        else:
            typos+=1
print('\nFinished with {} typos (max is {})'.format(typos,max_typos))
if typos > max_typos and vals.no_strict == True:
    print('Too many typos. Try again')

