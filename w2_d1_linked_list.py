#
#  Homework - Linked List
#
#  Problem 1: ListNode class
#
#  Prompt:    Create a ListNode class
#             The ListNode class should contain the following properties:
#
#                 value:   {Integer} (default None)
#                  next:   {ListNode} (default None)
#
#               Example:   input: sample1 = new ListNode(1)
#                          sample1.value     # 1
#                          sample1.next      # None
#
#               Example:   input: sample2 = new ListNode()
#                          sample2.value     # None
#                          sample2.next      # None
#
#
#  Problem 2:  LinkedList class
#
#  Prompt:     Create a LinkedList class
#              The LinkedList class should contain the following properties:
#
#                length:   {Integer}
#                  head:   {ListNode}
#                  tail:   {ListNode}
#
#              The LinkedList class should also contain the following methods:
#
#                append:   A method that appends a value to the end of the
#                          LinkedList.
#
#                          Input:     value {Integer}
#                          Output:    {None}
#
#                insert:   A method that inserts an integer value at a set
#                          index in the LinkedList (assume head index is 0).
#
#                          Input:     value {Integer}
#                          Input:     index {Integer}
#                          Output:    {None}
#
#                remove:   A method that removes a node at a specified index.
#
#                          Input:     index {Integer}
#                          Output:    {None}
#
#              contains:   A method that checks to see if a value is contained
#                          in the list.
#
#                          Input:     value {Integer}
#                          Output:    {Boolean}
#


class ListNode:
    def __init__(self, value=None):
        # YOUR WORK HERE
        pass


class LinkedList:
    def __init__(self):
        # YOUR WORK HERE
        pass

    # Time Complexity:
    # Auxiliary Space Complexity:
    def append(self, value):
        # YOUR WORK HERE
        pass

    # Time Complexity:
    # Auxiliary Space Complexity:
    def insert(self, value, index):
        # YOUR WORK HERE
        pass

    # Time Complexity:
    # Auxiliary Space Complexity:
    def remove(self, index):
        # YOUR WORK HERE
        pass

    # Time Complexity:
    # Auxiliary Space Complexity:
    def contains(self, value):
        # YOUR WORK HERE
        pass


# ###########################################################
# ##############  DO NOT TOUCH TEST BELOW!!!  ###############
# ###########################################################


from io import StringIO
import sys


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


print('ListNode Class')
test_count = [0, 0]


def test():
    node = ListNode()
    return isinstance(node, object)


expect(test_count, 'able to create an instance', test)


def test():
    node = ListNode()
    return hasattr(node, 'value')


expect(test_count, 'has value property', test)


def test():
    node = ListNode()
    return hasattr(node, 'next')


expect(test_count, 'has next property', test)


def test():
    node = ListNode()
    return node is not None and node.value is None


expect(test_count, 'has default value set to None', test)


def test():
    node = ListNode(5)
    return node is not None and node.value == 5


expect(test_count, 'able to assign a value upon instantiation', test)


def test():
    node = ListNode()
    node.value = 5
    return node is not None and node.value == 5


expect(test_count, 'able to reassign a value', test)


def test():
    node1 = ListNode(5)
    node2 = ListNode(10)
    node1.next = node2
    return (node1 is not None and node1.next is not None and
            node1.next.value == 10)


