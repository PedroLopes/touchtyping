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

def resume_exercise(user, filename):
    with open(filename) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        for line in content:
            if line.find(user) != -1:
                return int(line.split(":")[1])

def save_progress(user,filename,exercise):
    with open(filename, "r+") as f:
        content = f.readlines()
        #content = [x.strip() for x in content]
        new_lines = []
        for line in content:
            index = line.find(user)
            if index != -1:
                line = str(line.split(":")[0])+":"+str(exercise)+"\n"
            new_lines.append(line)
        f.seek(0)
        f.write(''.join(new_lines))
        f.truncate()

def load_exercise(number):
    file = open("exercises/"+str(number)+".txt", "r") 
    words = file.read().split(" ")[:-1]
    words = insert_separator(words, " ")
    return words

def execute_exercise(words,typos):
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
    return typos

parser = argparse.ArgumentParser(description='touch typing training in python (use ESC to quit)')
parser.add_argument('--no-strict', action="store_true", dest="no_strict", default=False)
parser.add_argument('--exercise', action="store", dest="exercise", type=int)
parser.add_argument('--typos','-t', action="store", dest="max_typos", type=int, default=3)
parser.add_argument('--user','-u', action="store", dest="username")
parser.add_argument('--filename', '-f', action="store", dest="filename", default="study_sessions.log")
args = parser.parse_args()


if args.username != None:
    args.exercise = resume_exercise(args.username, args.filename)
    print("For user {}, will resume study at exercise no. {}".format(args.username,args.exercise))
if args.exercise != None:
    words = load_exercise(args.exercise)
else:
    words = ["default", "exercise:", "please", "use", "> python touchtyping.py", "--help"]

last_exercise = 3

while True:
    if args.exercise > last_exercise:
        break
    words = load_exercise(args.exercise)
    print(''.join(words))
    typos = 0
    typos = execute_exercise(words,typos)
    print('\nFinished with {} typos (max is {})'.format(typos,args.max_typos))
    if typos > args.max_typos and args.no_strict == False:
        print('Too many typos. Try again')
    else:
        args.exercise+=1
        save_progress(args.username,args.filename,args.exercise)
