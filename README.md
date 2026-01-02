----------------------Hogwart project : The art of coding like a wizard----------------------

Title : hogwart adventure

desrcription : 
A text adventure game that takes players through various chapters of magical experiences at Hogwarts School.
Players create their character, get sorted into a house, learn spells, and participate in Quidditch matches.
The goal is to make your caracter's house win by making the good choise throughout the adventure.

contributors :
MOLLIERE Sacha
RAZAFINDRABE Jery

instalation :

python required

Usage :

Start the adventure by running the main.py
folow the given instruction by providing acceptable answer to the program
for exemple when you will be asked to press "enter" to continue the interaction you will press "enter" when you are finished reading.
An other exemple is when asked to make a choice you'l have to responde with the number corresponding to your answer 


Key Features :

Interactive character creation

House sorting ceremony

Spell learning and casting system

Quidditch match simulation

House point system

Multiple chapters with branching narratives


Log book :


Project time line :

Week 1: creating the bases needed before the start of the chapters

Week 2: chapter 1 and 2

Week 3: chapter 3 and testing chapter 1 and 2

Week 4: chapter 4 and fixing issues

Week 5: Testing and bug fixes


Task distribution :


We assigned our self tasks and then take knowledge from the work of each other while pointing out errors that can be made 

input utils : we both were contribuing

Sacha : house , README , chapter2 and chapter 4

Jery : character , chapter 1 , chapter 3 , main and menu


Control, Testing, and Validation :

Input and Error Management:

We had this type of error :
"C:\Users\20241530\Documents\GitHub\Hogwarts\chapters\chapter_2.py", 
line 16, in meet_friends character["loyalty"] += 1 
                        "~~~~~~~~~^^^^^^^^^^^ 
KeyError: 'loyalty'"
It was due to the fact that keys had uppercase and lowercase letters. 

We also had this in the input utils:
"C:\Users\20241530\Documents\GitHub\Hogwarts\utils\input_utils.py", 
line 36, in ask_number if user_input[0] == '-': 
                        "~~~~~~~~~~^^^ IndexError: string index out of range
The variable checking if nothing was inputed was not in the if statement.


The program originally stopped when the user entered an unwanted or invalid input. 
This was fixed by adding input validation loops so the question is asked again until a correct answer is provided.

We had similar error during the project, but no big one.

Because predefined functions were not allowed, some built-in behaviors had to be recreated manually in the 
utils folder using loops and conditions.

Errors occurred when .items() was used on a list instead of a dictionary, causing the program to crash. 
This issue was resolved by replacing .items() with simple loops adapted to the data structure being used.


Testing Strategies:

Each chapter of the program was tested individually to save time and to make it easier to identify and 
fix errors without running the entire game.

We had to import json directly inside the chapter file because it didn't recognize it as a module, and also the path was messy.

Specific test cases were used, including valid inputs to verify normal program behavior and invalid inputs (such as empty input, non-numeric values, or incorrect choices) to ensure 
the program asks the user again instead of stopping.

Targeted tests were performed to address previously encountered issues, such as incorrect input handling,
misuse of data structures (lists vs dictionaries), and functions recreated without predefined methods.
