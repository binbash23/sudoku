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
        print(" R" + str(i + 1) + "  ", end=" ")
        for j in range(0, 9):
            # print(str(a[i, j]) + " ", end=" ")
            print(str(trunc(a[i, j])) + " ", end=" ")
        print()
    print()


def count_nulls_in_sector(a: array, sector: int, verbose: bool=False) -> int:
    """

    :param verbose: Print debug info
    :param a: A two-dimensional array with the sudoku data
    :param sector: A number between 1 and 9
    :return: The number of zeros in the given sector
    """
    count_nulls = 0
    if sector < 1 or sector > 9:
        raise Exception("Sector must be between 1 and 9")
    if sector == 1:
        for x in range(0, 3):
            for y in range(0,3):
                if a[x, y] == N:
                    count_nulls += 1
    if sector == 2:
        for x in range(0, 3):
            for y in range(3,6):
                if a[x, y] == N:
                    count_nulls += 1
    if sector == 3:
        for x in range(0, 3):
            for y in range(6,9):
                if a[x, y] == N:
                    count_nulls += 1
    if sector == 4:
        for x in range(3, 6):
            for y in range(0,3):
                if a[x, y] == N:
                    count_nulls += 1
    if sector == 5:
        for x in range(3, 6):
            for y in range(3,6):
                if a[x, y] == N:
                    count_nulls += 1
    if sector == 6:
        for x in range(3, 6):
            for y in range(6,9):
                if a[x, y] == N:
                    count_nulls += 1
    if sector == 7:
        for x in range(6, 9):
            for y in range(0,3):
                if a[x, y] == N:
                    count_nulls += 1
    if sector == 8:
        for x in range(6, 9):
            for y in range(3,6):
                if a[x, y] == N:
                    count_nulls += 1
    if sector == 9:
        for x in range(6, 9):
            for y in range(6,9):
                if a[x, y] == N:
                    count_nulls += 1
    if verbose:
        if count_nulls == 0 or count_nulls == 1:
            print("Nulls in S" + str(sector) + " : " + str(count_nulls) + " *")
        else:
            print("Nulls in S" + str(sector) + " : " + str(count_nulls))
    # if verbose:
    #     print("Nulls in S" + str(sector) + " : " + str(count_nulls))
    return count_nulls


def possible_numbers_in_sector(a: array, sector: int, verbose: bool=False) -> array:
    """

    :param a: A two-dimensional array with the sudoku data
    :param sector: A number between 1 and 9
    :return: An array with possible numbers that are not used in this sector yet.
    """
    numbers = array(range(1, 10))
    if sector < 1 or sector > 9:
        raise Exception("Sector must be between 1 and 9")
    if sector == 1:
        for x in range(0, 3):
            for y in range(0,3):
                if a[x, y] != N:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 2:
        for x in range(0, 3):
            for y in range(3,6):
                if a[x, y] != N:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 3:
        for x in range(0, 3):
            for y in range(6,9):
                if a[x, y] != N:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 4:
        for x in range(3, 6):
            for y in range(0,3):
                if a[x, y] != N:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 5:
        for x in range(3, 6):
            for y in range(3,6):
                if a[x, y] != N:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 6:
        for x in range(3, 6):
            for y in range(6,9):
                if a[x, y] != N:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 7:
        for x in range(6, 9):
            for y in range(0,3):
                if a[x, y] != N:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 8:
        for x in range(6, 9):
            for y in range(3,6):
                if a[x, y] != N:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 9:
        for x in range(6, 9):
            for y in range(6,9):
                if a[x, y] != N:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    return numbers


def serialize_array(a: array, filename: str = "sudoku.txt"):
    """

    :param a: A two dimensional array with the sudoku data
    :param filename: The name of the file to write the data into
    :return:
    """
    numpy.savetxt(filename, a, delimiter=',', header='Sudoku', fmt='%d')


def deserialize_array(filename: str = "sudoku.txt") -> array:
    return numpy.loadtxt(filename, delimiter=",", skiprows=1)


def count_nulls_in_row(a: array, row_nr: int, verbose: bool = False) -> int:
    count_nulls = 0
    for j in range(0, 9):
        if a[row_nr, j] == N:
            count_nulls += 1
    # print("Row    " + str(row_nr+1) + " has " + str(count_nulls) + " nulls.")
    if verbose:
        if count_nulls == 0 or count_nulls == 1:
            print("Nulls in R" + str(row_nr + 1) + " : " + str(count_nulls) + " *")
        else:
            print("Nulls in R" + str(row_nr + 1) + " : " + str(count_nulls))
    return count_nulls


def count_nulls_in_column(a: array, column_nr: int, verbose: bool = False) -> int:
    count_nulls = 0
    for j in range(0, 9):
        if a[j, column_nr] == N:
            count_nulls += 1
    # print("Column " + str(column_nr+1) + " has " + str(count_nulls) + " nulls.")
    if verbose:
        if count_nulls == 0 or count_nulls == 1:
            print("Nulls in C" + str(column_nr + 1) + " : " + str(count_nulls) + " *")
        else:
            print("Nulls in C" + str(column_nr + 1) + " : " + str(count_nulls))
    # if verbose:
    #     print("Nulls in C" + str(column_nr + 1) + " : " + str(count_nulls))
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


def possible_numbers_in_column(a: array, column_nr: int) -> array:
    numbers = array(range(1,10))
    for j in range(0, 9):
        if a[j, column_nr] != N:
            numbers = numpy.setdiff1d(numbers, a[j, column_nr])
            # print("->" + str(numbers_1_to_10))
    return numbers


def possible_numbers_in_row(a: array, row_nr: int) -> array:
    numbers = array(range(1,10))
    for j in range(0, 9):
        if a[row_nr, j] != N:
            numbers = numpy.setdiff1d(numbers, a[row_nr, j])
            # print("->" + str(numbers_1_to_10))
    return numbers


def possible_numbers_in_columns(a:array):
    for i in range(0, 9):
        print("Possible numbers in C" + str(i+1) + " : " + str(possible_numbers_in_column(a, i)))


def possible_numbers_in_rows(a:array):
    for i in range(0, 9):
        print("Possible numbers in R" + str(i+1) + " : " + str(possible_numbers_in_row(a, i)))


def possible_numbers_in_sectors(a:array):
    for i in range(1, 10):
        print("Possible numbers in S" + str(i) + " : " + str(possible_numbers_in_sector(a, i)))


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


def rows_have_duplicates(a: array, verbose: bool = False) -> bool:
    for i in range(0, 9):
        if verbose:
            print("Duplicates in R" + str(i + 1) + ": " + str(row_has_duplicates(a, i)))
        if row_has_duplicates(a, i):
            return True
    return False


def columns_have_duplicates(a: array, verbose: bool = False) -> bool:
    for i in range(0, 9):
        if verbose:
            print("Duplicates in R" + str(i + 1) + ": " + str(column_has_duplicates(a, i)))
        if column_has_duplicates(a, i):
            return True
    return False


def count_nulls_in_rows(a: array, verbose: bool = False) -> int:
    count_nulls = 0
    for i in range(0, 9):
        count_nulls += count_nulls_in_row(a, i, verbose)
    return count_nulls


def count_nulls_in_columns(a: array, verbose: bool = False) -> int:
    count_nulls = 0
    for i in range(0, 9):
        count_nulls += count_nulls_in_column(a, i, verbose)
    return count_nulls


def count_nulls_in_sectors(a: array, verbose: bool = False) -> int:
    count_nulls = 0
    for i in range(1, 10):
        count_nulls += count_nulls_in_sector(a, i, verbose)
    return count_nulls


def analyze_sudoku(a, verbose: bool=False):
    print("== Analyzing sudoku")
    print("== Duplicate checking in rows    : " + str(rows_have_duplicates(a)))
    print("== Duplicate checking in columns : " + str(columns_have_duplicates(a)))
    print("== Nulls in rows                 : " + str(count_nulls_in_rows(a, verbose)))
    print("== Nulls in columns              : " + str(count_nulls_in_columns(a, verbose)))
    print("== Nulls in sectors              : " + str(count_nulls_in_sectors(a, verbose)))
    print("== Possible numbers in columns")
    possible_numbers_in_columns(a)
    print("== Possible numbers in rows")
    possible_numbers_in_rows(a)
    print("== Possible numbers in sectors")
    possible_numbers_in_sectors(a)


def main():
    a = deserialize_array()
    show(a)
    analyze_sudoku(a, False)
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
