#
# Homework - Decrease and Conquer
#
# Number of Ones: Given a sorted bit array (values of either 0 or 1),
# ... determine the number of 1's in the array.

# Parameters
# Input: arr (ints)
# Output: int

# Constraints
# Time: O(logN)
# Space: O(1)

# Examples:
# [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1] --> 8
# [0, 0, 0] --> 0
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1] --> 7
# [1, 1, 1] --> 3

def number_of_ones(arr):
    # YOUR WORK HERE
    pass


# Closest value: Given a sorted array of integers, and a target value,
# ... find the number in the array that is closest to the target.

# Parameters
# Input: arr (ints)
# Input: target (int)
# Output: int

# Constraints
# If there are two numbers tied for the closest value, return the lowest value.
# Time: O(logN)
# Space: O(1)

# [1, 2, 3, 5, 5, 7, 9, 10, 11], 6 --> 5
# [1, 2, 3], 8 --> 3
# [-2, -1, 0], -5 --> -2


def closest_value(arr, target):
    # YOUR WORK HERE
    pass

# Square Root: Given an positive integer, find the square root.

# Parameters
# Input: value (int)
# Output: float

# Constraints
# Do not use a native built in method.
# Ensure the result is accurate to 6 decimal places (0.000001)
# Time: O(logN)
# Space: O(1)

# Examples:
# 4 --> 2.0
# 98 --> 9.899495
# 14856 --> 121.885192


def square_root(n):
    # YOUR WORK HERE
    pass

# Greater Values: Given an sorted array of integers,
# ... and a target value return the number of values greater the target.

# Parameters
# Input: arr (ints)
# Input: target {Integer} Output: {Integer}

# Constraints
# Time: O(logN)
# Space: O(1)

# Examples:
# [1, 2, 3, 5, 5, 7, 9, 10, 11], 5 --> 4
# [1, 2, 3], 4 --> 0
# [1, 10, 22, 59, 67, 72, 100], 13 --> 5


def greater_values(arr, target):
    # YOUR WORK HERE
    pass

# Rotated Sorted Array [Extra Credit]

# Given a array that is sorted and rotated, find out if a target value exists in the array.

# Parameters
# Input: arr (ints)
# Output: boolean

# Constraints
# Time: O(logN)
# Space: O(1)

# Examples:
# [35, 46, 79, 102, 1, 14, 29, 31], 46 --> True
# [35, 46, 79, 102, 1, 14, 29, 31], 47 --> False
# [35, 46, 79, 102, 1, 14, 29, 31], 47 --> false
# [7, 8, 9, 10, 1, 2, 3, 4, 5, 6], 9 --> true

def rotated_array_search(nums, target):
    # YOUR WORK HERE
    pass


def binary_search(nums, start, end, target):
    # YOUR WORK HERE
    pass


# Multiplication Russian Peasant [Extra Credit]

# Multiplication Given two positive integers, return its product using Russian Peasant method of multiplication

# Parameters
# Input: a (int)
# Input: b (int)
# Output: int

# Constraints
# Assume a <= b, and the value of a is N.
# Time: O(logN)
# Space: O(1)

# 487, 734--> 357458
# 846, 908--> 768168

def multiplication_russian_peasant(a, b):
    # double the first number and half the second number
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


print('\nNumber of Ones')
test_count = [0, 0]


def test():
    example = number_of_ones([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])
    return example is not None and example == 8

expect(test_count, "should return correct number of ones for array with zeroes and ones", test)

def test():
    example = number_of_ones([0, 0, 0])
    return example is not None and example == 0

expect(test_count, "should return correct number of ones for array with all zeroes", test)


def test():
    example = number_of_ones([1, 1, 1])
    return example is not None and example == 3

expect(test_count, "should return correct number of ones for array with all ones", test)


print('\nClosest Value')
test_count = [0, 0]

def test():
    example = closest_value([1, 2, 3, 5, 5, 7, 9, 10, 11], 6)
    return example is not None and example == 5

expect(test_count, "should return correct closest value for number in the middle range", test)


def test():
    example = closest_value([1, 2, 3], 8)
    return example is not None and example == 3

expect(test_count, "should return closest value for highest number", test)


def test():
    example = closest_value([-2, -1, 0], -5)
    return example is not None and example == -2

expect(test_count, "should return closest value for lowest number", test)


print('\nSquare Root')
test_count = [0, 0]

def test():
    example = square_root(4)
    return example is not None and example == 2.0

expect(test_count, "should return correct square root for number < 10", test)


def test():
    example = square_root(98)
    return example is not None and example == 9.899495

expect(test_count, "should return correct square root for number between 10 and 100", test)

def test():
    example = square_root(14856)
    return example is not None and example == 121.885192

expect(test_count, "should return correct square root for number over 10,000", test)

print('\nGreater Values')
test_count = [0, 0]


def test():
    example = greater_values([1, 2, 3, 5, 5, 7, 9, 10, 11], 5)
    return example is not None and example == 4

expect(test_count, "should return greater values for number in the middle of the array", test)


def test():
    example = greater_values([1, 2, 3], 4)
    return example is not None and example == 0

expect(test_count, "should return 0 for number greater than largest in the array", test)


def test():
    example = greater_values([1, 10, 22, 59, 67, 72, 100], -2)
    return example is not None and example == 7

expect(test_count, "should return greater values for number less than least in the array", test)

print('\nRotated Sorted Array')
test_count = [0, 0]

def test():
    example = rotated_array_search([35, 46, 79, 102, 1, 14, 29, 31], 46)
    return example is not None and example is True

expect(test_count, "returns True when target is in the array", test)


def test():
    example = rotated_array_search([35, 46, 79, 102, 1, 14, 29, 31], 47)
    return example is not None and example is False

expect(test_count, "returns False when target is not in the array", test)


def test():
    example = rotated_array_search([7, 8, 9, 10, 1, 2, 3, 4, 5, 6], 7)
    return example is not None and example is True

expect(test_count, "returns True when target is the first number in the array", test)

def test():
    example = rotated_array_search([7, 8, 9, 10, 1, 2, 3, 4, 5, 6], 6)
    return example is not None and example is True

expect(test_count, "returns True when target is the last number in the array", test)


print('\nMultiplication Russian Peasant')
test_count = [0, 0]

def test():
    example = multiplication_russian_peasant(487,734)
    return example is not None and example == 357458

expect(test_count, "returns correct value for two integers", test)
