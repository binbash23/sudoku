"""

20240916 jens heine <binbash@gmx.net>

sudoku.py

"""

import random
from numpy import array
import numpy
from math import trunc

# Variables section
N = 0


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
    print("     C1 C2 C3 C4 C5 C6 C7 C8 C9")
    print()
    for i in range(0, 9):
        print(" R" + str(i + 1) + " ", end=" ")
        for j in range(0, 9):
            # print(str(a[i, j]) + " ", end=" ")
            print(str(trunc(a[i, j])) + " ", end=" ")
        print()
    print()


def serialize_array(a: array, filename:  str="sudoku.txt"):
    numpy.savetxt(filename, a, delimiter=',', header='Sudoku', fmt='%d')


def deserialize_array(filename: str="sudoku.txt") -> array:
    return numpy.loadtxt(filename, delimiter=",", skiprows=1)


def count_nulls_in_row(a: array, row_nr: int, verbose: bool=False) -> int:
    count_nulls = 0
    for j in range(0, 9):
        if a[row_nr, j] == N:
            count_nulls += 1
    # print("Row    " + str(row_nr+1) + " has " + str(count_nulls) + " nulls.")
    if verbose:
        print("Nulls in R" + str(row_nr + 1) + " : " + str(count_nulls))
    return count_nulls


def count_nulls_in_column(a: array, column_nr: int, verbose: bool=False) -> int:
    count_nulls = 0
    for j in range(0, 9):
        if a[j, column_nr] == N:
            count_nulls += 1
    # print("Column " + str(column_nr+1) + " has " + str(count_nulls) + " nulls.")
    if verbose:
        print("Nulls in C" + str(column_nr + 1) + " : " + str(count_nulls))
    return count_nulls


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
    if matched:
        return True
    else:
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
    if matched:
        return True
    else:
        return False


def rows_have_duplicates(a: array, verbose: bool=False) -> bool:
    for i in range(0, 9):
        if verbose:
            print("Duplicates in R" + str(i+1) + ": " + str(row_has_duplicates(a, i)))
        if row_has_duplicates(a, i):
            return True
    return False


def columns_have_duplicates(a: array, verbose: bool=False) -> bool:
    for i in range(0, 9):
        if verbose:
            print("Duplicates in R" + str(i+1) + ": " + str(column_has_duplicates(a, i)))
        if column_has_duplicates(a, i):
            return True
    return False


def count_nulls_in_rows(a: array, verbose: bool=False) -> int:
    count_nulls=0
    for i in range(0, 9):
        count_nulls+=count_nulls_in_row(a, i)
    return count_nulls


def count_nulls_in_columns(a: array, verbose: bool=False) -> int:
    count_nulls=0
    for i in range(0, 9):
        count_nulls+=count_nulls_in_column(a, i)
    return count_nulls


def show_sudoku_status(a):
    print("== Analyzing sudoku")
    print("== Duplicate checking in rows    : " + str(rows_have_duplicates(a)))
    print("== Duplicate checking in columns : " + str(columns_have_duplicates(a)))
    print("== Nulls in rows                 : " + str(count_nulls_in_rows(a)))
    print("== Nulls in columns              : " + str(count_nulls_in_columns(a)))


def main():
    a = deserialize_array()
    show(a)
    show_sudoku_status(a)
    #print(a)
    #empty(a)
    #randomize(a)
    #show(a)
    #serialize_array(a)


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

if __name__ == '__main__':
    main()
