# Homework - Matrices
#
# Prompt: Create a Matrix class
#
# The Matrix will take in the following input:
#
#              m:    {Integer} - represents the number of ROWS
#              n:    {Integer} - represent the number of COLUMNS
#
# The Matrix will have the following properties:
#
#        storage:    {Array of Arrays of Integers} - stores of numbers within matrix
#              m:    {Integer} - represents the number of ROWS
#              n:    {Integer} - represent the number of COLUMNS
#
# The Matrix will have the following methods:
#
#         isValid:   checks whether given coordinates are within the matrix
#
#                  Input:      i {Integer} - row index
#                  Input:      j {Integer} - column index
#                 Output:        {Boolean}
#
#                Example:
#
#                matrix.storage == [[0, 1, 2],
#                                   [3, 4, 5],
#                                   [6, 7, 8]]
#
#                matrix.isValid(1, 1)
#
#                result == true
#
#                matrix.isValid(100, 1)
#
#                result == false
#
#
#      initialize:   takes in a valid array of arrayOfArrays, and
#
#                  Input: arrayOfArrays {Array of Arrays of Integers}
#
#                 Output:        {undefined / void}
#
#                Example:
#
#                matrix.intitialize([[0, 1, 2],
#                                    [3, 4, 5],
#                                    [6, 7, 8]])
#
#
#                result:
#
#                matrix.storage == [[0, 1, 2],
#                                   [3, 4, 5],
#                                   [6, 7, 8]]
#
#                matrix.m == 3
#
#                matrix.n == 3
#
#
#           print:   optional method to print the contents of a matrix's storage
#                    prints each row of the matrix on a new line.
#
#                  Input: N/A {undefined / void}
#
#                 Output:        {undefined / void}
#
#                Example:
#
#                matrix.storage == [[0, 1, 2],
#                                   [3, 4, 5],
#                                   [6, 7, 8]]
#
#
#                console:
#
#                [0, 1, 2]
#                [3, 4, 5]
#                [6, 7, 8]
#
#
#          insert:   inserts an integer into the given coordinates
#                   returns true if insertion was successful
#                   returns false otherwise
#
#                  Input:      i {Integer}
#                  Input:      j {Integer}
#                  Input:    val {Integer}
#                 Output:        {Boolean}
#
#                Example:
#
#                matrix.storage == [[0, 1, 2],
#                                   [3, 4, 5],
#                                   [6, 7, 8]]
#
#                matrix.insert(1, 1, 400)
#
#                matrix.storage == [[0, 1, 2],
#                                   [3, 400, 5],
#                                   [6, 7, 8]]
#
#                result == true
#
#
#                matrix.insert(100, 1, 400)
#
#                matrix.storage = [[0, 1, 2],
#                                  [3, 4, 5],
#                                  [6, 7, 8]]
#
#                result == false
#
#
#        retrieve:   returns value stored at given coordinates
#                    returns -Infinity / Integer.MIN_VALUE if coordinates are invalid
#
#                  Input:      i {Integer} - row index
#                  Input:      j {Integer} - column index
#                 Output:        {Integer}
#
#                 Example:
#
#                 matrix.storage == [[0, 1, 2],
#                                    [3, 4, 5],
#                                    [6, 7, 8]]
#
#                 matrix.retrieve(1, 1)
#
#                 result == 4
#
#
#           scale:   multiplies every value in the matrix by some constant factor
#                    returns undefined / void
#
#                   Input:  factor {Integer} - amount each entry will be multiplied by
#                   Output:         {undefined}
#
#                  Example:
#
#                  matrix.storage == [[1, 1, 1],
#                                     [1, 1, 1],
#                                     [1, 1, 1]]
#
#                  matrix.scale(5)
#
#                  matrix.storage == [[5, 5, 5],
#                                     [5, 5, 5],
#                                     [5, 5, 5]]
#
#
#            fill:   sets every entry in the matrix equal to input value
#                    returns undefined / void
#
#                  Input:     val {Integer} - value to be inserted throughout matrix
#                 Output:         {undefined}
#
#                Example:
#
#                matrix.storage == [[0, 1, 2],
#                                   [3, 4, 5],
#                                   [6, 7, 8]]
#
#                matrix.fill(1)
#
#                matrix.storage == [[1, 1, 1],
#                                   [1, 1, 1],
#                                   [1, 1, 1]]
#
#
#         flatten:   returns an array containing all the elements in the matrix if traversed row by row
#
#                  Input:      N/A
#                 Output:     {Array of Integers}
#
#                Example:
#
#                matrix.storage == [[0, 1, 2],
#                                   [3, 4, 5],
#                                   [6, 7, 8]]
#
#                matrix.flatten()
#
#                result == [0, 1, 2, 3, 4, 5, 6, 7, 8]
#
#
#           slice:   returns a new Matrix representing a subset of the original matrix
#                    it's rows are bounded by the first two-element array input
#                    it's columns are bounded by the second two-element array input
#
#                    NOTE: If the rowRange or colRange is larger than the original matrix
#                          just return the bounds of the original matrix
#
#                    NOTE: Think about how much you'll have to offset insertions into the new matrix
#
#                   Input:      rowRange {Array of Two Integers}
#                   Input:      colRange {Array of Two Integers}
#                  Output:     {Matrix}
#
#                Example:
#
#                matrix.storage == [[0, 1, 2],
#                                   [3, 4, 5],
#                                   [6, 7, 8]]
#
#                matrix.slice([0, 2], [0, 2])
#
#                result == [[0, 1],
#                           [3, 4]]
#
#
#       transpose:   returns a new Matrix representing the transpose of the original matrix
#                    The transpose of a matrix is like flipping a matrix along its diagonal axis
#
#                    Link to Wikipedia:
#                    NOTE: if the original matrix was M x N, the new one will be N x M
#
#                   Input:      N/A
#                  Output:     {Matrix}
#
#                matrix.storage == [[0, 1, 2],
#                                   [3, 4, 5]]
#
#                matrix.transpose()
#
#                result == [[0, 3],
#                           [1, 4],
#                           [2, 5]]
#
#
#
#        mulitply:   returns a new Matrix representing the matrix multiplication of original matrix
#                    by the input matrix.
#
#                    Link to Wikipedia:
#                    NOTE: if the original matrix was M x N, the input one MUST be N x K
#                          the result matrix will then be M x K dimensions
#
#                   Input:      matrix {Matrix}
#                  Output:     {Matrix}
#
#                matrix.storage == [[4, 1, 3],
#                                   [3, 2, 5]]
#
#                matrix.multiply([[8, 9],
#                                 [7, 10],
#                                 [0, 6]])
#
#                result == [[39, 64],
#                           [38, 77]]
#
#                Reasoning:
#                         [[(4 * 8) + (1 * 7) + (3 * 0),    (4 * 9) + (1 * 10) + (3 * 6)],
#
#                          [(3 * 8) + (2 * 7) + (5 * 0),    (3 * 9) + (2 * 10) + (5 * 6)]]
#
#
#                     =>  [[32 + 7 + 0,   36 + 10 + 18],
#
#                          [24 + 14 + 0,  27 + 20 + 30]]
#
#
#                     =>  [[39, 64],
#                          [38, 77]]


