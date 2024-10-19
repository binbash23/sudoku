"""

20241017 jens heine <binbash@gmx.net>

branch_point_tree.py

"""
from numpy import array
from branch_point import BranchPoint
from uuid import uuid4


class BranchPointTree:
    _branch_point_array = []

    def __init__(self, root_array: array):
        """
        Create a branch_point_tree object. The root branch point object will be generated from
        the given array.
        :param root_array: The root sudoku array
        """
        root_branch_point = BranchPoint(root_array, is_root=True)
        self._branch_point_array = self._branch_point_array + [root_branch_point]

    def print(self):
        """
        Print out some information about this branch point tree object which also
        lists all contained branch point information.
        :return:
        """
        print()
        print("Branch point tree (" + str(self.get_size()) + " elements)")
        i = 0
        while i < self.get_size():
            print()
            print(str(i + 1) + ". Element:\n")
            if self._branch_point_array[i] is not None:
                self._branch_point_array[i].print()
            i += 1
        print()

    def exists(self, branch_point: BranchPoint) -> bool:
        """
        Check if a branch point already exists in the branch point tree
        :param branch_point:
        :return: True if the new branch point already exists in the tree
        """
        i = 0
        while i < self.get_size():
            if self._branch_point_array[i] == branch_point:
                return True
            i += 1
        return False

    def add_branch_point(self, branch_point: BranchPoint):
        """
        Add a new branch point object to this tree
        :param branch_point: The new branch point
        :return:
        """
        if self.exists(branch_point):
            raise Exception("Branch point already exists.")
        self._branch_point_array = self._branch_point_array + [branch_point]

    def get_size(self) -> int:
        """
        Return the number of branch points in the tree.
        :return: The number of branch points in this tree
        """
        return len(self._branch_point_array)

    def get_branch_point(self, branch_point_id: uuid4) -> BranchPoint | None:
        """
        Get a branch point by id.
        :param branch_point_id: The id to be returned
        :return: If found, the branch point with the given id
        """
        i = 0
        while i < self.get_size():
            if self._branch_point_array[i].get_id() == branch_point_id:
                return self._branch_point_array[i]
            i += 1
        return None

    def get_parent_of(self, branch_point: BranchPoint) -> BranchPoint | None:
        """
        Get the parent branch point of the given branch point.
        :param branch_point: The child branch point to get the parent from
        :return: The parent branch point if it exists or None
        """
        parent_id = branch_point.get_parent_id()
        return self.get_branch_point(parent_id)

    def get_root(self) -> BranchPoint | None:
        """
        Get the root branch point of this tree.
        :return: The root branch point
        """
        i = 0
        while i < self.get_size():
            if self._branch_point_array[i].is_root():
                return self._branch_point_array[i]
            i += 1
        return None

    def get_depth(self, branch_point) -> int:
        """
        Get the depth of the given branch point relative to the root branch point
        :param branch_point:
        :return: The depth level
        """
        current_branch_point = branch_point
        level = 0
        parent_id = current_branch_point.get_parent_id
        while parent_id is not None:
            level += 1
            current_branch_point = self.get_parent_of(current_branch_point)
            if current_branch_point:
                parent_id = current_branch_point.get_id()
            else:
                parent_id = None
        return level




