# touchtyping
A basic touch typing trainer (for python3). Created for those moments in which ratatype is down or you are offline. 

![image](https://raw.githubusercontent.com/PedroLopes/touchtyping/master/images/demo.gif)

I realized later that this was loosely inspired after ratatype (any similarity is purely coincidental, but the default values for minimum wpm and maximum typos offer great learning potential).

## basic usage
* ``python3 touchtyping.py``: loads the welcome exercise.
* ``python3 touchtyping.py -u name``: loads the last exercise "name" was working on (saves sessions automatically when you advance)
* ``python3 touchtyping.py -e 1``: loads exercise numer "1"

## key mapping
Nothing special here. The only things to keep in mind are:

* **ESC**: restarts the current exercise (clearing typos and wpm)
* **ESC twice** (in less than 1 second): quits the application

## advanced usage
* ``python3 touchtyping.py --filename othername.txt"``: loads "othername.txt" as the save file for usernames and their exercises
* ``python3 touchtyping.py --typos 10``: changes the maximum allowed typos to 10 for advancing to next lesson (default is 3)
* ``python3 touchtyping.py --wpm 10``: changes the minimum allowed wpm to 10 for advancing to next lesson (default is 20)

## exercises and saving sessions

### exercise files
1. **To create new exercises**: simple save them as a numbered .txt file (e.g., 1.txt). Exercise files should only contain the string of characters that you wish to display.
2. **Example** of a ``1.txt`` file contents:
   ``this is a file for the touchtyping trainner``
3. **Put exercise files** in the ``exercises`` folder (default) or in your ``own-folder``, to read files from a custom folder use ``python3 touchtyping.py --exercise-folder own-folder`` instead.
   
### saving sessions for enabling continuous study
1. There is a file ``study_sessions.log`` which saves your progress if you start the trainer in the **username mode** using ``python3 touchtyping.py -u name``. 
2. If your username is not on that file (first time you are starting with a new user name) it will be created.
3. If you wish to change this file (defaul is ``study_sessions.log``) you can invoke it as such:  ``python3 touchtyping.py --filename othername.txt"``

#### To do and idea collection
* alias as command
* pip install
* Give hints, use a special symbol on exercise file to mark what is a hint. Then when hint modes are enabled or after the first failure, the user is presented with hint text. 
* colorful mode
* refresh shell mode (after every exercise or attempt)
* save not only where you are but also best scores
  * load new "last" by keyword on user.txt
  * load all exercise scores into a table? or access file always? (prob ok)
  * print score
* allow mode to redo exercises
* if you typer super fast you can get division by zero, fix