# NOTE: Please attempt to complete this hw without using additional modules such as numpy
class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.storage = [[0 for col in range(n)] for row in range(m)]

    def printer(self):
        # YOUR WORK HERE
        pass

    def isValid(self, i, j):
        # YOUR WORK HERE
        pass

    def initialize(self, arrayOfArrays):
        # YOUR WORK HERE
        pass

    def insert(self, i, j, val):
        # YOUR WORK HERE
        pass

    def retrieve(self, i, j):
        # YOUR WORK HERE
        pass

    def scale(self, factor):
        # YOUR WORK HERE
        pass

    def fill(self, val):
        # YOUR WORK HERE
        pass

    def flatten(self):
        # YOUR WORK HERE
        pass

    def slice(self, rowRange, colRange):
        # YOUR WORK HERE
        pass

    def transpose(self):
        # YOUR WORK HERE
        pass

    def multiply(self, matrix):
        # YOUR WORK HERE
        pass


#############################################################
################  DO NOT TOUCH TEST BELOW!!!  ###############
#############################################################

# custom expect function to handle tests
# List count : keeps track out how many tests pass and how many total
#   in the form of a two item array i.e., [0, 0]
# String name : describes the test
# Function test : performs a set of operations and returns a boolean
#   indicating if test passed
def expect(count, name, test):
  if(count == None or not isinstance(count, list) or len(count) != 2):
    count = [0, 0]
  else:
    count[1] += 1


  result = 'false'
  errMsg = None
  try:
    if test():
      result = ' true'
      count[0] += 1
  except Exception as err:
    errMsg = str(err)

  print('  ' + (str(count[1]) + ')   ') + result + ' : ' + name)
  if errMsg != None:
    print('       ' + errMsg + '\n')

# code for capturing print output
#
# directions: capture_print function returns a list of all elements that were
#             printed using print with the function that it is given. Note that
#             the function given to capture_print must be fed using lambda.
#             Example cis provided below

print('Matrix Tests')

test_count = [0, 0]
print('IsValid Tests')
def test():
    matrix = Matrix(3, 4)
    return matrix.isValid(1, 1) == True
expect(test_count, 'should return true for a valid set of coordinates', test)

def test():
    matrix = Matrix(3, 4)
    return matrix.isValid(5, 1) == False
