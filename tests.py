import unittest

from bucket_sort import bucket_sort
from intro_sort import IntroSort
from merge_sort import merge_sort
from radix_sort import radix_sort
from smoothsort import smoothsort
from sorts import *
from timsort import timsort
from tree_sort import tree_sort

TEST_LIST = [18, 22, 19, 36, 99, 115, 8, 54, 20, 55, 1, 6, 93, 23, 5]
TEST_LIST_INCREASING = [1, 5, 6, 8, 18, 19, 20, 22, 23, 36, 54, 55, 93, 99, 115]
FULL_TIME = dict()


class TestHeapSort(unittest.TestCase):
    def test_increasing(self):
        self.assertEqual(heap_sort(TEST_LIST), TEST_LIST_INCREASING)


class TestMergeSort(unittest.TestCase):
    def test_increasing(self):
        self.assertEqual(merge_sort(TEST_LIST), TEST_LIST_INCREASING)


class TestRadixSort(unittest.TestCase):
    def test_increasing(self):
        self.assertEqual(radix_sort(TEST_LIST), TEST_LIST_INCREASING)


class TestSmoothSort(unittest.TestCase):
    def test_increasing(self):
        self.assertEqual(smoothsort(TEST_LIST), TEST_LIST_INCREASING)



class TestTimSort(unittest.TestCase):
    def test_increasing(self):
        self.assertEqual(timsort(TEST_LIST), TEST_LIST_INCREASING)



class TestTreeSort(unittest.TestCase):
    def test_increasing(self):
        self.assertEqual(tree_sort(TEST_LIST), TEST_LIST_INCREASING)



class TestBucketSort(unittest.TestCase):
    def test_increasing(self):
        self.assertEqual(bucket_sort(TEST_LIST), TEST_LIST_INCREASING)


class TestIntroSort(unittest.TestCase):
    def test_increasing(self):
        TEST_LIST_INTRO_SORT = TEST_LIST
        IntroSort().introsort(TEST_LIST_INTRO_SORT)
        self.assertEqual(TEST_LIST_INTRO_SORT, TEST_LIST_INCREASING)



class TestBubbleSort(unittest.TestCase):
    def test_increasing(self):
        self.assertEqual(bubble_sort(TEST_LIST), TEST_LIST_INCREASING)



class TestCocktailSort(unittest.TestCase):
    def test_increasing(self):
        self.assertEqual(cocktail_sort(TEST_LIST), TEST_LIST_INCREASING)



class TestInsertionSort(unittest.TestCase):
    def test_increasing(self):
        self.assertEqual(bubble_sort(TEST_LIST), TEST_LIST_INCREASING)



class TestGnomeSort(unittest.TestCase):
    def test_increasing(self):
        self.assertEqual(gnome_sort(TEST_LIST), TEST_LIST_INCREASING)



class TestSelectionSort(unittest.TestCase):
    def test_increasing(self):
        self.assertEqual(selection_sort(TEST_LIST), TEST_LIST_INCREASING)


class TestCombSort(unittest.TestCase):
    def test_increasing(self):

        self.assertEqual(comb_sort(TEST_LIST), TEST_LIST_INCREASING)



class TestShellSort(unittest.TestCase):
    def test_increasing(self):

        self.assertEqual(shell_sort(TEST_LIST), TEST_LIST_INCREASING)



class TestQuickSort(unittest.TestCase):
    def test_increasing(self):

        self.assertEqual(quicksort(TEST_LIST), TEST_LIST_INCREASING)



class TestCountingSort(unittest.TestCase):
    def test_increasing(self):
        self.assertEqual(counting_sort(TEST_LIST), TEST_LIST_INCREASING)



if __name__ == "__main__":
    unittest.main()
    print(FULL_TIME)

