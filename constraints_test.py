from constraints import difference_constraints, equality_constraints, difference_constraints_without_aux_vertex, single_variable_constraints, difference_constraints_with_arbitrary_weight
import unittest
from math import floor

class TestConstraints(unittest.TestCase):
    def test_difference_constraints(self):
        A = [[1, -1, 0, 0, 0], [1, 0, 0, 0, -1], [0, 1, 0, 0, -1], [-1, 0, 1, 0, 0], [-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [0, 0, -1, 0, 1], [0, 0, 0, -1, 1]]
        b = [0, -1, 1, 5, 4, -1, -3, -3]
        self.assertEquals(difference_constraints(A, b), [-5, -3, 0, -1, -4])
        A = [[1, -1, 0, 0, 0, 0], [1, 0, 0, -1, 0, 0], [0, 1, -1, 0, 0, 0], [0, 1, 0, 0, -1, 0], [0, 1, 0, 0, 0, -1], [0, 0, 1, 0, 0, -1], [0, -1, 0, 1, 0, 0], [-1, 0, 0, 0, 1, 0], [0, 0, 0, -1, 1, 0], [0, 0, -1, 0, 0, 1]]
        b = [1, -4, 2, 7, 5, 10, 2, -1, 3, -8]
        self.assertEquals(difference_constraints(A, b), [-5, -3, 0, -1, -6, -8])
        A = [[1, -1, 0, 0, 0], [1, 0, 0, 0, -1], [0, 1, 0, -1, 0], [0, -1, 1, 0, 0], [-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [0, 0, 0, 1, -1], [0, 0, -1, 0, 1], [0, 0, 0, -1, 1]]
        b = [4, 5, -6, 1, 3, 5, 10, -4, 8]
        self.assertEquals(difference_constraints(A, b), None)
        A = [[1, -1, 0, 0, 0, 0], [1, 0, 0, -1, 0, 0], [0, 1, -1, 0, 0, 0], [0, 1, 0, 0, -1, 0], [0, 1, 0, 0, 0, -1], [0, 0, 1, 0, 0, -1], [0, -1, 0, 1, 0, 0], [-1, 0, 0, 0, 1, 0], [0, 0, 0, -1, 1, 0], [0, 0, -1, 0, 0, 1]]
        b = [1, -4, 2, 7.3, 5, 10.1, 2.9, -1.11, 3, -8.6]
        c = [int(floor(i)) for i in b]
        print difference_constraints(A, c)

    def test_equality_constraints(self):
        A = [[1, -1, 0, 0, 0], [1, 0, 0, 0, -1], [0, 1, 0, 0, -1], [-1, 0, 1, 0, 0], [-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [0, 0, -1, 0, 1], [0, 0, 0, -1, 1]]
        b = [0, -1, 1, 5, 4, -1, -3, -3]
        self.assertEquals(equality_constraints(A, b), None)
        A = [[1, -1, 0, 0, 0, 0], [1, 0, 0, -1, 0, 0], [0, 1, -1, 0, 0, 0], [0, 1, 0, 0, -1, 0], [0, 1, 0, 0, 0, -1], [0, 0, 1, 0, 0, -1], [0, -1, 0, 1, 0, 0], [-1, 0, 0, 0, 1, 0], [0, 0, 0, -1, 1, 0], [0, 0, -1, 0, 0, 1]]
        b = [1, -4, 2, 7, 5, 10, 2, -1, 3, -8]
        self.assertEquals(equality_constraints(A, b), None)
        A = [[1, -1, 0, 0, 0], [1, 0, 0, 0, -1], [0, 1, 0, -1, 0], [0, -1, 1, 0, 0], [-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [0, 0, 0, 1, -1], [0, 0, -1, 0, 1], [0, 0, 0, -1, 1]]
        b = [4, 5, -6, 1, 3, 5, 10, -4, 8]
        self.assertEquals(equality_constraints(A, b), None)
        A = [[-1, 1, 0], [0, -1, 1], [-1, 0, 1]]
        b = [1, 1, 2]
        self.assertEquals(equality_constraints(A, b), [-2, -1, 0])
    def test_difference_constraints_without_aux_vertex(self):
        A = [[1, -1, 0, 0, 0], [1, 0, 0, 0, -1], [0, 1, 0, 0, -1], [-1, 0, 1, 0, 0], [-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [0, 0, -1, 0, 1], [0, 0, 0, -1, 1]]
        b = [0, -1, 1, 5, 4, -1, -3, -3]
        self.assertEquals(difference_constraints_without_aux_vertex(A, b), [-5, -3, 0, -1, -4])
        A = [[1, -1, 0, 0, 0, 0], [1, 0, 0, -1, 0, 0], [0, 1, -1, 0, 0, 0], [0, 1, 0, 0, -1, 0], [0, 1, 0, 0, 0, -1], [0, 0, 1, 0, 0, -1], [0, -1, 0, 1, 0, 0], [-1, 0, 0, 0, 1, 0], [0, 0, 0, -1, 1, 0], [0, 0, -1, 0, 0, 1]]
        b = [1, -4, 2, 7, 5, 10, 2, -1, 3, -8]
        self.assertEquals(difference_constraints_without_aux_vertex(A, b), [-5, -3, 0, -1, -6, -8])
        A = [[1, -1, 0, 0, 0], [1, 0, 0, 0, -1], [0, 1, 0, -1, 0], [0, -1, 1, 0, 0], [-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [0, 0, 0, 1, -1], [0, 0, -1, 0, 1], [0, 0, 0, -1, 1]]
        b = [4, 5, -6, 1, 3, 5, 10, -4, 8]
        self.assertEquals(difference_constraints_without_aux_vertex(A, b), None)
    def test_single_variable_constraints(self):
        A = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 0]]
        b = [3, 1, 5, -1, 2]
        self.assertEquals(single_variable_constraints(A, b), [2, 1])
        A = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 0]]
        b = [3, -1, 5, -1, 2]
        self.assertEquals(single_variable_constraints(A, b), None)
#    def test_difference_constraints_with_arbitrary_weight(self):
#        A = [[1, -1, 0, 0, 0], [1, 0, 0, 0, -1], [0, 1, 0, 0, -1], [-1, 0, 1, 0, 0], [-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [0, 0, -1, 0, 1], [0, 0, 0, -1, 1]]
#        b = [0, -1, 1, 5, 4, -1, -3, -3]
#        self.assertEquals(difference_constraints_with_arbitrary_weight(A, b), [-5, -3, 0, -1, -4])
#        A = [[1, -1, 0, 0, 0, 0], [1, 0, 0, -1, 0, 0], [0, 1, -1, 0, 0, 0], [0, 1, 0, 0, -1, 0], [0, 1, 0, 0, 0, -1], [0, 0, 1, 0, 0, -1], [0, -1, 0, 1, 0, 0], [-1, 0, 0, 0, 1, 0], [0, 0, 0, -1, 1, 0], [0, 0, -1, 0, 0, 1]]
#        b = [1, -4, 2, 7, 5, 10, 2, -1, 3, -8]
#        self.assertEquals(difference_constraints_with_arbitrary_weight(A, b), [-5, -3, 0, -1, -6, -8])
#        A = [[1, -1, 0, 0, 0], [1, 0, 0, 0, -1], [0, 1, 0, -1, 0], [0, -1, 1, 0, 0], [-1, 0, 0, 1, 0], [0, 0, -1, 1, 0], [0, 0, 0, 1, -1], [0, 0, -1, 0, 1], [0, 0, 0, -1, 1]]
#        b = [4, 5, -6, 1, 3, 5, 10, -4, 8]
#        self.assertEquals(difference_constraints_with_arbitrary_weight(A, b), None)