expect(test_count, 'should return false for a set of coordinates off the matrix', test)

def test():
    matrix = Matrix(3, 4)
    return matrix.isValid(-4, 1) == False
expect(test_count, 'should return false for a negative set of coordinates', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


test_count = [0, 0]
print('Initialize Tests')
def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[1, 2, 3], [4, 5, 6]])
    return matrix.m == 2 and matrix.n == 3
expect(test_count, 'should override m and n values in old matrix', test)

def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[1, 2], [3, 4]])
    return matrix.storage != None and matrix.storage[0] != None and \
        matrix.storage[1] != None and matrix.storage[0][0] == 1 and \
        matrix.storage[0][1] == 2 and matrix.storage[1][0] == 3 and \
        matrix.storage[1][1] == 4
expect(test_count, 'should override contents of old matrix', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')



test_count = [0, 0]
print('Insert Tests')
def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[1, 2, 3], [4, 5, 6]])
    return matrix.insert(1, 1, 50) == True
expect(test_count, 'should return true if given valid coordinates', test)

def test():
    matrix =  Matrix(1, 1)
    matrix.initialize([[1, 2, 3], [4, 5, 6]])
    return matrix.insert(1, 1, 50) == True and matrix.storage[1][1] == 50
expect(test_count, 'should override old value in matrix given valid coordinates', test)

def test():
    matrix =  Matrix(1, 1)
    matrix.initialize([[1, 2, 3], [4, 5, 6]])
    return matrix.insert(5, 5, 10) == False
expect(test_count, 'should return false if given invalid coordinates', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')



test_count = [0, 0]
print('Retrieve Tests')
def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[0, 1, 2],[3, 4, 5],[6, 7, 8]])
    return matrix.retrieve(1, 1) == 4
expect(test_count, 'should return correct value if given valid coordinates', test)

def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[0, 1, 2],[3, 4, 5],[6, 7, 8]])
    return matrix.retrieve(10, 10) == float('-inf')
expect(test_count, 'should return -Infinity if given invalid coordinates', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')



test_count = [0, 0]
print('Scale Tests')
def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[0, 1],[3, 4]])
    matrix.scale(2)
    return matrix.storage[0][0] == 0 and  matrix.storage[0][1] == 2 and \
         matrix.storage[1][0] == 6 and  matrix.storage[1][1] == 8
expect(test_count, 'should scale values in matrix by amount given', test)

def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[0, 1],[3, 4]])
    matrix.scale(-3)
    return matrix.storage[0][0] == 0 and matrix.storage[0][1] == -3 and \
        matrix.storage[1][0] == -9 and matrix.storage[1][1] == -12
expect(test_count, 'should scale values in matrix by amount given', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')



test_count = [0, 0]
print('Fill Tests')
def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[0, 1],[3, 4]])
    matrix.fill(2)
    return matrix.storage[0][0] == 2 and  matrix.storage[0][1] == 2 and \
         matrix.storage[1][0] == 2 and  matrix.storage[1][1] == 2
expect(test_count, 'should scale values in matrix by amount given', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')



test_count = [0, 0]
print('Flatten Tests')
def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[0], [1], [3], [4]])
    return matrix.flatten() == [0, 1, 3, 4]
expect(test_count, 'should work for a single column matrix', test)

def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[0, 1, 3, 4]])
    return matrix.flatten() == [0, 1, 3, 4]
expect(test_count, 'should work for a single row matrix', test)

def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    return matrix.flatten() == [0, 1, 2, 3, 4, 5, 6, 7, 8]
expect(test_count, 'should work for example matrix', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')




test_count = [0, 0]
print('Slice Tests')
def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    newMatrix = matrix.slice([0,2], [0,2])

    return newMatrix != None and newMatrix.m == 2 and newMatrix.n == 2 and \
         newMatrix.storage[0][0] == 0 and newMatrix.storage[0][1] == 1 and \
         newMatrix.storage[1][0] == 3 and newMatrix.storage[1][1] == 4
expect(test_count, 'should return 2x2 matrix slice from a 3x3 matrix when rowRange is [0,2] and colRange is [0,2]', test)

def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    newMatrix = matrix.slice([1,3], [1,3])

    return newMatrix != None and newMatrix.m == 2 and newMatrix.n == 2 and \
         newMatrix.storage[0][0] == 4 and newMatrix.storage[0][1] == 5 and \
         newMatrix.storage[1][0] == 7 and newMatrix.storage[1][1] == 8
expect(test_count, 'should return 2x2 matrix slice from a 3x3 matrix when rowRange is [1,3] and colRange is [1,3]', test)

def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    newMatrix = matrix.slice([-5,20], [-2,6])

    return newMatrix != None and newMatrix.m == 3 and newMatrix.n == 3 and \
         newMatrix.storage[0][0] == 0 and newMatrix.storage[0][1] == 1 and \
         newMatrix.storage[0][2] == 2 and newMatrix.storage[1][0] == 3 and \
         newMatrix.storage[1][1] == 4 and newMatrix.storage[1][2] == 5 and \
         newMatrix.storage[2][0] == 6 and newMatrix.storage[2][1] == 7 and \
         newMatrix.storage[2][2] == 8
expect(test_count, 'should return copy of original matrix if rowRange and colRange are larger than original', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')



test_count = [0, 0]
print('Transpose Tests')
def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[1]])
    newMatrix = matrix.transpose()
    return newMatrix != None and newMatrix.m == 1 and newMatrix.n == 1 and \
         newMatrix.storage[0][0] == 1
