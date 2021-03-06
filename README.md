# touchtyping
A basic touch typing trainer (for python3). Created for those moments in which ratatype is down or you are offline. 

![image](https://raw.githubusercontent.com/PedroLopes/touchtyping/master/images/demo.gif)

I realized later that this was loosely inspired after ratatype (any similarity is purely coincidental, but the default values for minimum wpm and maximum typos offer great learning potential).

## basic usage
* ``python3 touchtyping.py``: loads the welcome exercise.
* ``python3 touchtyping.py -u name``: loads the last exercise ``name``` was working on (saves sessions automatically when you advance)
* ``python3 touchtyping.py -e 1``: jumps to exercise number ``1``

## key mapping
Nothing special here. The only things to keep in mind are:

* **ESC**: restarts the current exercise (clearing typos and wpm)
* **ESC twice** (in less than 1 second): quits the application

## tracking your performance a.k.a. --user or -u
If you start the program with ``python3 touchtyping.py -u name`` you start as user ``name``. This will:
* automatically save your progress when you advance lessons
* save your last exercise
* display your score upon request: ``touchtyping.py -u name --score``

![image](https://raw.githubusercontent.com/PedroLopes/touchtyping/master/images/score.gif)
 
### more advanced usage
* ``python3 touchtyping.py --filename othername.txt"``: loads "othername.txt" as the save file for usernames and their exercises
* ``python3 touchtyping.py --typos 5``: changes the maximum allowed typos to ``5`` for advancing to next lesson (default is 3)
* ``python3 touchtyping.py --wpm 10``: changes the minimum allowed wpm to ``10`` for advancing to next lesson (default is 20)
 
## exercises and saving sessions

### exercise files
1. **To create new exercises**: simple save them as a numbered .txt file (e.g., 1.txt). Exercise files should only contain the string of characters that you wish to display.
2. **Example** of a ``1.txt`` file contents:
   ``this is a file for the touchtyping trainner``
3. **Put exercise files** in the ``exercises`` folder (default) or in your ``own-folder``, to read files from a custom folder use ``python3 touchtyping.py --exercise-folder own-folder`` instead.
   
### saving sessions for enabling continuous study
1. There is a directory named ``saved_state`` which saves the progress of ver user. 
2. Each user is a file, e.g., the progress of a user called ``pedro`` is in ``saved_state/pedro.txt``
3. To change this directory you can invoke it as such: ``python3 touchtyping.py --save-dir new_dir"``

#### To do and idea collection
* alias as command
* pip install
* Give hints, use a special symbol on exercise file to mark what is a hint. Then when hint modes are enabled or after the first failure, the user is presented with hint text. 
* colorful mode
* refresh shell mode (after every exercise or attempt)
* scores from all users?
* allow mode to redo exercises
