#
#  Homework - Binary Search Tree
#
#  Problem 1: TreeNode class
#
#  Prompt:    Create a TreeNode class
#             The TreeNode class should contain the following properties:
#
#                    value:  {Integer}
#                     left:  {TreeNode} (initially None)
#                    right:  {TreeNode} (initially None)
#
#                  Example:  sample1 = TreeNode()
#                            sample1.value   # None
#                            sample1.left    # None
#                            sample1.right   # None
#
#                  Example:  sample2 = TreeNode(1)
#                            sample2.value   # 1
#                            sample2.left    # None
#                            sample2.right   # None
#
#
#  Problem 2: BinarySearchTree class.
#
#  Prompt:    Create a BinarySearchTree class
#
#             The BinarySearchTree class should contain the following
#             properties:
#
#                    root:   {TreeNode} (initially None)
#                    size:   {Integer}
#
#             The BinarySearchTree class should also contain the following
#             methods:
#
#                  insert:   A method that takes takes an integer value, and
#                            creates a node with the given input.  The method
#                            will then find the correct place to add the new
#                            node. Values larger than the current node node go
#                            to the right, and smaller values go to the left.
#
#                            Input:     value {Integer}
#                            Output:    {None}
#
#                  search:   A method that searches if a value exists with a
#                            exists within the tree and returns true if found.
#
#                            Input:     value {Integer}
#                            Output:    {Boolean}
#


class TreeNode:
    def __init__(self, value=None):
        # YOUR WORK HERE
        pass


class BinarySearchTree:
    def __init__(self):
        # YOUR WORK HERE
        pass

    # Time Complexity:
    # Auxiliary Space Complexity:
    def insert(self, value):
        # YOUR WORK HERE
        pass

    # Time Complexity:
    # Auxiliary Space Complexity:
    def search(self, value):
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


print('TreeNode Class')
test_count = [0, 0]


def test():
    node = TreeNode()
    return isinstance(node, object)


expect(test_count, 'able to create an instance', test)


def test():
    node = TreeNode()
    return hasattr(node, 'value')


expect(test_count, 'has value property', test)


def test():
    node = TreeNode()
    return hasattr(node, 'left')


expect(test_count, 'has left property', test)


def test():
    node = TreeNode()
    return hasattr(node, 'right')


expect(test_count, 'has right property', test)


def test():
    node = TreeNode()
    return node.value is None


expect(test_count, 'has default value set to None', test)


def test():
    node = TreeNode(5)
    return node.value == 5


expect(test_count, 'able to assign a value upon instantiation', test)


def test():
    node = TreeNode()
    node.value = 5
    return node.value == 5


expect(test_count, 'able to reassign a value', test)


def test():
    node1 = TreeNode(5)
    node2 = TreeNode(10)
    node1.left = node2
    return node1.left.value == 10


expect(test_count, 'able to point to left child node', test)


def test():
    node1 = TreeNode(5)
    node2 = TreeNode(10)
    node1.right = node2
    return node1.right.value == 10


expect(test_count, 'able to point to right child node', test)
print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Binary Search Tree Class')
test_count = [0, 0]


def test():
    bst = BinarySearchTree()
    return isinstance(bst, object)


expect(test_count, 'able to create an instance', test)


def test():
    bst = BinarySearchTree()
    return hasattr(bst, 'root')


expect(test_count, 'has root property', test)


def test():
    bst = BinarySearchTree()
    return hasattr(bst, 'size')


expect(test_count, 'has size property', test)


def test():
    bst = BinarySearchTree()
    return bst.root is None


expect(test_count, 'default root set to None', test)


def test():
    bst = BinarySearchTree()
    return bst.size == 0


expect(test_count, 'default size set to 0', test)


print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('BinarySearchTree Insert Method')
test_count = [0, 0]


def test():
    bst = BinarySearchTree()
    return hasattr(bst, 'insert') and callable(getattr(bst, 'insert'))


expect(test_count, 'has insert method', test)


def test():
    bst = BinarySearchTree()
    bst.insert(5)
    return bst.size == 1 and bst.root.value == 5


expect(test_count, 'able to insert a node into empty binary search tree', test)


def test():
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    return bst.size == 2 and bst.root.value == 5 and bst.root.left.value == 3


expect(test_count, 'able to insert node to left of root node', test)


def test():
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(4)
    return bst.size == 3 and bst.root.value == 5 and bst.root.left.value == 3 \
        and bst.root.left.right.value == 4


expect(test_count, 'able to insert node to right of node left of root node',
       test)


def test():
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(8)
    return bst.size == 2 and bst.root.value == 5 and bst.root.right.value == 8


expect(test_count, 'able to insert node to right of root node', test)


def test():
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(8)
    bst.insert(7)
    return bst.size == 3 and bst.root.value == 5 and \
        bst.root.right.value == 8 and bst.root.right.left.value == 7


expect(test_count, 'able to insert node to left of node right of root node',
       test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('BinarySearchTree Search Method')
test_count = [0, 0]


def test():
    bst = BinarySearchTree()
    return hasattr(bst, 'search') and callable(getattr(bst, 'search'))


expect(test_count, 'has search method', test)


def test():
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(4)
    bst.insert(7)
    return bst.search(4) is True


expect(test_count, 'returns true when element exists in binary search tree',
       test)


def test():
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(4)
    bst.insert(7)
    return bst.search(10) is False


expect(test_count, 'returns false when element does not exist in binary ' +
       'search tree', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
