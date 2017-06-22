from os import listdir
from os.path import basename
from os.path import splitext
from Getch import getch
from sys import argv
from sys import exit
import argparse
from time import time
from time import asctime

separator="/"

def insert_separator(words, char):
    words_spaces = []
    for w in words:
        words_spaces.append(w)
        words_spaces.append(char)
    return words_spaces[:-1]

def resume_exercise(user, saved_state_dir):
    try:
        with open(saved_state_dir+"/"+user+".txt","a+") as f:
            f.seek(0)
            content = f.readlines()
            if not content:
                raise FileNotFoundError
            content = [x.strip() for x in content]
            line = content[0] 
            if line.find(user) != -1:
                return int(line.split(separator)[1])
            else :
                print("Error: cannot find user's ({}) last exercise to resume on log file {}. Log file is missing the first line?".format(user,filename))
                exit()
    except FileNotFoundError:
        print("User's {} logfile did not exist. Creating...".format(user,saved_state_dir))
        new_entry = []
        new_entry.append(user)
        new_entry.append(str(1))
        new_entry.append(asctime()+"\n")
        with open(saved_state_dir+"/"+user+".txt","a+") as f:
            f.seek(0)
            f.write(separator.join(new_entry))
        return 1

def save_progress(exercise,wpm_data,typos_data,user,saved_state_dir):
    print("Will save progress for {}".format(exercise))
    try:
        with open(saved_state_dir+"/"+user+".txt", "r+") as f:
            content = f.readlines()
            new_lines = []
            update_last = content[0].split(separator)
            update_last[1] = str(exercise+1)
            new_lines.append(separator.join(update_last))
            i = 1
            found = False
            #while i<len(content): #this was so wrong
            for line in content[1:]:
                segments = line.split(separator)
                print("trying to find {}".format(exercise))
                if segments[0] == str(exercise):
                    found =True
                    if wpm_data > float(segments[1]):
                        print("Updating previous score for exercise {}".format(exercise))
                        segments[1]=str(wpm_data)
                    #if typos_data < int(segments[2]):
                        segments[2] = str(typos_data)
                        segments[3] = str(asctime())+"\n"
                    line = separator.join(segments)
                new_lines.append(line)
            if not found:
                print("not found side...")
                line = separator.join([str(exercise),str(wpm_data),str(typos_data),str(asctime())+"\n"])
                new_lines.append(line)
            f.seek(0)
            print(new_lines)
            # would be neat to sort this alphabetical according to exercise number
            f.write(''.join(new_lines))
            f.truncate()
    except FileNotFoundError:
        print("Error: cannot save user's ({}) progress to log file {}. This file does not exist. Your last exercise was {}".format(user,filename, exercise))

def find_last_exercise(folder):
    exercise_index = [-1]
    for filename in listdir(folder):
        if filename.endswith(".txt"):
            exercise_index.append(int(splitext(basename(filename))[0]))
        else:
            continue
    return max(exercise_index)

def load_exercise(number):
    try:
        file = open(args.exercise_folder + "/" + str(number)+".txt", "r") 
        words = file.read().split(" ")#[:-1]
        words = insert_separator(words, " ")
        words[-1] = words[-1].strip()
        return words
    except FileNotFoundError:
        print("Error: cannot open exercise with filename {}.txt This file does not exist. Please make sure your exercises are named accordingly. Will attempt skipping to next exercise.".format(number))
        return -1

def execute_exercise(words,typos,begin_time):
    first_char = True
    escape_pressed_twice_interval = 1
    escape_pressed = 0
    j = 0
    while j<len(words):
        #print(words)
        word = words[j]
        #print("word is {} and j is {}".format(word,j))
        char = ""
        i = 0
        while(i<len(word)):
            #print(i)
            char = getch()
            if first_char:
                begin_time = time()
                first_char = False
            if char == '\x1b' and time() - escape_pressed > escape_pressed_twice_interval:
                print("\nRetry (press ESC twice to quit)\n{}".format(''.join(words)))
                typos=0
                first_char = True
                escape_pressed = time()
                j=-1
                break
            if char == '\x1b' and time() - escape_pressed < escape_pressed_twice_interval:
                print("\nExiting (user pressed ESC twice)")
                exit()
            if char == word[i]:
                print(char, end='',flush=True)
                i+=1
            else:
                typos+=1
        j+=1
    return typos, begin_time

def wpm(time, words):
    word_length = len((''.join(words)).split(" "))
    if time == 0:
        print("\nWarning: you were obscenely fast. Are you human?", end='')
        words_per_m = 9001
    else:
        words_per_m = word_length / time
    return words_per_m

def show_score(username, saved_state_dir):
    try:
        with open(saved_state_dir+"/"+username+".txt", "r") as f:
            content = f.readlines()
            print("{}'s score:".format(username))
            print("--------------------------------------------------------")
            print("exercise#\twpm\ttypos\tdate")
            for line in content[1:]:
                segments = line.split(separator)
                print("{}\t\t{}\t{}\t{}".format(segments[0],segments[1],segments[2],segments[3]),end='')
            print("--------------------------------------------------------")
    except FileNotFoundError:
        print("Error: cannot save user's ({}) progress to log file {}. This file does not exist. Your last exercise was {}".format(user,filename, exercise))

parser = argparse.ArgumentParser(description='touch typing trainer in python (use ESC to retry and ESC twice to quit)')
parser.add_argument('--no-strict', '-n', action="store_true", dest="no_strict", default=False)
parser.add_argument('--score', '-s', action="store_true", dest="show_score", default=False)
parser.add_argument('--exercise', '-e', action="store", dest="exercise", type=int)
parser.add_argument('--typos','-t', action="store", dest="max_typos", type=int, default=3)
parser.add_argument('--wpm','-w', action="store", dest="min_wpm", type=int, default=20)
parser.add_argument('--user','-u', action="store", dest="username")
parser.add_argument('--save-dir', '-sd', action="store", dest="saved_state_dir", default="saved_state")
parser.add_argument('--exercise-dir', '-ed', action="store", dest="exercise_folder", default="exercises")
args = parser.parse_args()


if args.username != None:
    exercise = resume_exercise(args.username, args.saved_state_dir)
    print("For user {}, will resume study at exercise no. {}".format(args.username,args.exercise))
    if args.show_score:
        show_score(args.username, args.saved_state_dir)
if args.exercise != None:
    exercise = args.exercise
    words = load_exercise(exercise)
elif args.username == None:
    exercise = 1

last_exercise = find_last_exercise(args.exercise_folder)


while True:
    if exercise > last_exercise:
        print("Congrats. That was the last exercise (you can always add more to the {} folder)".format(args.exercise_folder))
        break
    words = load_exercise(exercise)
    if words == -1:
        exercise+=1
        continue
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
    if typos >= args.max_typos and args.no_strict == False:
        print('Too many typos. Try again')
    elif words_per_minute < args.min_wpm and args.no_strict == False:
        print('Too slow. Try again')
    else:
        if args.username: 
                save_progress(exercise,words_per_minute,typos,args.username,args.saved_state_dir)
        exercise+=1
