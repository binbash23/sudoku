"""

20240916 jens heine <binbash@gmx.net>

sudoku.py

"""

import random

from numpy import array
import numpy
from math import trunc

# Variables section
zero = 0


# Functions section

def empty(a: array):
    """
    Fill the given sudoku matrix with zeros.
    :param a: A two-dimensional array with the sudoku data
    :return:
    """
    for i in range(0, 9):
        for j in range(0, 9):
            a[i, j] = zero


def randomize(a: array):
    for i in range(0, 9):
        for j in range(0, 9):
            a[i, j] = random.randint(1, 9)


def show(a: array):
    """
    Print out the sudoku matrix.
    :param a: A two-dimensional array with the sudoku data
    :return:
    """
    print()
    print("     C1 C2 C3 C4 C5 C6 C7 C8 C9")
    print()
    for row_index in range(0, 9):
        print(" R" + str(row_index + 1) + "  ", end=" ")
        for column_index in range(0, 9):
            # print(str(a[i, j]) + " ", end=" ")
            print(str(trunc(a[row_index, column_index])) + " ", end=" ")
        print()
    print()


def count_nulls_in_sector(a: array, sector: int, verbose: bool=False) -> int:
    """
    Count the unknown numbers in the given sudoku matrix sector. The sector has to be
    between 1 and 9.
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
                if a[x, y] == zero:
                    count_nulls += 1
    if sector == 2:
        for x in range(0, 3):
            for y in range(3,6):
                if a[x, y] == zero:
                    count_nulls += 1
    if sector == 3:
        for x in range(0, 3):
            for y in range(6,9):
                if a[x, y] == zero:
                    count_nulls += 1
    if sector == 4:
        for x in range(3, 6):
            for y in range(0,3):
                if a[x, y] == zero:
                    count_nulls += 1
    if sector == 5:
        for x in range(3, 6):
            for y in range(3,6):
                if a[x, y] == zero:
                    count_nulls += 1
    if sector == 6:
        for x in range(3, 6):
            for y in range(6,9):
                if a[x, y] == zero:
                    count_nulls += 1
    if sector == 7:
        for x in range(6, 9):
            for y in range(0,3):
                if a[x, y] == zero:
                    count_nulls += 1
    if sector == 8:
        for x in range(6, 9):
            for y in range(3,6):
                if a[x, y] == zero:
                    count_nulls += 1
    if sector == 9:
        for x in range(6, 9):
            for y in range(6,9):
                if a[x, y] == zero:
                    count_nulls += 1
    if verbose:
        if count_nulls == 0 or count_nulls == 1:
            print("Nulls in S" + str(sector) + " : " + str(count_nulls) + " *")
        else:
            print("Nulls in S" + str(sector) + " : " + str(count_nulls))
    # if verbose:
    #     print("Nulls in S" + str(sector) + " : " + str(count_nulls))
    return count_nulls


def possible_numbers_in_sector(a: array, sector: int) -> array:
    """
    Search a list of all possible numbers that may fit into the given sector of the
    sudoku matrix.
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
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 2:
        for x in range(0, 3):
            for y in range(3,6):
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 3:
        for x in range(0, 3):
            for y in range(6,9):
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 4:
        for x in range(3, 6):
            for y in range(0,3):
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 5:
        for x in range(3, 6):
            for y in range(3,6):
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 6:
        for x in range(3, 6):
            for y in range(6,9):
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 7:
        for x in range(6, 9):
            for y in range(0,3):
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 8:
        for x in range(6, 9):
            for y in range(3,6):
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 9:
        for x in range(6, 9):
            for y in range(6,9):
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    return numbers


def serialize_array(a: array, filename: str = "sudoku.txt"):
    """
    Write the content of a sudoku matrix into a file with the given filename
    which is sudoku.txt per default
    :param a: A two-dimensional array with the sudoku data
    :param filename: The name of the file to write the data into
    :return:
    """
    numpy.savetxt(filename, a, delimiter=',', header='Sudoku', fmt='%d')


