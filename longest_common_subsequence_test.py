#!/usr/bin/env ipython
import unittest
from longest_common_subsequence import lcs_length_one_row, lcs_length

class TestLCS(unittest.TestCase):
    def test_lcs_length(self):
        X = "ABCBDAB"
        Y = "BDCABA"
        c,b = lcs_length(X, Y)
        self.assertEquals(c[len(X), len(Y)], 4)
        X = [1, 0, 0, 1, 0, 1, 0, 1]
        Y = [0, 1, 0, 1, 1, 0, 1, 1, 0]
        c,b = lcs_length(X, Y)
        self.assertEquals(c[len(X), len(Y)], 6)
        X = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
        Y = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
        c,b = lcs_length(X, Y)
        self.assertEquals(c[len(X), len(Y)], 20)
    def test_lcs_length_one_row(self):
        X = "ABCBDAB"
        Y = "BDCABA"
        self.assertEquals(lcs_length_one_row(X, Y), 4)
        X = [1, 0, 0, 1, 0, 1, 0, 1]
        Y = [0, 1, 0, 1, 1, 0, 1, 1, 0]
        self.assertEquals(lcs_length_one_row(X, Y), 6)
        X = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
        Y = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
        self.assertEquals(lcs_length_one_row(X, Y), 20)
