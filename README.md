# sudoku
This is a fun project for playing around with the sudoku game.

# Howto run it
First create a text file with your sudoku matrix you want to resolve:
```
$ cat 001_sudoku.txt
# Sudoku
0,0,0,8,3,0,0,5,7
0,0,8,5,0,0,6,0,0
1,3,0,0,0,2,0,8,0
8,0,2,3,9,0,7,0,0
6,0,0,1,0,0,0,3,2
0,5,7,2,0,4,0,9,0
0,6,0,4,1,0,3,7,0
0,7,3,9,0,8,0,6,0
0,0,0,7,6,0,4,0,0
```
The sudoku file is expected to have one line header and all numbers seperated by comma (',').

Now run the sudoku.py program
```
python sudoku.py -f 001_sudoku.txt
```
The program will try through all possible varations and will hopefully come to a result like this:
```
     C1 C2 C3 C4 C5 C6 C7 C8 C9

 R1   9  4  6  8  3  1  2  5  7  
 R2   7  2  8  5  4  9  6  1  3  
 R3   1  3  5  6  7  2  9  8  4  
 R4   8  1  2  3  9  6  7  4  5  
 R5   6  9  4  1  5  7  8  3  2  
 R6   3  5  7  2  8  4  1  9  6  
 R7   2  6  9  4  1  5  3  7  8  
 R8   4  7  3  9  2  8  5  6  1  
 R9   5  8  1  7  6  3  4  2  9  

== Analyzing ==

Sudoku is solved                 : True
Sudoku is deadlocked             : False
Found duplicates in rows         : False
Found duplicates in columns      : False
Solved positions                 : 81 / 81
Unsolved positions               : 0
Min unsolved positions           : 0
Save predicable positions        : 0
Branch points                    : 1
Current depth                    : 1
Max depth                        : 1
Iteration from latest branch     : 6
Iteration in total               : 6

Operation stopped.

Runtime       : 0:00:00.249702
Branch points : 1
Iterations    : 6

*** Bingo! Sudoku is solved. ***
```

If you want to create a binary of the python code, try this:
```
$ pyinstaller sudoku.py --onefile --clean
```
The pyinstaller will create a binary in the folder "dist" for you.

Happy coding, Jens