def deserialize_array(filename: str = "sudoku.txt") -> array:
    """
    Load the data of a sudoku matrix from a given file into an array and return
    it. Default filename is sudoku.txt.
    :param filename: The filename of the matrix data
    :return: An array with the sudoku matrix data
    """
    return numpy.loadtxt(filename, delimiter=",", skiprows=1)


def count_nulls_in_row(a: array, row_index: int, verbose: bool = False) -> int:
    """
    Count the unknown numbers in a given row. The row count start at 0.
    :param a: A two-dimensional array with the sudoku data
    :param row_index: The array index of the row starting at 0
    :param verbose: Show some debug info
    :return: The count of unknown numbers in a row
    """
    count_nulls = 0
    for j in range(0, 9):
        if a[row_index, j] == zero:
            # if verbose:
            #     print("a[row_index, j] == zero : True")
            #     print("type(a[row_index, j]) : " + str(type(a[row_index, j])))
            #     print("type(zero) : " + str(type(zero)))
            count_nulls += 1
    # print("Row    " + str(row_nr+1) + " has " + str(count_nulls) + " nulls.")
    if verbose:
        if count_nulls == 0 or count_nulls == 1:
            print("Nulls in R" + str(row_index + 1) + " : " + str(count_nulls) + " *")
        else:
            print("Nulls in R" + str(row_index + 1) + " : " + str(count_nulls))
    return count_nulls


def count_nulls_in_column(a: array, column_index: int, verbose: bool = False) -> int:
    """
    Count the unknown numbers in a given column. The column count start at 0.
    :param a: A two-dimensional array with the sudoku data
    :param column_index: The array index of the column starting at 0
    :param verbose: Show some debug info
    :return: The count of unknown numbers in a column
    """
    count_nulls = 0
    for j in range(0, 9):
        if a[j, column_index] == zero:
            count_nulls += 1
    # print("Column " + str(column_nr+1) + " has " + str(count_nulls) + " nulls.")
    if verbose:
        if count_nulls == 0 or count_nulls == 1:
            print("Nulls in C" + str(column_index + 1) + " : " + str(count_nulls) + " *")
        else:
            print("Nulls in C" + str(column_index + 1) + " : " + str(count_nulls))
    # if verbose:
    #     print("Nulls in C" + str(column_nr + 1) + " : " + str(count_nulls))
    return count_nulls


def column_has_duplicates(a: array, column_index: int) -> bool:
    """
    Check if a given column has duplicate numbers in it.
    :param a: A two-dimensional array with the sudoku data
    :param column_index: The index of the column starting at 0
    :return: True if a number from 1 to 9 appears more than one time in the column
    """
    numbers = array(range(1, 10))
    matched = False
    for j in range(0, 9):
        if a[j, column_index] == zero:
            # print("Found N value, skipping")
            continue
        matched = False
        # print("Checking: array[" + str(j) + ", " + str(column_nr) + "] : " + str(a[j, column_nr]))
        for x in range(0, numbers.size):
            # print("Verifying: " + str(a[j, column_nr]) + " with " + str(numbers[x]))
            if str(a[j, column_index]) == str(numbers[x]):
                # print("Found: " + str(numbers[x]))
                matched = True
                # print("Deleting " + str(numbers[x]) + " from numbers array")
                numbers = numpy.delete(numbers, x)
                break
    if matched:
        return True
    else:
        return False


def possible_numbers_in_column(a: array, column_index: int) -> array:
    """
    Search possible numbers in a given column.
    :param a: A two-dimensional array with the sudoku data
    :param column_index: The column index starting at 0
    :return: A list possible numbers in the given column
    """
    numbers = array(range(1,10))
    for j in range(0, 9):
        if a[j, column_index] != zero:
            numbers = numpy.setdiff1d(numbers, a[j, column_index])
            # print("->" + str(numbers_1_to_10))
    return numbers


