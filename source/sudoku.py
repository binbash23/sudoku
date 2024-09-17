"""
20240916 jens heine <binbash@gmx.net>

sudoku.py

"""

#import array 
#import numpy.array
from numpy import array

# Variables section
N='-'
s = array([ [1, 1, 1, 1, N, 1, 1, 1, 1], [2, 1, 1, 1, 1, 1, 1, 1, 1], [3, 1, 1, 1, 1, 1, 1, 1, 1], [4, 1, 1, 1, 1, 1, 1, 1, 1], [5, 1, 1, 1, 1, 1, 1, 1, 1], [6, 1, 1, 1, 1, 1, 1, 1, 1], [7, 1, 1, 1, 1, 1, 1, 1, 1], [8, 1, 1, 1, 1, 1, 1, 1, 1], [9, 1, 1, 1, 1, 1, 1, 1, 1] ])

# Functions section
def show(a: array):
    for i in range(0,8):
        for j in range(0,8):
            print(a[i, j], end=" ")
        print()
    print()


def line_is_complete(a: array, i: int) -> bool:
    print("Line " + str(i+1) + ":")
    for j in range(0,8):
        print(a[i, j], end=" ")
    print()
    return False


show(s)
print()
line_is_complete(s, 3)


