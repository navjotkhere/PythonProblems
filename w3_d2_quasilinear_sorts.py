#
#  Homework - Quasilinear Sorts
#
#  Problem 1: Mergesort
#
#  Prompt:    Given an unsorted list of integers, return the list
#             sorted using mergesort.
#
#             What are the time and auxilliary space complexity?
#
#  Input:     input {List}
#  Output:    {List}
#
#  Example:   [3,9,1,4,7] --> [1,3,4,7,9]
#


import math

# Worse Time Complexity:
# Worse Auxiliary Space Complexity:
# Average Time Complexity:
# Average Auxiliary Space Complexity:
def mergesort(input):
    # YOUR WORK HERE
    pass


# ###########################################################
# ##############  DO NOT TOUCH TEST BELOW!!!  ###############
# ###########################################################


from io import StringIO
import sys
import random


# code for capturing print output
#
# directions: capture_print function returns a list of all elements that were
#             printed using print with the function that it is given. Note that
#             the function given to capture_print must be fed using lambda.
#             Example cis provided below
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


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


# compare if two flat lists are equal
def lists_equal(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(0, len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True


# check if a list is sorted in linear time
def is_sorted(input):
    if (len(input) < 2):
        return True
    for i in range(1, len(input)):
        if (input[i-1] > input[i]):
            return False
    return True


print('Mergesort Tests')
test_count = [0, 0]


def test():
    example = mergesort([3, 9, 1, 4, 7])
    return lists_equal(example, [1, 3, 4, 7, 9])


expect(test_count, 'should sort example input', test)


def test():
    example = mergesort([])
    return lists_equal(example, [])


expect(test_count, 'should return empty array for empty input', test)


def test():
    example = mergesort([10])
    return lists_equal(example, [10])


expect(test_count, 'should sort single-element input', test)


def test():
    work = []
    for i in range(0, 1000):
        work.append(int(random.random() * 1000))
    example = mergesort(list(work))
    return len(example) == 1000 and is_sorted(example)


expect(test_count, 'should sort moderate-sized input', test)


def test():
    work = []
    for i in range(0, 1000000):
        work.append(int(random.random() * 1000000))
    example = mergesort(list(work))
    return len(example) == 1000000 and is_sorted(example)


expect(test_count, 'should sort large input', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