def possible_numbers_in_row(a: array, row_index: int) -> array:
    """
    Search possible numbers in a given row.
    :param a: A two-dimensional array with the sudoku data
    :param row_index: The row index starting at 0
    :return: A list possible numbers in the given row
    """
    numbers = array(range(1,10))
    for j in range(0, 9):
        if a[row_index, j] != zero:
            numbers = numpy.setdiff1d(numbers, a[row_index, j])
            # print("->" + str(numbers_1_to_10))
    return numbers


def possible_numbers_in_columns(a:array, verbose:bool=False):
    """
    Print the possible numbers to be filled in of all columns.
    :param verbose: Show debug info
    :param a: A two-dimensional array with the sudoku data
    :return:
    """
    unsolved_columns = 0
    for i in range(0, 9):
        current_numbers = possible_numbers_in_column(a, i)
        if len(current_numbers) > 1:
            unsolved_columns+=1
        if verbose:
            print("Possible numbers in C" + str(i+1) + " : " + str(current_numbers))
    print("Unsolved columns : " + str(unsolved_columns))


def possible_numbers_in_rows(a:array, verbose:bool=False):
    """
    Print the possible numbers to be filled in of all rows.
    :param verbose: Show debug info
    :param a: A two-dimensional array with the sudoku data
    :return:
    """
    unsolved_rows = 0
    for i in range(0, 9):
        current_numbers = possible_numbers_in_row(a, i)
        if len(current_numbers) > 1:
            unsolved_rows += 1
        if verbose:
            print("Possible numbers in R" + str(i+1) + " : " + str(current_numbers))
    print("Unsolved rows : " + str(unsolved_rows))


def possible_numbers_in_sectors(a:array, verbose:bool=False):
    """
    Print the possible numbers to be filled in of all sectors.
    :param verbose: Show debug info
    :param a: A two-dimensional array with the sudoku data
    :return:
    """
    unsolved_sectors = 0
    for i in range(1, 10):
        current_numbers = possible_numbers_in_sector(a, i)
        if len(current_numbers) > 1:
            unsolved_sectors += 1
        if verbose:
            print("Possible numbers in S" + str(i) + " : " + str(current_numbers))
    print("Unsolved sectors : " + str(unsolved_sectors))


def row_has_duplicates(a: array, row_index: int) -> bool:
    """
    Check if a given row has duplicate numbers in it.
    :param a: A two-dimensional array with the sudoku data
    :param row_index: The row index starting at 0
    :return: True if the row has a number between 1 and 9 more than one time
    """
    numbers = array(range(1, 10))
    matched = False
    for j in range(0, 9):
        #print("Checking: array[" + str(j) + ", " + str(row_nr) + "] : " + str(a[row_nr, j]))
        if a[row_index, j] == zero:
            #print("Found N value, skipping")
            continue
        matched = False
        for x in range(0, numbers.size):
            # print("Verifying: " + str(a[j, column_nr]) + " with " + str(numbers[x]))
            if str(a[row_index, j]) == str(numbers[x]):
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


def get_sector_id(row_index: int, column_index: int) -> int:
    """
    Determine the sudoku sector id of the given coordinates. Can be between 1 and 9
    :param column_index: The column of the element to analyze
    :param row_index: The row of the element to analyze
    :return: The sector number of the element with column, row
    """
    if row_index < 3 and column_index < 3:
        return 1
    if row_index < 3 and column_index < 6:
        return 2
    if row_index < 3 and column_index < 9:
        return 3
    if row_index < 6 and column_index < 3:
        return 4
    if row_index < 6 and column_index < 6:
        return 5
    if row_index < 6 and column_index < 9:
        return 6
    if row_index < 9 and column_index < 3:
        return 7
    if row_index < 9 and column_index < 6:
        return 8
    if row_index < 9 and column_index < 9:
        return 9

