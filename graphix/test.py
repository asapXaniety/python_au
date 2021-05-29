import unittest
from graphix.main import *


class TestGr(unittest.TestCase):
    def test_from_str_to_dict(self):
        lst = ['date, resource, staff_id, count\n', '2020-01, 1, 120, 15\n', '2020-02, 1, 21, 20\n', '2020-03, 3, 25, 29\n', '2020-04, 2, 21, 38\n', '2020-05, 3, 24, 44\n']
        result = convert_to_dict(lst)
        print(result)
        expect = [{'date': '2020-01', 'resource': '1', 'staff_id': '120', 'count\n': '15\n'}, {'date': '2020-02', 'resource': '1', 'staff_id': '21', 'count\n': '20\n'}, {'date': '2020-03', 'resource': '3', 'staff_id': '25', 'count\n': '29\n'}, {'date': '2020-04', 'resource': '2', 'staff_id': '21', 'count\n': '38\n'}, {'date': '2020-05', 'resource': '3', 'staff_id': '24', 'count\n': '44\n'}]
        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()