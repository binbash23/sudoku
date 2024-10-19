"""

20240916 jens heine <binbash@gmx.net>

sudoku.py

"""

import random
import sys
from math import trunc
from optparse import OptionParser

import numpy
from numpy import array
from branch_point import BranchPoint
from branch_point_tree import BranchPointTree

# Variables section
zero = 0


# _branch_point_tree: BranchPointTree = None
# filename = "sudoku.txt"


# Functions section

def fill_with_zeros(a: array):
    """
    Fill the given sudoku matrix with zeros.
    :param a: A two-dimensional array with the sudoku data
    :return:
    """
    for i in range(0, 9):
        for j in range(0, 9):
            a[i, j] = zero


def fill_with_random_numbers(a: array):
    """
    Fill the given sudoku matrix with random numbers.
    :param a: A two-dimensional array with the sudoku data
    :return:
    """
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


def count_zeros_in_sector(a: array, sector: int, verbose: bool = False) -> int:
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
            for y in range(0, 3):
                if a[x, y] == zero:
                    count_nulls += 1
    if sector == 2:
        for x in range(0, 3):
            for y in range(3, 6):
                if a[x, y] == zero:
                    count_nulls += 1
    if sector == 3:
        for x in range(0, 3):
            for y in range(6, 9):
                if a[x, y] == zero:
                    count_nulls += 1
    if sector == 4:
        for x in range(3, 6):
            for y in range(0, 3):
                if a[x, y] == zero:
                    count_nulls += 1
    if sector == 5:
        for x in range(3, 6):
            for y in range(3, 6):
                if a[x, y] == zero:
                    count_nulls += 1
    if sector == 6:
        for x in range(3, 6):
            for y in range(6, 9):
                if a[x, y] == zero:
                    count_nulls += 1
    if sector == 7:
        for x in range(6, 9):
            for y in range(0, 3):
                if a[x, y] == zero:
                    count_nulls += 1
    if sector == 8:
        for x in range(6, 9):
            for y in range(3, 6):
                if a[x, y] == zero:
                    count_nulls += 1
    if sector == 9:
        for x in range(6, 9):
            for y in range(6, 9):
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


def predictable_numbers_in_sector(a: array, sector: int) -> array:
    """
    Search a list of all predictable numbers that may fit into the given sector of the
    sudoku matrix.
    :param a: A two-dimensional array with the sudoku data
    :param sector: A number between 1 and 9
    :return: An array with predictable numbers that are not used in this sector yet.
    """
    numbers = array(range(1, 10))
    if sector < 1 or sector > 9:
        raise Exception("Sector must be between 1 and 9")
    if sector == 1:
        for x in range(0, 3):
            for y in range(0, 3):
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 2:
        for x in range(0, 3):
            for y in range(3, 6):
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 3:
        for x in range(0, 3):
            for y in range(6, 9):
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 4:
        for x in range(3, 6):
            for y in range(0, 3):
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 5:
        for x in range(3, 6):
            for y in range(3, 6):
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 6:
        for x in range(3, 6):
            for y in range(6, 9):
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 7:
        for x in range(6, 9):
            for y in range(0, 3):
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 8:
        for x in range(6, 9):
            for y in range(3, 6):
                if a[x, y] != zero:
                    numbers = numpy.setdiff1d(numbers, a[x, y])
    if sector == 9:
        for x in range(6, 9):
            for y in range(6, 9):
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


def count_zeros_in_row(a: array, row_index: int, verbose: bool = False) -> int:
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


def count_zeros_in_column(a: array, column_index: int, verbose: bool = False) -> int:
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


def predictable_numbers_in_column(a: array, column_index: int) -> array:
    """
    Search predictable numbers in a given column.
    :param a: A two-dimensional array with the sudoku data
    :param column_index: The column index starting at 0
    :return: A list predictable numbers in the given column
    """
    numbers = array(range(1, 10))
    for j in range(0, 9):
        if a[j, column_index] != zero:
            numbers = numpy.setdiff1d(numbers, a[j, column_index])
            # print("->" + str(numbers_1_to_10))
    return numbers


def predictable_numbers_in_row(a: array, row_index: int) -> array:
    """
    Search predictable numbers in a given row.
    :param a: A two-dimensional array with the sudoku data
    :param row_index: The row index starting at 0
    :return: A list predictable numbers in the given row
    """
    numbers = array(range(1, 10))
    for j in range(0, 9):
        if a[row_index, j] != zero:
            numbers = numpy.setdiff1d(numbers, a[row_index, j])
            # print("->" + str(numbers_1_to_10))
    return numbers