expect(test_count, 'able to point to another node', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('LinkedList Class')
test_count = [0, 0]


def test():
    linked_list = LinkedList()
    return isinstance(linked_list, object)


expect(test_count, 'able to create an instance', test)


def test():
    linked_list = LinkedList()
    return hasattr(linked_list, 'head')


expect(test_count, 'has head property', test)


def test():
    linked_list = LinkedList()
    return hasattr(linked_list, 'tail')


expect(test_count, 'has tail property', test)


def test():
    linked_list = LinkedList()
    return hasattr(linked_list, 'length')


expect(test_count, 'has length property', test)


def test():
    linked_list = LinkedList()
    return linked_list is not None and linked_list.head is None


expect(test_count, 'default head set to None', test)


def test():
    linked_list = LinkedList()
    return linked_list is not None and linked_list.tail is None


expect(test_count, 'default tail set to None', test)


def test():
    linked_list = LinkedList()
    return linked_list is not None and linked_list.length == 0


expect(test_count, 'default length set to 0', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('LinkedList Insert Method')
test_count = [0, 0]


def test():
    linked_list = LinkedList()
    return (hasattr(linked_list, 'insert') and
            callable(getattr(linked_list, 'insert')))


expect(test_count, 'has insert method', test)


def test():
    linked_list = LinkedList()
    linked_list.insert(5, 0)
    return (linked_list is not None and linked_list.length == 1 and
            linked_list.head.value == 5 and linked_list.tail.value == 5)


expect(test_count, 'able to insert a node into empty linked list', test)


def test():
    linked_list = LinkedList()
    linked_list.insert(5, 0)
    linked_list.insert(10, 1)
    return (linked_list is not None and linked_list.length == 2 and
            linked_list.head.value == 5 and linked_list.tail.value == 10)


expect(test_count, 'able to insert a node after another node', test)


def test():
    linked_list = LinkedList()
    linked_list.insert(5, 0)
    linked_list.insert(10, 0)
    return (linked_list is not None and linked_list.length == 2 and
            linked_list.head.value == 10 and linked_list.tail.value == 5)


expect(test_count, 'able to insert a node before another node', test)


def test():
    linked_list = LinkedList()
    linked_list.insert(5, 0)
    linked_list.insert(10, 1)
    linked_list.insert(7, 1)
    return (linked_list is not None and linked_list.length == 3 and
            linked_list.head.value == 5 and linked_list.tail.value == 10 and
            linked_list.head.next.value == 7)


expect(test_count, 'able to insert a node in between two nodes', test)


def test():
    linked_list = LinkedList()
    linked_list.insert(5, -1)
    linked_list.insert(10, 3)
    return (linked_list is not None and linked_list.length == 0 and
            linked_list.head is None and linked_list.tail is None)


expect(test_count, 'does not insert a node if index is out of bounds', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('LinkedList Append Method')
test_count = [0, 0]


def test():
    linked_list = LinkedList()
    return (hasattr(linked_list, 'append') and
            callable(getattr(linked_list, 'append')))


expect(test_count, 'has append method', test)


def test():
    linked_list = LinkedList()
    linked_list.append(5)
    return (linked_list is not None and linked_list.length == 1 and
            linked_list.head.value == 5 and linked_list.tail.value == 5)


expect(test_count, 'able to append a node into empty linked list', test)


def test():
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(10)
    return (linked_list is not None and linked_list.length == 2 and
            linked_list.head.value == 5 and linked_list.tail.value == 10)


expect(test_count, 'able to append a second node into linked list', test)


def test():
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    return (linked_list is not None and linked_list.length == 3 and
            linked_list.head.value == 5 and linked_list.tail.value == 15)


expect(test_count, 'able to append a third node into linked list', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print('LinkedList Remove Method')
test_count = [0, 0]


def test():
    linked_list = LinkedList()
    return (hasattr(linked_list, 'remove') and
            callable(getattr(linked_list, 'remove')))


expect(test_count, 'has remove method', test)


def test():
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.remove(0)
    return (linked_list is not None and linked_list.length == 1 and
            linked_list.head.value == 10 and linked_list.tail.value == 10)


expect(test_count, 'able to remove a node from the head', test)


def test():
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.remove(1)
    return (linked_list is not None and linked_list.length == 1 and
            linked_list.head.value == 5 and linked_list.tail.value == 5)


expect(test_count, 'able to remove a node from the tail', test)


def test():
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    linked_list.remove(1)
    return (linked_list is not None and linked_list.length == 2 and
            linked_list.head.value == 5 and linked_list.tail.value == 15)


expect(test_count, 'able to remove a node in between two nodes', test)


def test():
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.remove(0)
    return (linked_list is not None and linked_list.length == 0 and
            linked_list.head is None and linked_list.tail is None)


expect(test_count, 'able to remove the only node in a linked list', test)


def test():
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.remove(-1)
    linked_list.remove(2)
    return (linked_list is not None and linked_list.length == 1 and
            linked_list.head.value == 5 and linked_list.tail.value == 5)


expect(test_count, 'does not remove a node when the index is out of bounds',
       test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print('LinkedList Contains Method')
test_count = [0, 0]


def test():
    linked_list = LinkedList()
    return (hasattr(linked_list, 'contains') and
            callable(getattr(linked_list, 'contains')))


expect(test_count, 'has contains method', test)


def test():
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    return linked_list.contains(15) is True


expect(test_count, 'returns True if linked list contains value', test)


def test():
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(10)
    linked_list.append(15)
    return linked_list.contains(8) is False


expect(test_count, 'returns False if linked list contains value', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
