import unittest

from LeetCodeSolution import read_all_file
from LeetCodeSolution import read_all_lines_from_file
from LeetCodeSolution import merge_solutions
LEETCODE_END_LINK = '\n[comment]: <> (Stop)\n'

class TestGenerator(unittest.TestCase):
    def test_read_all_file(self):
        expect = "My first name is\n\n[comment]: <> (Stop)\n\nMy second name is"
        result = read_all_file("input.txt")
        self.assertEqual(expect, result)

    def test_read_all_lines_form_file(self):
        expect = ["My first name is\n", "\n", "[comment]: <> (Stop)\n", "\n", "My second name is"]
        result = read_all_lines_from_file("input.txt")
        self.assertEqual(expect, result)

    def test_merge_solutions(self):
        expect = "My first name is\nsecond\nMy second name is"
        result = merge_solutions(read_all_file("input.txt"), "second")
        self.assertEqual(expect, result)