def predictable_numbers_in_columns(a: array, verbose: bool = False):
    """
    Print the predictable numbers to be filled in of all columns.
    :param verbose: Show debug info
    :param a: A two-dimensional array with the sudoku data
    :return:
    """
    unsolved_columns = 0
    for i in range(0, 9):
        current_numbers = predictable_numbers_in_column(a, i)
        if len(current_numbers) > 1:
            unsolved_columns += 1
        if verbose:
            print("Predictable numbers in C" + str(i + 1) + " : " + str(current_numbers))
    print("Unsolved columns                 : " + str(unsolved_columns))


def predictable_numbers_in_rows(a: array, verbose: bool = False):
    """
    Print the predictable numbers to be filled in of all rows.
    :param verbose: Show debug info
    :param a: A two-dimensional array with the sudoku data
    :return:
    """
    unsolved_rows = 0
    for i in range(0, 9):
        current_numbers = predictable_numbers_in_row(a, i)
        if len(current_numbers) > 1:
            unsolved_rows += 1
        if verbose:
            print("Predictable numbers in R" + str(i + 1) + " : " + str(current_numbers))
    print("Unsolved rows                    : " + str(unsolved_rows))


def predictable_numbers_in_sectors(a: array, verbose: bool = False):
    """
    Print the predictable numbers to be filled in of all sectors.
    :param verbose: Show debug info
    :param a: A two-dimensional array with the sudoku data
    :return:
    """
    unsolved_sectors = 0
    for i in range(1, 10):
        current_numbers = predictable_numbers_in_sector(a, i)
        if len(current_numbers) > 1:
            unsolved_sectors += 1
        if verbose:
            print("Predictable numbers in S" + str(i) + " : " + str(current_numbers))
    print("Unsolved sectors                 : " + str(unsolved_sectors))


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


def count_zeros_in_rows(a: array, verbose: bool = False) -> int:
    count_nulls = 0
    for i in range(0, 9):
        count_nulls += count_zeros_in_row(a, i, verbose)
    return count_nulls


def count_zeros_in_columns(a: array, verbose: bool = False) -> int:
    count_nulls = 0
    for i in range(0, 9):
        count_nulls += count_zeros_in_column(a, i, verbose)
    return count_nulls


def count_zeros(a: array) -> int:
    """
    Count all zero numbers in the given matrix.
    :param a: A two-dimensional array with the sudoku data
    :return: The number of zeros in the matrix
    """
    return count_zeros_in_columns(a, False)


def count_non_zeros(a: array) -> int:
    """
    Count all non-zero numbers in the given matrix.
    :param a: A two-dimensional array with the sudoku data
    :return: The number of non-zeros in the matrix
    """
    return 81 - count_zeros_in_columns(a, False)


def count_zeros_in_sectors(a: array, verbose: bool = False) -> int:
    count_nulls = 0
    for i in range(1, 10):
        count_nulls += count_zeros_in_sector(a, i, verbose)
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


def predictable_numbers_in_position(a: array, row_index: int, column_index: int, verbose: bool = False) -> array:
    """
    Search a list of predictable numbers that can fit in the position of the sudoku matrix
    :param verbose: Show debug info
    :param a: A two-dimensional array with the sudoku data
    :param column_index: The column number to analyze
    :param row_index: The row number to analyze
    :return: All predictable numbers that may fit on this position in an array
    """
    if a[row_index, column_index] != zero:
        if verbose:
            print("Found value != " + str(zero) + " : " + str(a[row_index, column_index]))
            # print("Type a[column_index, row_index] : " + str(type(a[row_index, column_index])))
            # print("Type zero                       : " + str(type(zero)))
            print("row_index : " + str(row_index))
            print("column_index : " + str(column_index))
        return array([trunc(a[row_index, column_index])])
    numbers = numpy.intersect1d(predictable_numbers_in_column(a, column_index),
                                predictable_numbers_in_row(a, row_index))
    if verbose:
        print(
            "Predictable values in C" + str(column_index) + " : " + str(predictable_numbers_in_column(a, column_index)))
        print("Predictable values in R" + str(row_index) + " : " + str(predictable_numbers_in_row(a, row_index)))
        print(
            "Intersect between predictable values from C" + str(column_index) + " and R" + str(row_index) + " : " + str(
                numbers))
    numbers = numpy.intersect1d(numbers, predictable_numbers_in_sector(a, get_sector_id(row_index, column_index)))
    if verbose:
        print("pPedictable numbers in S" + str(get_sector_id(row_index, column_index)) + " : " + str(
            predictable_numbers_in_sector(a, get_sector_id(row_index, column_index))))
    return numbers


