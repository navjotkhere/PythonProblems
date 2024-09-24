#
#  Homework - Quadratic Sorts
#
#  Problem 1: Insertion Sort
#
#  Prompt:    Given an unsorted list of integers, return the list sorted
#             using insertion sort.
#
#             What are the time and auxilliary space complexity?
#
#  Input:     input {List}
#  Output:    {List}
#
#  Example:   [3,9,1,4,7] --> [1,3,4,7,9]
#
#
#  Problem 2: Selection Sort
#
#  Prompt:    Given an unsorted list of integers, return the list sorted
#             using selection sort.
#
#             What are the time and auxilliary space complexity?
#
#  Input:     input {List}
#  Output:    {List}
#
#  Example:   [3,9,1,4,7] --> [1,3,4,7,9]
#
#
#  Problem 3: Bubble Sort
#
#  Prompt:    Given an unsorted list of integers, return the list sorted
#             using bubble sort.
#
#             What are the time and auxilliary space complexity?
#
#  Input:     input {List}
#  Output:    {List}
#
#  Example:   [3,9,1,4,7] --> [1,3,4,7,9]
#


# Time Complexity:
# Auxiliary Space Complexity:
def insertion_sort(input):
    # YOUR WORK HERE
    pass


# Time Complexity:
# Auxiliary Space Complexity:
def selection_sort(input):
    # YOUR WORK HERE
    pass


# Time Complexity:
# Auxiliary Space Complexity:
def bubble_sort(input):
    # YOUR WORK HERE
    pass


# ###########################################################
# ##############  DO NOT TOUCH TEST BELOW!!!  ###############
# ###########################################################


from io import StringIO
import sys
import random


# custom assert function to handle tests
# input: count {List} - keeps track out how many tests pass and how many total
#        in the form of a two item array i.e., [0, 0]
# input: name {String} - describes the test
# input: test {Function} - performs a set of operations and returns a boolean
#        indicating if test passed
# output: {None}
def expect(count, name, test):
    if (count is None or not isinstance(count, list) or len(count) != 2):
        count = [0, 0]
    else:
        count[1] += 1

    result = 'false'
    error_msg = None
    try:
        if test():
            result = ' true'
            count[0] += 1
    except Exception as err:
        error_msg = str(err)

    print('  ' + (str(count[1]) + ')   ') + result + ' : ' + name)
    if error_msg is not None:
        print('       ' + error_msg + '\n')


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


# compare if two flat lists are equal
def lists_equal(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(0, len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True


print('Insertion Sort Tests')
test_count = [0, 0]


def test():
    example = insertion_sort([3, 9, 1, 4, 7])
    return example is not None and lists_equal(example, [1, 3, 4, 7, 9])


expect(test_count, 'should sort example input', test)


def test():
    example = insertion_sort([])
    return example is not None and lists_equal(example, [])


expect(test_count, 'should return empty array for empty input', test)


def test():
    example = insertion_sort([10])
    return example is not None and lists_equal(example, [10])


expect(test_count, 'should sort single-element input', test)


def test():
    work = []
    for i in range(0, 1000):
        work.append(int(random.random() * 1000))
    example = insertion_sort(list(work))
    work.sort()
    return example is not None and lists_equal(example, work)


expect(test_count, 'should sort moderate-sized input', test)


print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print('Selection Sort Tests')
test_count = [0, 0]


def test():
    example = selection_sort([3, 9, 1, 4, 7])
    return example is not None and lists_equal(example, [1, 3, 4, 7, 9])


expect(test_count, 'should sort example input', test)


def test():
    example = selection_sort([])
    return example is not None and lists_equal(example, [])


expect(test_count, 'should return empty array for empty input', test)


def test():
    example = selection_sort([10])
    return example is not None and lists_equal(example, [10])


expect(test_count, 'should sort single-element input', test)


def test():
    work = []
    for i in range(0, 1000):
        work.append(int(random.random() * 1000))
    example = selection_sort(list(work))
    work.sort()
    return example is not None and lists_equal(example, work)


expect(test_count, 'should sort moderate-sized input', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Bubble Sort Tests')
test_count = [0, 0]


def test():
    example = bubble_sort([3, 9, 1, 4, 7])
    return example is not None and lists_equal(example, [1, 3, 4, 7, 9])


expect(test_count, 'should sort example input', test)


def test():
    example = bubble_sort([])
    return example is not None and lists_equal(example, [])


expect(test_count, 'should return empty array for empty input', test)


def test():
    example = bubble_sort([10])
    return example is not None and lists_equal(example, [10])


expect(test_count, 'should sort single-element input', test)


def test():
    work = []
    for i in range(0, 1000):
        work.append(int(random.random() * 1000))
    example = bubble_sort(list(work))
    work.sort()
    return example is not None and lists_equal(example, work)


expect(test_count, 'should sort moderate-sized input', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
