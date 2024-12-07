import unittest

def merge(left, right):
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if list(left.values())[i] < list(right.values())[j]:
            sorted_array.append([list(left.keys())[i], list(left.values())[i]])
            i += 1
        else:
            sorted_array.append([list(right.keys())[j], list(right.values())[j]])
            j += 1

    while i < len(left):
        sorted_array.append([list(left.keys())[i], list(left.values())[i]])
        i += 1

    while j < len(right):
        sorted_array.append([list(right.keys())[j], list(right.values())[j]])
        j += 1

    return dict(sorted_array)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(dict(list(arr.items())[:mid]))
    right_half = merge_sort(dict(list(arr.items())[mid:]))

    return merge(left_half, right_half)

class TestMergeSort(unittest.TestCase):

    def test_merge_sort_basic(self):
        input_data = {1: 5, 2: 3, 3: 1, 4: 4, 5: 2}
        expected_output = {3: 1, 5: 2, 2: 3, 4: 4, 1: 5}
        self.assertEqual(merge_sort(input_data), expected_output)

    def test_merge_sort_already_sorted(self):
        input_data = {1: 1, 2: 2, 3: 3}
        expected_output = {1: 1, 2: 2, 3: 3}
        self.assertEqual(merge_sort(input_data), expected_output)

    def test_merge_sort_reverse_sorted(self):
        input_data = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}
        expected_output = {5: 1, 4: 2, 3: 3, 2: 4, 1: 5}
        self.assertEqual(merge_sort(input_data), expected_output)

    def test_merge_sort_single_element(self):
        input_data = {1: 42}
        expected_output = {1: 42}
        self.assertEqual(merge_sort(input_data), expected_output)

    def test_merge_sort_empty(self):
        input_data = {}
        expected_output = {}
        self.assertEqual(merge_sort(input_data), expected_output)

    def test_merge_sort_with_duplicates(self):
        input_data = {1: 3, 2: 1, 3: 2, 4: 2}
        expected_output = {2: 1, 3: 2, 4: 2, 1: 3}
        self.assertEqual(merge_sort(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()