expect(test_count, 'should work correctly on a 1x1 matrix', test)

def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[0, 1], [2, 3]])
    newMatrix = matrix.transpose()

    return newMatrix != None and newMatrix.m == 2 and newMatrix.n == 2 and \
         newMatrix.storage[0][0] == 0 and newMatrix.storage[0][1] == 2 and \
         newMatrix.storage[1][0] == 1 and newMatrix.storage[1][1] == 3
expect(test_count, 'should work correctly on a 2x2 matrix', test)

def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[0, 1], [3, 4], [6, 7]])
    newMatrix = matrix.transpose()

    return newMatrix != None and newMatrix.m == 2 and newMatrix.n == 3 and \
         newMatrix.storage[0][0] == 0 and newMatrix.storage[0][1] == 3 and \
         newMatrix.storage[0][2] == 6 and newMatrix.storage[1][0] == 1 and \
         newMatrix.storage[1][1] == 4 and newMatrix.storage[1][2] == 7
expect(test_count, 'should work correctly on a 3x2 matrix', test)

def test():
    matrix = Matrix(1, 1)
    matrix.initialize([[0, 1, 3], [4, 6, 7]])
    newMatrix = matrix.transpose()

    return newMatrix != None and newMatrix.m == 3 and newMatrix.n == 2 and \
         newMatrix.storage[0][0] == 0 and newMatrix.storage[0][1] == 4 and \
         newMatrix.storage[1][0] == 1 and newMatrix.storage[1][1] == 6 and \
         newMatrix.storage[2][0] == 3 and newMatrix.storage[2][1] == 7
expect(test_count, 'should work correctly on a 2x3 matrix', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')




test_count = [0, 0]
print('Multiply Tests')
def test():
    matrix1 = Matrix(1, 1)
    matrix2 = Matrix(1, 1)

    matrix1.initialize([[4, 1, 3],
                      [3, 2, 5]])

    matrix2.initialize([[8, 9],
                      [7, 10],
                      [0, 6]])

    newMatrix = matrix1.multiply(matrix2)

    return newMatrix != None and newMatrix.m == 2 and newMatrix.n == 2 and \
         newMatrix.storage[0][0] == 39 and newMatrix.storage[0][1] == 64 and \
         newMatrix.storage[1][0] == 38 and newMatrix.storage[1][1] == 77
expect(test_count, 'should work correctly on example matrix with valid input', test)

def test():
    matrix1 = Matrix(1, 1)
    matrix2 = Matrix(1, 1)

    matrix1.initialize([[4, 1, 3],
                      [3, 2, 5]])

    matrix2.initialize([[8]])

    newMatrix = matrix1.multiply(matrix2)

    return newMatrix == None
expect(test_count, 'should work correctly on example matrix with invalid input of wrong dimensions', test)

def test():
    matrix1 = Matrix(1, 1)
    matrix2 = Matrix(1, 1)

    matrix1.initialize([[4, 1, 3],
                      [3, 2, 5]])

    matrix2.initialize([[8], [1], [2]])

    newMatrix = matrix1.multiply(matrix2)

    return newMatrix != None and newMatrix.m == 2 and newMatrix.n == 1 and \
         newMatrix.storage[0][0] == 39 and newMatrix.storage[1][0] == 36
expect(test_count, 'should work correctly on example matrix when multiplied by 3x1 matrix', test)

def test():
    matrix1 = Matrix(1, 1)
    matrix2 = Matrix(1, 1)

    matrix1.initialize([[4, 1, 3],
                      [3, 2, 5]])

    matrix2.initialize([[3, 5]])

    newMatrix = matrix2.multiply(matrix1)

    return newMatrix != None and newMatrix.m == 1 and newMatrix.n == 3 and \
         newMatrix.storage[0][0] == 27 and newMatrix.storage[0][1] == 13 and \
         newMatrix.storage[0][2] == 34
expect(test_count, 'should work correctly when 1x2 matrix is multiplied by example matrix', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
