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


    def __init__(self, a: array, branch_position_row_index: int = -1, branch_position_column_index = -1,
                 is_root: bool = False, initial_possibilities:array=array([]),
                 # possibilities_left:array=array([]),
                 parent_id: uuid4=None):
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
        print("Sudoku branch point")
        print()
        print("Sudoku matrix:")
        print(self._a)
        print()
        print("Parent ID              : " + str(self._parent_id))
        print("ID                     : " + str(self._id))
        print("Root                   : " + str(self._is_root))
        print("Branch position row    : " + str(self._branch_position_row_index))
        print("Branch position column : " + str(self._branch_position_column_index))
        print("Initial possibilities  : " + str(self._initial_possibilities))
        print("Possibilities left     : " + str(self._possibilities_left))


    def get_branch_position_row(self) -> int:
        if self._branch_position_row_index > -1:
            return self._branch_position_row_index+1
        else:
            return -1


    def get_branch_position_column(self) -> int:
        if self._branch_position_column_index > -1:
            return self._branch_position_column_index+1
        else:
            return -1


    def get_initial_possibilities(self) -> array:
        return self._initial_possibilities


    def get_possibilities_left(self) -> array:
        return self._possibilities_left


    def get_id(self) -> uuid4:
        return self._id


    def has_possibilities_left(self) -> bool:
        if len(self.get_possibilities_left()) > 0:
            return True
        else:
            return False


    def is_root(self) -> bool:
        return self._is_root


    def get_parent_id(self) -> uuid4:
        return self._parent_id


    def pop_possibility_left(self) -> int|None:
        possibility=None
        if self.has_possibilities_left():
            possibility = self._possibilities_left[0]
            self._possibilities_left = numpy.delete(self._possibilities_left, 0)
        return possibility


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
    bp_array = array([ copy.deepcopy(bp)])
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