def possible_numbers_in_position(a: array, row_index: int, column_index: int, verbose: bool=False) -> array:
    """
    Search a list of possible numbers that can fit in the position of the sudoku matrix
    :param verbose: Show debug info
    :param a: A two-dimensional array with the sudoku data
    :param column_index: The column number to analyze
    :param row_index: The row number to analyze
    :return: All possible numbers that may fit on this position in an array
    """
    if a[row_index, column_index] != zero:
        if verbose:
            print("Found value != " + str(zero) + " : " + str(a[row_index, column_index]))
            # print("Type a[column_index, row_index] : " + str(type(a[row_index, column_index])))
            # print("Type zero                       : " + str(type(zero)))
            print("row_index : " + str(row_index))
            print("column_index : " + str(column_index))
        return array([trunc(a[row_index, column_index])])
    numbers = numpy.intersect1d(possible_numbers_in_column(a, column_index), possible_numbers_in_row(a, row_index))
    if verbose:
        print("Possible values in C" + str(column_index) + " : " + str(possible_numbers_in_column(a, column_index)))
        print("Possible values in R" + str(row_index) + " : " + str(possible_numbers_in_row(a, row_index)))
        print("Intersect between possible values from C" + str(column_index) + " and R" + str(row_index) + " : " + str(numbers))
    numbers = numpy.intersect1d(numbers, possible_numbers_in_sector(a, get_sector_id(row_index, column_index)))
    if verbose:
        print("Possible numbers in S" + str(get_sector_id(row_index, column_index)) + " : " + str(possible_numbers_in_sector(a, get_sector_id(row_index, column_index))))
    return numbers


def possible_numbers_in_positions(a: array, verbose: bool=False):
    """
    Search possible numbers that can fit in the every position of the sudoku
    :param verbose: Show debug info
    :param a: A two-dimensional array with the sudoku data
    :return:
    """
    unknown_positions = 0
    for row_index in range(0, 9):
        for column_index in range(0, 9):
            current_possible_numbers = possible_numbers_in_position(a, row_index, column_index)
            if len(current_possible_numbers) > 1:
                unknown_positions+=1
            if verbose:
                print("R" + str(row_index+1) + ", C" + str(column_index+1) + " : " + str(current_possible_numbers))
    print("Unknown positions : " + str(unknown_positions))


def analyze_sudoku(a, verbose: bool=False):
    """
    Prints out some structure analysis of the sudoku matrix in arg a
    :param a: A two-dimensional array with the sudoku data
    :param verbose: Show some debug info
    :return:
    """
    print("== Analyzing sudoku")
    print("== Duplicate checking in rows    : " + str(rows_have_duplicates(a)))
    print("== Duplicate checking in columns : " + str(columns_have_duplicates(a)))
    print("== Nulls in rows")
    print("== Nulls in rows                 : " + str(count_nulls_in_rows(a, verbose)))
    print("== Nulls in columns")
    print("== Nulls in columns              : " + str(count_nulls_in_columns(a, verbose)))
    print("== Nulls in sectors              : " + str(count_nulls_in_sectors(a, verbose)))
    print("== Possible numbers in columns")
    possible_numbers_in_columns(a)
    print("== Possible numbers in rows")
    possible_numbers_in_rows(a)
    print("== Possible numbers in sectors")
    possible_numbers_in_sectors(a)
    print("== Possible numbers in positions")
    possible_numbers_in_positions(a, verbose)

    # print("== debug")
    # # print("Sector nr from C3, R2: " + str(get_sector_id(1, 2)))
    # print("Sector nr from C4, R3: " + str(get_sector_id(2, 3)))
    #
    # # print("C0, R0 : " + str(possible_number_in_position(a, 0, 0, True)))
    # # print("C1, R2 : " + str(possible_number_in_position(a, 0, 1, True)))
    # print("possible_number_in_position C4, R3 : " + str(possible_number_in_position(a, 2, 3, True)))


def main():
    a = deserialize_array()
    show(a)
    analyze_sudoku(a, False)
    #print(a)
    #empty(a)
    #randomize(a)
    #show(a)
    #serialize_array(a)


if __name__ == '__main__':
    main()
