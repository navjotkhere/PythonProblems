#
#  Homework - Hash Table
#
#  Problem: Hash Table
#
#  Prompt: Create a hash table class using separate chaining.
#
#  The HashTable will have the following properties:
#
#         storage:  {List} - an list of lists.
#         buckets:  {Integer} - the maximum number of buckets that your
#                   storage can contain. Initially set to 8.
#           size:   {Integer} count of key-value pairs in the storage
#
#  The HashTable will also have the following methods:
#
#           hash:   Method that takes a key and bucket number and provides a
#                   hashed value. The dbjb2 hashing function has been
#                   provided.
#
#                   Input:      key {String}
#                   Input:      buckets {Integer}
#                   Output:     index {Integer}
#
#            put:   Method that adds a key-value pair into the storage. If the
#                   key already exists, the value should be updated. Use
#                   separate chaining to handle collisions.
#
#                   Input:      key {String}
#                   Input:      value {String}
#                   Output:     {None}
#
#            get:   Method that given a key, return its corresponding value.
#                   If the key does not exist, return null.
#
#                   Input:      key {String}
#                   Output:     value {String}
#
#         remove:   Method that takes a key as its input, and looks for the
#                   and removes the key-value pair from the bucket.
#
#                   Input:      key {String}
#                   Output:     {None}
#
#         resize:   If the load factor reaches a critical 0.75 or higher,
#                   double the number of buckets. If the load factor is 0.25
#                   or less, half the number of buckets. Make sure the number
#                   of buckets do not fall below 8 and re-index all key-value
#                   pairs if bucket size is changed.
#
#                   Input:      key {String}
#                   Output:     {None}
#
#  Input: N/A
#  Output: A HashTable instance
#


class HashTable:

    def __init__(self):
        # YOUR WORK HERE
        pass

    # Time Complexity:
    # Auxiliary Space Complexity:
    def hash(self, key, buckets):
        hash = 5381
        for char in key:
            hash = ((hash << 5) + hash) + ord(char)
        return hash % buckets

    # Amortized Time Complexity (amortized):
    # Auxiliary Space Complexity (amortized):
    def insert(self, key, value):
        # YOUR WORK HERE
        pass

    # Time Complexity:
    # Auxiliary Space Complexity:
    def get(self, key):
        # YOUR WORK HERE
        pass

    # Amortized Time Complexity (amortized):
    # Auxiliary Space Complexity (amortized):
    def remove(self, key):
        # YOUR WORK HERE
        pass

    # Time Complexity:
    # Auxiliary Space Complexity:
    def resize(self):
        # YOUR WORK HERE
        pass

# ###########################################################
# ##############  DO NOT TOUCH TEST BELOW!!!  ###############
# ###########################################################

import inspect


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

    result = 'False'
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


print('HashTable Tests')
test_count = [0, 0]


def test():
    hash_table = HashTable()
    return isinstance(hash_table, object)


expect(test_count, 'able to create an instance', test)


def test():
    hash_table = HashTable()
    return hasattr(hash_table, 'storage')


expect(test_count, 'has storage property', test)


def test():
    hash_table = HashTable()
    return hasattr(hash_table, 'buckets')


expect(test_count, 'has buckets property', test)


def test():
    hash_table = HashTable()
    return hasattr(hash_table, 'size')


expect(test_count, 'has size property', test)


def test():
    hash_table = HashTable()
    return hasattr(hash_table, 'storage') and type(hash_table.storage) is list


expect(test_count, 'default storage set to a list', test)


def test():
    hash_table = HashTable()
    return hasattr(hash_table, 'buckets') and hash_table.buckets == 8


expect(test_count, 'default buckets set to 8', test)


def test():
    hash_table = HashTable()
    return hasattr(hash_table, 'size') and hash_table.size == 0


expect(test_count, 'default size set to 0', test)


print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('HashTable Hash method')
test_count = [0, 0]


def test():
    hash_table = HashTable()
    return (hasattr(hash_table, 'hash') and
            callable(getattr(hash_table, 'hash')))


expect(test_count, 'has hash method', test)


def test():
    hash_table = HashTable()
    for i in range(1, 100):
        index = hash_table.hash('hello', i)
        if not isinstance(index, int) or index >= i:
            return False
    return True


expect(test_count, 'should hash a string in to a number less than bucket size',
       test)


def test():
    hash_table = HashTable()
    index = hash_table.hash('hello', 100000)
    return isinstance(index, int) and index == hash_table.hash('hello', 100000)