def save_predictable_numbers_in_positions(a: array, verbose: bool = False) -> int:
    """
    Search save predictable numbers that can fit in a position with a zero of the sudoku
    :param verbose: Show debug info
    :param a: A two-dimensional array with the sudoku data
    :return:
    """
    save_predictable_positions = 0
    for row_index in range(0, 9):
        for column_index in range(0, 9):
            if a[row_index, column_index] != 0:
                continue
            current_predictable_numbers = predictable_numbers_in_position(a, row_index, column_index)
            if len(current_predictable_numbers) == 1:
                save_predictable_positions += 1
            if verbose:
                print(
                    "R" + str(row_index + 1) + ", C" + str(column_index + 1) + " : " + str(current_predictable_numbers))
    # print("Unknown positions                : " + str(unknown_positions))
    return save_predictable_positions


def predictable_numbers_in_positions(a: array, verbose: bool = False):
    """
    Loop through all positions and print possible numbers which may fit.
    :param verbose: Show debug info
    :param a: A two-dimensional array with the sudoku data
    :return:
    """
    for row_index in range(0, 9):
        for column_index in range(0, 9):
            if a[row_index, column_index] != 0:
                if verbose:
                    print("R" + str(row_index + 1) + ", C" + str(column_index + 1) + " : "
                          + str(trunc(a[row_index, column_index])) + " *FIX*")
                continue
            current_predictable_numbers = predictable_numbers_in_position(a, row_index, column_index)
            print("R" + str(row_index + 1) + ", C" + str(column_index + 1) + " : " + str(current_predictable_numbers))


def get_best_position_indices_for_branching(a: array) -> []:
    """
    Search through all positions and return the row_index and column_index of the first position
    with the lowest count of possible numbers.
    :param a: A two-dimensional array with the sudoku data
    :return: A list with the row_index and the column_index
    """
    best_position = []
    current_possibilities = 10
    for row_index in range(0, 9):
        for column_index in range(0, 9):
            if a[row_index, column_index] != 0:
                continue
            current_predictable_numbers = predictable_numbers_in_position(a, row_index, column_index)
            if len(current_predictable_numbers) < current_possibilities:
                current_possibilities = len(current_predictable_numbers)
                best_position = [row_index, column_index]
                # When can quit here if we already found a position with the lowest possibilities (=2)
                if current_possibilities == 2:
                    return best_position
    return best_position


def analyze_sudoku(a, verbose: bool = False):
    """
    Prints out some structure analysis of the sudoku matrix in arg a
    :param a: A two-dimensional array with the sudoku data
    :param verbose: Show some debug info
    :return:
    """
    print("== Analyzing sudoku")
    #print("== Duplicate checking in rows")
    print("Found duplicates in rows         : " + str(rows_have_duplicates(a)))
    #print("== Duplicate checking in columns")
    print("Found duplicates in columns      : " + str(columns_have_duplicates(a)))
    #print("== Non-zero numbers in matrix")
    print("Non-zero numbers                 : " + str(count_non_zeros(a)))
    #print("== Save predictable numbers in positions")
    print("Save predicable positions        : "
          + str(save_predictable_numbers_in_positions(a, verbose)))
    #print("== Checking if sudoku is complete")
    print("Sudoku is comple                 : " + str(is_complete(a)))
    #print("== Checking if sudoku is deadlocked")
    print("Sudoku is deadlocked             : " + str(is_deadlocked(a)))


def fill_save_predictable_zeros(a: array, verbose: bool = False) -> array:
    """
    Calculate all predictable numbers for zeros in a given sudoku array and return the new array
    :param a: A two-dimensional array with the sudoku data
    :param verbose: Show debug info
    :return:
    """
    filled_array = numpy.copy(a)
    for column_index in range(0, 9):
        for row_index in range(0, 9):
            if filled_array[row_index, column_index] != zero:
                if verbose:
                    print(
                        "filled_array[row_index, column_index] != zero : " + str(filled_array[row_index, column_index]))
                continue
            current_predictable_numbers = predictable_numbers_in_position(a, row_index, column_index)
            if len(current_predictable_numbers) == 1:
                filled_array[row_index, column_index] = current_predictable_numbers[0]
            else:
                filled_array[row_index, column_index] = 0
            if verbose:
                print("R" + str(row_index + 1) + ", C" + str(column_index + 1) + " : " + str(
                    filled_array[row_index, column_index]))
    return filled_array


