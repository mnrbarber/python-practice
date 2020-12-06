"""Implementing a binary search algorithm on a list"""
import math
from random import randint
from unittest import TestCase


class BinarySearchTestCase(TestCase):
    def setUp(self):
        self.list = [randint(0, 100) for _ in range(100)]
        self.list.sort()
        self.search_index = 61
        self.search_in_list = self.list[self.search_index]
        self.search_not_in_list = 101

    def test_in_list(self):
        """Test to check something that is in the list"""
        is_found, index = binary_search(self.list, self.search_in_list)
        self.assertTrue(is_found)
        self.assertEqual(self.search_index, index)

    def test_not_in_list(self):
        """Test to check something that is not in the list"""
        is_found, index = binary_search(self.list, self.search_not_in_list)
        self.assertFalse(is_found)
        self.assertIsNone(index)


def binary_search(search_list, search_int):
    """Implement a binary search algorithm to return boolean if found and index at which found"""
    left_ind = 0
    right_ind = len(search_list) - 1
    x = math.floor((left_ind + right_ind) / 2)
    while search_list[x] != search_int and right_ind != left_ind:
        if search_list[x] < search_int:
            left_ind = x + 1
        else:
            right_ind = x - 1
        x = math.floor((left_ind + right_ind) / 2)
    if search_list[x] == search_int:
        return True, x
    return False, None
