from os import listdir
from os.path import basename
from os.path import splitext
from Getch import getch
from sys import argv
from sys import exit
import argparse
from time import time

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
        new_lines = []
        for line in content:
            index = line.find(user)
            if index != -1:
                line = str(line.split(":")[0])+":"+str(exercise)+"\n"
            new_lines.append(line)
        f.seek(0)
        f.write(''.join(new_lines))
        f.truncate()

def find_last_exercise(folder):
    exercise_index = [-1]
    for filename in listdir(folder):
        if filename.endswith(".txt"):
            exercise_index.append(int(splitext(basename(filename))[0]))
        else:
            continue
    return max(exercise_index)

def load_exercise(number):
    file = open(args.exercise_folder + "/" + str(number)+".txt", "r") 
    words = file.read().split(" ")[:-1]
    words = insert_separator(words, " ")
    return words

def execute_exercise(words,typos,begin_time):
    first_char = True
    for word in words:
        char = ""
        i = 0
        while(i<len(word)):
            char = getch()
            if first_char:
                begin_time = time()
                first_char = False
            if char == '\x1b':
                exit()
            if char == word[i]:
                print(char, end='',flush=True)
                i+=1
            else:
                typos+=1
    return typos, begin_time

def wpm(time, words):
    word_length = len((''.join(words)).split(" "))
    words_per_m = word_length / time
    return words_per_m

parser = argparse.ArgumentParser(description='touch typing training in python (use ESC to quit)')
parser.add_argument('--no-strict', '-n', action="store_true", dest="no_strict", default=False)
parser.add_argument('--exercise', '-e', action="store", dest="exercise", type=int)
parser.add_argument('--typos','-t', action="store", dest="max_typos", type=int, default=3)
parser.add_argument('--wpm','-w', action="store", dest="min_wpm", type=int, default=20)
parser.add_argument('--user','-u', action="store", dest="username")
parser.add_argument('--filename', '-f', action="store", dest="filename", default="study_sessions.log")
parser.add_argument('--exercise-foldr', '-ef', action="store", dest="exercise_folder", default="exercises")
args = parser.parse_args()


if args.username != None:
    args.exercise = resume_exercise(args.username, args.filename)
    print("For user {}, will resume study at exercise no. {}".format(args.username,args.exercise))
if args.exercise != None:
    words = load_exercise(args.exercise)
else:
    words = ["default", "exercise:", "please", "use", "> python touchtyping.py", "--help"]

last_exercise = find_last_exercise(args.exercise_folder)

while True:
    if args.exercise > last_exercise:
        print("Congrats. That was the last exercise (you can always add more to the {} folder)".format(args.exercise_folder))
        break
    words = load_exercise(args.exercise)
    print(''.join(words))
    typos = 0
    begin_time = 0
    typos, begin_time = execute_exercise(words,typos,begin_time)
    end_time = time()
    #print("begin_time:{} end_time:{} sub:{}".format(begin_time, end_time, end_time - begin_time))
    final_time = (end_time - begin_time) / 60
    final_time = round(final_time, 2)
    words_per_minute = wpm(final_time, words)
    words_per_minute = round(words_per_minute, 2)
    print('\nFinished at {} wpm (min {}) with {} typos (max is {})'.format(words_per_minute,args.min_wpm,typos,args.max_typos))
    if typos > args.max_typos and args.no_strict == False:
        print('Too many typos. Try again')
    if words_per_minute < args.min_wpm and args.no_strict == False:
        print('Too slow. Try again')
    else:
        args.exercise+=1
        if args.username: 
                save_progress(args.username,args.filename,args.exercise)