expect(test_count, 'should hash same key-bucket combination to the same index',
       test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('HashTable Insert Method')
test_count = [0, 0]


def test():
    hash_table = HashTable()
    return (hasattr(hash_table, 'insert') and
            callable(getattr(hash_table, 'insert')))


expect(test_count, 'has insert method', test)


def test():
    hash_table = HashTable()
    hash_table.insert('hello', 'world')
    if not hasattr(hash_table, 'buckets'):
        return False
    index = hash_table.hash('hello', hash_table.buckets)
    return (hash_table.size == 1 and
            type(hash_table.storage[index]) is list and
            len(hash_table.storage[index]) == 1 and
            hash_table.storage[index][0][0] == 'hello' and
            hash_table.storage[index][0][1] == 'world')


expect(test_count, 'can insert a key-value pair into hashtable', test)


def test():
    hash_table = HashTable()
    hash_table.insert('hello', 'world')
    hash_table.insert('foo', 'bar')
    if not hasattr(hash_table, 'buckets'):
        return False
    index1 = hash_table.hash('hello', hash_table.buckets)
    index2 = hash_table.hash('foo', hash_table.buckets)
    return (hash_table.size == 2 and
            type(hash_table.storage[index1]) is list and
            type(hash_table.storage[index2]) is list)


expect(test_count, 'can insert a second key-value pair into hashtable', test)


def test():
    hash_table = HashTable()
    hash_table.insert('hello', 'world')
    hash_table.insert('hello', 'universe')
    if not hasattr(hash_table, 'buckets'):
        return False
    index = hash_table.hash('hello', hash_table.buckets)
    return (hash_table.size == 1 and
            type(hash_table.storage[index]) is list and
            hash_table.storage[index][0][0] == 'hello' and
            hash_table.storage[index][0][1] == 'universe')


expect(test_count, 'can overwrite value if key already exists', test)
print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('HashTable Get Method')
test_count = [0, 0]


def test():
    hash_table = HashTable()
    return (hasattr(hash_table, 'get') and
            callable(getattr(hash_table, 'get')))


expect(test_count, 'has get method', test)


def test():
    hash_table = HashTable()
    hash_table.insert('hello', 'world')
    return hash_table.get('hello') == 'world'


expect(test_count, 'should return correct value for existing input key', test)


def test():
    hash_table = HashTable()
    hash_table.insert('hello', 'world')
    return hash_table.get('bye') is None


expect(test_count, 'should return None if key does not exist', test)
print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('HashTable Remove Method')
test_count = [0, 0]


def test():
    hash_table = HashTable()
    return (hasattr(hash_table, 'remove') and
            callable(getattr(hash_table, 'remove')))


expect(test_count, 'has remove method', test)


def test():
    hash_table = HashTable()
    hash_table.insert('hello', 'world')
    hash_table.remove('hello')
    return (hasattr(hash_table, 'size') and hash_table.size == 0 and
            hash_table.get('hello') is None)


expect(test_count, 'can remove a key-value pair', test)


def test():
    hash_table = HashTable()
    hash_table.insert('hello', 'world')
    hash_table.remove('cat')
    if not hasattr(hash_table, 'buckets'):
        return False
    index = hash_table.hash('hello', hash_table.buckets)
    return (hash_table.size == 1 and
            hash_table.storage[index][0][0] == 'hello' and
            hash_table.storage[index][0][1] == 'world')


expect(test_count, 'does not remove a key-value pair that does not exist',
       test)
print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('HashTable Resize Method')
test_count = [0, 0]


def test():
    hash_table = HashTable()
    return (hasattr(hash_table, 'resize') and
            callable(getattr(hash_table, 'resize')))


expect(test_count, 'has resize method', test)


def test():
    hash_table = HashTable()
    keys = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']
    values = ['0', '1', '2', '3', '4', '5', '6']
    if not hasattr(hash_table, 'buckets'):
        return False
    for i in range(5):
        hash_table.insert(keys[i], values[i])
        if hash_table.buckets != 8:
            return False
    hash_table.insert(keys[5], values[5])
    if hash_table.buckets != 16:
        return False
    hash_table.insert(keys[6], values[6])
    return hash_table.buckets == 16


expect(test_count, 'doubles hashtable number of buckets if load factor is ' +
       'equal to or larger than 0.75', test)


def test():
    hash_table = HashTable()
    keys = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']
    values = ['0', '1', '2', '3', '4', '5', '6']
    if not hasattr(hash_table, 'buckets'):
        return False
    for i in range(6):
        hash_table.insert(keys[i], values[i])
    buckets = hash_table.buckets
    hash_table.remove('four')
    hash_table.remove('five')
    hash_table.remove('six')
    return buckets == hash_table.buckets * 2


expect(test_count, 'halves buckets if load factor drops equal to or below ' +
       '0.25 and bucket length is greater than 8', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