def is_complete(a: array, verbose: bool = False) -> bool:
    """
    Checks if there are unknown numbers in a sudoku matrix and returns False if there
    are any zeros in the matrix. Returns True if there are only non-zero numbers.
    :param a: A two-dimensional array with the sudoku data
    :return: True if the matrix has only non-zero numbers
    """
    for column_index in range(0, 9):
        for row_index in range(0, 9):
            if a[row_index, column_index] == zero:
                if verbose:
                    print("First zero number found at R" + str(row_index + 1) + ", C" + str(column_index + 1))
                return False
    return True


def is_deadlocked(a: array, verbose: bool = False) -> bool:
    """
    Checks if the matrix is in a deadlock state. This is when a position exists that has a number
    which is already used in a dependent row, column or sector.
    :param verbose: Show debug info
    :param a: A two-dimensional array with the sudoku data
    :return: True if the matrix is deadlocked
    """
    for column_index in range(0, 9):
        for row_index in range(0, 9):
            current_predictable_numbers = predictable_numbers_in_position(a, row_index, column_index)
            if len(current_predictable_numbers) == 0:
                if verbose:
                    print("Found deadlock in R" + str(row_index + 1) + ", C" + str(column_index + 1))
                return True
    return False


def main():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="read sudoku from FILE", metavar="FILE")
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose", default=False,
                      help="be verbose")

    (options, args) = parser.parse_args()

    _filename = "sudoku.txt"
    if options.filename:
        _filename = options.filename
    a = deserialize_array(_filename)

    _verbose = False
    if options.verbose:
        _verbose = options.verbose

    show(a)
    analyze_sudoku(a, _verbose)

    # Initialize the branch point tree with the root array
    branch_point_tree = BranchPointTree(a)
    branch_point_tree.print()

    # Main Loop to dive into the branch to the solution #
    current_branch_point = branch_point_tree.get_root()
    current_array = numpy.copy(a)
    iterations = 0
    while (not is_complete(current_array)
           and not is_deadlocked(current_array)
           and save_predictable_numbers_in_positions(current_array) > 0):
        current_array = fill_save_predictable_zeros(current_array, _verbose)
        iterations += 1
        print()
        print("== Iteration no " + str(iterations) + ":")
        show(current_array)
        analyze_sudoku(current_array, _verbose)

        if save_predictable_numbers_in_positions(current_array) == 0:
            print("== No position with save predictable numbers available.")
            current_best_position_indices_for_branching = get_best_position_indices_for_branching(current_array)
            current_best_position_possibilities = predictable_numbers_in_position(current_array,
                                                                                  current_best_position_indices_for_branching[
                                                                                      0],
                                                                                  current_best_position_indices_for_branching[
                                                                                      1])
            print("== Best first position indices for branching are "
                  + str(current_best_position_indices_for_branching))
            # predictable_numbers_in_positions(current_array)
            if len(current_best_position_indices_for_branching) == 0:
                print("== NO BRANCH POSITION FOUND")
                break
            print("== Creating new branch point")
            branch_point_tree.add_branch_point(BranchPoint(current_array,
                                                           parent_id=current_branch_point.get_id(),
                                                           branch_position_row_index=
                                                           current_best_position_indices_for_branching[0],
                                                           branch_position_column_index=
                                                           current_best_position_indices_for_branching[1],
                                                           initial_possibilities=current_best_position_possibilities))
            print("##########")
            branch_point_tree.print()
            sys.exit()

    print()

    print("Operation stopped.")
    print("Iterations done : " + str(iterations))
    if is_deadlocked(current_array):
        print("Sudoku is deadlocked:")
        is_deadlocked(current_array, True)
    if is_complete(current_array):
        print("Bingo! Sudoku is complete.")
    if save_predictable_numbers_in_positions(current_array) == 0:
        print("No save predictable numbers found.")
        # branch_point_tree.add_branch_point(BranchPoint(current_array, parent_id=current_branch_point.get_id()))
        # branch_point_tree.print()


if __name__ == '__main__':
    main()
