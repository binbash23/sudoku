"""

20240916 jens heine <binbash@gmx.net>

sudoku.py

"""

import random
from numpy import array
import numpy

# Variables section
N = '?'
s = array(
    [[1, 1, 1, 1, N, 1, 1, 1, 1], [2, 3, 4, 5, 6, 7, 8, 9, 1], [3, 1, 1, 1, 1, 1, 1, 1, 1], [4, 1, 1, 1, 1, 1, 1, 1, 1],
     [5, 1, 1, 1, 1, 1, 1, 1, 1], [6, 1, 1, 1, 1, 1, 1, 1, 1], [7, 1, 1, 1, 1, 1, 1, 1, 1], [8, 1, 1, 1, 1, 1, 1, 1, 1],
     [9, 1, 1, 1, 1, 1, 1, 1, 1]])


# Functions section

def empty(a: array):
    for i in range(0, 9):
        for j in range(0, 9):
            a[i, j] = N


def randomize(a: array):
    for i in range(0, 9):
        for j in range(0, 9):
            a[i, j] = random.randint(1, 9)


def show(a: array):
    print("    C1 C2 C3 C4 C5 C6 C7 C8 C9")
    for i in range(0, 9):
        print(" R" + str(i + 1) + " ", end=" ")
        for j in range(0, 9):
            print(a[i, j] + " ", end=" ")
        print()
    print()


def count_nulls_in_row(a: array, row_nr: int) -> int:
    count_nulls = 0
    for j in range(0, 9):
        if a[row_nr, j] == N:
            count_nulls += 1
    print("Row " + str(row_nr) + " has " + str(count_nulls) + " nulls.")
    return False


def count_nulls_in_column(a: array, column_nr: int) -> int:
    count_nulls = 0
    for j in range(0, 9):
        if a[j, column_nr] == N:
            count_nulls += 1
    print("Column " + str(column_nr) + " has " + str(count_nulls) + " nulls.")
    return False


def column_has_duplicates(a: array, column_nr: int) -> bool:
    numbers = array(range(1, 10))
    matched = False
    for j in range(0, 9):
        if a[j, column_nr] == N:
            # print("Found N value, skipping")
            continue
        matched = False
        # print("Checking: array[" + str(j) + ", " + str(column_nr) + "] : " + str(a[j, column_nr]))
        for x in range(0, numbers.size):
            # print("Verifying: " + str(a[j, column_nr]) + " with " + str(numbers[x]))
            if str(a[j, column_nr]) == str(numbers[x]):
                # print("Found: " + str(numbers[x]))
                matched = True
                # print("Deleting " + str(numbers[x]) + " from numbers array")
                numbers = numpy.delete(numbers, x)
                break
    if not matched:
        return True
    return False


def row_has_duplicates(a: array, row_nr: int) -> bool:
    numbers = array(range(1, 10))
    matched = False
    for j in range(0, 9):
        #print("Checking: array[" + str(j) + ", " + str(row_nr) + "] : " + str(a[row_nr, j]))
        if a[row_nr, j] == N:
            #print("Found N value, skipping")
            continue
        matched = False
        for x in range(0, numbers.size):
            # print("Verifying: " + str(a[j, column_nr]) + " with " + str(numbers[x]))
            if str(a[row_nr, j]) == str(numbers[x]):
                # print("Found: " + str(numbers[x]))
                matched = True
                # print("Deleting " + str(numbers[x]) + " from numbers array")
                numbers = numpy.delete(numbers, x)
                break
    if not matched:
        return True
    return False



show(s)
print()


#print("Column 1 has duplicates: " + str(column_has_duplicates(s, 0)))
#print("Column 2 has duplicates: " + str(column_has_duplicates(s, 1)))

#print("Row 4 has duplicates: " + str(row_has_duplicates(s, 3)))
#print("Row 2 has duplicates: " + str(row_has_duplicates(s, 1)))

#for f in range(0, 9):
#    print("Row " + str(f+1) + " has duplicates: " + str(row_has_duplicates(s, f)))

# for f in range(0, 9):
#     #print("Row " + str(f+1) + " has duplicates: " + str(row_has_duplicates(s, f)))
#     count_nulls_in_row(s, f)

#empty(s)
#show(s)

#randomize(s)
#show(s)

#count_nulls_in_row(s, 3)
#count_nulls_in_column(s, 4)
