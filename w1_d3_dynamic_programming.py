#
#  Homework - Dynamic Programming
#
#  Problem:   Lattice Paths (Dynamic Programming Approach)
#
#  Prompt:    Count the number of unique paths to travel from the top left
#             to the bottom right of a lattice of squares.
#
#  Input:     An interger N (which is the size of the lattice)
#  Output:    An interger (which represents the number of unique paths)
#
#  Example:   input: 2
#
#             (2 x 2 lattice of squares)
#              __ __
#             |__|__|
#             |__|__|
#
#             output: 6 (number of unique paths from top left corner to bottom
#                     right)
#
#  Notes:     What is the time and auxilliary space complexity of your solution?
#
#             When moving through the lattice, you can only move either down or
#             to the right.
#
#             You did this problem before with recursion. Try implementing it
#             now with dynamic programming!
#
#  Resources:
#    1: https://projecteuler.net/problem=15
#    2: https://en.wikipedia.org/wiki/Lattice_path


# Time Complexity:
# Auxiliary Space Complexity:
def lattice_paths(m, n):
    # YOUR WORK HERE
    pass

############################################################
###############  DO NOT TOUCH TEST BELOW!!!  ###############
############################################################

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

print('Lattice Paths Tests')
test_count = [0, 0]


def test():
    example = lattice_paths(2, 3)
    return example == 10


expect(test_count, 'should work for a 2 x 3 lattice', test)


def test():
    example = lattice_paths(3, 2)
    return example == 10


expect(test_count, 'should work for a 3 x 2 lattice', test)


def test():
    example = lattice_paths(0, 0)
    return example == 1


expect(test_count, 'should work for a 0 x 0 lattice', test)


def test():
    example = lattice_paths(10, 10)
    return example == 184756


expect(test_count, 'should work for a 10 x 10 lattice (square input)', test)

def test():
    example = lattice_paths(20, 15)
    return example == 3247943160


expect(test_count, 'work for a 20 x 15 lattice (large input)', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
