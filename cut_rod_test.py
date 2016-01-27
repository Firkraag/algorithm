#!/usr/bin/env ipython
import unittest

from cut_rod import bottom_up_cut_rod, bottom_up_cut_rod_two_subproblem, memoized_cut_rod, print_cut_rod_solution, bottom_up_cut_rod_with_fixed_cut_cost, extended_memoized_cut_rod

class TestCutRod(unittest.TestCase):
    def test_bottom_up_cut_rod(self):
        p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        values = [1, 1, 2, 5, 3, 8, 4, 10, 5, 13, 6, 17, 7, 18, 8, 22, 9, 25, 10, 30]
        for i in range(0, len(values), 2):
            self.assertEquals(bottom_up_cut_rod(p, values[i]), values[i + 1])
    def test_bottom_up_cut_rod_two_subproblem(self):
        p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        values = [1, 1, 2, 5, 3, 8, 4, 10, 5, 13, 6, 17, 7, 18, 8, 22, 9, 25, 10, 30]
        for i in range(0, len(values), 2):
            self.assertEquals(bottom_up_cut_rod_two_subproblem(p, values[i]), values[i + 1])
    def test_memoized_cut_rod(self):
        p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        values = [1, 1, 2, 5, 3, 8, 4, 10, 5, 13, 6, 17, 7, 18, 8, 22, 9, 25, 10, 30]
        for i in range(0, len(values), 2):
            self.assertEquals(memoized_cut_rod(p, values[i]), values[i + 1])
    def test_bottom_up_cut_rod_with_fixed_cut_cost(self):
        p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        values = [1, 1, 2, 5, 3, 8, 4, 9, 5, 11, 6, 17, 7, 17, 8, 20, 9, 24, 10, 30]
        for i in range(0, len(values), 2):
            self.assertEquals(bottom_up_cut_rod_with_fixed_cut_cost(p, values[i], 2), values[i + 1])
        values = [1, 1, 2, 5, 3, 8, 4, 9, 5, 11.5, 6, 17, 7, 17, 8, 20.5, 9, 24, 10, 30]
        for i in range(0, len(values), 2):
            self.assertEquals(bottom_up_cut_rod_with_fixed_cut_cost(p, values[i], 1.5), values[i + 1])
    def test_print_rod_solution(self):
        p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        values = [1, 1, 2, 5, 3, 8, 4, 10, 5, 13, 6, 17, 7, 18, 8, 22, 9, 25, 10, 30]
        print_cut_rod_solution(p, 9, extended_memoized_cut_rod)
