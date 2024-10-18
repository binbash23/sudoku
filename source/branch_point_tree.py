"""

20241017 jens heine <binbash@gmx.net>

branch_point_tree.py

"""
import numpy
from numpy import array
from branch_point import BranchPoint
from uuid import uuid4

class BranchPointTree:

    _branch_point_array = []


    def __init__(self, root_array: array):
        root_branch_point = BranchPoint(root_array, is_root=True)
        self._branch_point_array = self._branch_point_array + [root_branch_point]


    def print(self):
        print()
        print("Branch point tree (" + str(self.get_size()) + " elements)")
        i=0
        while i < self.get_size():
            print()
            print(str(i+1) + ". Element:\n")
            if self._branch_point_array[i] is not None:
                self._branch_point_array[i].print()
            i+=1
        print()


    def add_branch_point(self, branch_point: BranchPoint):
        self._branch_point_array = self._branch_point_array + [branch_point]


    def get_size(self) -> int:
        return len(self._branch_point_array)


    def get_branch_point(self, branch_point_id: uuid4) -> BranchPoint|None:
        i=0
        while i < self.get_size():
            if self._branch_point_array[i].get_id() == branch_point_id:
                return self._branch_point_array[i]
            i+=1
        return None


    def get_parent_of(self, branch_point: BranchPoint) -> BranchPoint|None:
        parent_id = branch_point.get_parent_id()
        return self.get_branch_point(parent_id)


    def get_root(self) -> BranchPoint|None:
        i=0
        while i < self.get_size():
            if self._branch_point_array[i].is_root():
                return self._branch_point_array[i]
            i+=1
        return None
