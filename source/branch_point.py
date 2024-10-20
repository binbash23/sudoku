"""

20241017 jens heine <binbash@gmx.net>

branch_point.py

"""
from xmlrpc.client import Boolean

import numpy
from numpy import array
from uuid import uuid4
import copy


class BranchPoint:
    _a: array = None
    _is_root: bool = False
    _branch_position_row_index: int = -1
    _branch_position_column_index: int = -1
    _initial_possibilities: array = array([])
    _possibilities_left: array = array([])
    _id: uuid4 = None
    _parent_id = None

    def __init__(self, a: array, branch_position_row_index: int = -1, branch_position_column_index=-1,
                 is_root: bool = False, initial_possibilities: array = array([]),
                 parent_id: uuid4 = None):
        """
        The constructor creates a new branch_point object, which can be a root branch point or a non-root
        branch point. The non-root branch point holds information like a copy of the sudoku matrix at
        creation time. Also the best position identified by row_index and column_index to go on trying.
        The possible numbers are remembered, too. The parent id points to the parent branch point of this
        one, to be able to follow the tree up to the root branch point from any leaf. It is possible to
        pop out one possible number after another to try one solution number and get back if this was not
        the right one - and then pop out the next number to try.
        :param a: A two-dimensional array with the sudoku data
        :param branch_position_row_index: row index of the position to dive into
        :param branch_position_column_index: column index of the position to dive into
        :param is_root: True if this should be the root branch point
        :param initial_possibilities: initial possible numbers on the position to try
        :param parent_id: The id of the parent branch point
        """
        self._a = numpy.copy(a)
        self._is_root = is_root
        self._branch_position_row_index = branch_position_row_index
        self._branch_position_column_index = branch_position_column_index
        self._initial_possibilities = numpy.copy(initial_possibilities)
        self._possibilities_left = numpy.copy(initial_possibilities)
        self._id = uuid4()
        self._parent_id = parent_id

    # def __str__(self):
    def print(self):
        """
        Print out the information of this branch point
        :return:
        """
        print("Sudoku branch point")
        print()
        print("Sudoku matrix:")
        print(self._a)
        print()
        print("Parent ID              : " + str(self._parent_id))
        print("ID                     : " + str(self._id))
        print("Root                   : " + str(self._is_root))
        print("Branch position row    : " + str(self.get_branch_position_row()))
        print("Branch position column : " + str(self.get_branch_position_column()))
        print("Initial possibilities  : " + str(self._initial_possibilities))
        print("Possibilities left     : " + str(self._possibilities_left))

    def get_branch_info(self):
        """
        Get the branch information in this format R4, C4: [2 6 8]
        :return: The info string
        """
        return ("R" + str(self.get_branch_position_row()) + ", C" + str(self.get_branch_position_column()) +
                ": " + str(self.get_initial_possibilities()))

    def get_branch_position_row(self) -> int:
        """
        Get the branch position row number (1-9) or -1 if not set.
        :return:
        """
        if self._branch_position_row_index > -1:
            return self._branch_position_row_index + 1
        else:
            return -1

    def get_branch_position_row_index(self) -> int:
        """
        Get the branch position row index (0-8) or -1 if not set.
        :return:
        """
        if self._branch_position_row_index > -1:
            return self._branch_position_row_index
        else:
            return -1

    def get_branch_position_column_index(self) -> int:
        """
        Get the branch position column index (0-8) or -1 if not set.
        :return:
        """
        if self._branch_position_column_index > -1:
            return self._branch_position_column_index
        else:
            return -1

    def get_branch_position_column(self) -> int:
        """
        Get the branch position column number (1-9) or -1 if not set.
        :return:
        """
        if self._branch_position_column_index > -1:
            return self._branch_position_column_index + 1
        else:
            return -1

    def get_initial_possibilities(self) -> array:
        """
        Get the array with the initial possible numbers of the position which can be tried
        our from this branch point.
        :return:
        """
        return self._initial_possibilities

    def get_possibilities_left(self) -> array:
        """
        Get the array with the numbers left to try for the position of this branch point
        which ave not been tried out.
        :return:
        """
        return self._possibilities_left

    def get_id(self) -> uuid4:
        """
        Get the id of this branch point.
        :return: the id of the branch point
        """
        return self._id

    def has_possibilities_left(self) -> bool:
        """
        Return True if there are some possible numbers left to try out.
        :return: True if there are some un-tried numbers left
        """
        if len(self.get_possibilities_left()) > 0:
            return True
        else:
            return False

    def is_root(self) -> bool:
        """
        Checks if this branch point is the root branch point.
        :return: True if this branch point is the root
        """
        return self._is_root

    def get_parent_id(self) -> uuid4:
        """
        Get the id of the parent branch point if it exists.
        :return: The id of the parent branch point if this is not the root
        """
        return self._parent_id

    def pop_possible_number(self) -> int | None:
        """
        Pop the next possible number that can be tried out for the position of this branch point.
        The number will be removed from the list of possible numbers.
        :return: A possible number that can be tried or None
        """
        possibility = None
        if self.has_possibilities_left():
            # possibility = self._possibilities_left[len(self._possibilities_left)-1]
            # self._possibilities_left = numpy.delete(self._possibilities_left, len(self._possibilities_left)-1)

            possibility = self._possibilities_left[0]
            self._possibilities_left = numpy.delete(self._possibilities_left, 0)
        return possibility

    def get_array(self) -> array:
        """
        Get a copy of the array/matrix with the sudoku data.
        :return: The sudoku array
        """
        return numpy.copy(self._a)

    def __eq__(self, other):
        """
        Compare two BranchPoints whether the array and the branch coordinates are equal.
        :param other: Another branch point object
        :return: True if the arrays and branch point coordinates are the same
        """
        if isinstance(other, BranchPoint):
            if (numpy.array_equal(self._a, other._a) and self.get_branch_position_row() == other.get_branch_position_row()
                    and self.get_branch_position_column() == other.get_branch_position_column()):
                # print("First array:")
                # print(self._a)
                # print("First coordinates:")
                # print("R" + str(self.get_branch_position_row()) + ", C" + str(self.get_branch_position_column()))
                #
                # print("Second array:")
                # print(other._a)
                # print("Second coordinates:")
                # print("R" + str(other.get_branch_position_row()) + ", C" + str(other.get_branch_position_column()))
                return True
            else:
                return False
        else:
            return NotImplemented


def main():
    a = array([1])
    bp = BranchPoint(a, is_root=True)
    #print(bp)
    bp.print()
    print("=======")
    print(str(bp.get_id()))

    #bp_array = array([bp])
    #bp_array = array([])
    #bp_array = bp_array + [copy.deepcopy(bp)]
    bp_array = array([copy.deepcopy(bp)])
    bp_array = [copy.deepcopy(bp)]

    print("==")
    print("type: " + str(type(bp_array)))
    print("type: " + str(type(bp_array[0])))
    print("==")
    #print("id: " + str(BranchPoint(bp_array[0]).get_id()))
    bp_array[0].print()


if __name__ == '__main__':
    main()

    # def get_parent_branch_point(branch_point: SudokuBranchPoint, branch_point_array: array([SudokuBranchPoint]) -> SudokuBranchPoint:
