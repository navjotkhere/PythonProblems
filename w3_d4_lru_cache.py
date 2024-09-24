#
#  Homework - LRU Cache
#
#  Problem: LRU Cache Class
#
#  Instructions: LRU Cache is a popular and challenging algorithm question
#                commonly asked during whiteboarding and tech screen sessions.
#
#                While difficult, this exercise is a good problem to test your
#                ability to build and manipulate data structures.
#
#                Design and implement a data structure for a Least Recently
#                Used (LRU) Cache.
#
#                This implementation involves a doubly linked list and a hash map.
#
#          NOTE: A LRU caching scheme is designed to remove the least recently
#                used item when a new item is added to the cache which is
#                currently at or has just reached capacity.
#
#                An item is considered to be recently used if it has just been
#                accessed or added.
#
#          I.  Node Class
#              Create a Node class
#
#              The Node class should contain the following properties:
#              key: {String}
#              value: {String}
#              previous: {Node} (initially None)
#              next: {Node} (initially None)
#
#         II.  LRUCache Class
#              Create an LRUCache class
#
#              The LRUCache class should contain the following properties:
#              capacity: {Integer}
#              count: {Integer} (initially 0)
#              cache: {Hash Table} The keys represent unique ids of each node, and the values represent the node objects
#                                that possess those keys.
#              head: {Node}
#              tail: {Node}
#
#     Your LRU cache should have the following methods:
#
#      get(key): Retreives a value from the cache (will always be positive) at
#                the key if the key exists in the cache, otherwise returns -1.
#
# set(key,value): Inserts the value at the key or creates a new key:value entry
#                if key is not present. When the cache reaches its capacity, it
#                should invalidate the least recently used item before
#                inserting a new item.
#
#          HINT: Consider what data structure(s) might be neccessary to
#                implement the LRU Cache
#
#     Example:
#     lruCache = new LRUCache(3);
#     lruCache.set('doc', 'david');
#     lruCache.set('cpo', 'joshua');
#     lruCache.set('ceo', 'andy');
#
#     lruCache.get('doc'); => 'david'
#     lruCache.set('swe', 'ron');
#     lruCache.get('cpo'); => -1
#


class Node:
  pass

class LRUCache:
  pass

  # Time Complexity:
  # Auxiliary Space Complexity:
  def add_node(self, node):
    """
    Helper function: adds a node right after the head.
    """
    pass

    # Time Complexity:
    # Auxiliary Space Complexity:
  def remove_node(self, node):
    """
    Helper function: Removes a node from its position.
    """
    pass

  # Time Complexity:
  # Auxiliary Space Complexity:
  def move_to_head(self, node):
    """
    Helper function: Moves a node to the position right after the head.
    """
    pass


  # Time Complexity:
  # Auxiliary Space Complexity:
  def remove_from_tail(self):
    """
    Helper function: Removes the node right before the tail.
    """
    pass


  # Time Complexity:
  # Auxiliary Space Complexity:
  def get(self, key):
    pass


  # Time Complexity:
  # Auxiliary Space Complexity:
  def set(self, key, value):
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

from io import StringIO
import sys
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


def capture_print(toRun):
  with Capturing() as output:
    pass
  with Capturing(output) as output:  # note the constructor argument
    toRun()
  return output


print('LRU Cache tests')
test_count = [0, 0]

def test():
  lru_cache = LRUCache(3)
  lru_cache.set('doc', 'david')
  lru_cache.set('cpo', 'joshua')
  lru_cache.set('ceo', 'andy')
  example1 = lru_cache.get('doc')
  example2 = lru_cache.get('cpo')
  example3 = lru_cache.get('ceo')
  return example1 == 'david' and example2 == 'joshua' and example3 == 'andy'
expect(test_count, 'should be able to set and get key-value pairs', test)

def test():
  lru_cache = LRUCache(3)
  lru_cache.set('student', 'henry')
  lru_cache.set('student', 'eliza')
  example = lru_cache.get('student')
  return example == 'eliza'
expect(test_count, 'should be able overwrite values with same keys when using set method', test)

def test():
  lru_cache = LRUCache(3)
  lru_cache.set('dentist', 'akali')
  lru_cache.set('doctor', 'swain')
  lru_cache.set('lawyer', 'kennan')
  lru_cache.set('judge', 'leona')
  return lru_cache.get('dentist') == -1
expect(test_count, 'old key value pairs should be removed when capacity has been exceeded', test)

def test():
  lru_cache = LRUCache(3)
  lru_cache.set('doc', 'david')
  lru_cache.set('cpo', 'joshua')
  lru_cache.set('ceo', 'andy')
  lru_cache.get('doc')
  lru_cache.set('swe', 'ron')
  return lru_cache.get('cpo') == -1
expect(test_count, 'most recently modified/viewed items should be moved to front of LRU cache while stale items are moved to end', test)

def test():
  lru_cache = LRUCache(3)
  lru_cache.set('one', 1)
  lru_cache.set('two', 2)
  lru_cache.set('three', 3)
  lru_cache.set('four', 4)
  lru_cache.set('five', 5)
  lru_cache.set('six', 6)
  ex1 = lru_cache.get('one')
  ex2 = lru_cache.get('two')
  ex3 = lru_cache.get('three')
  ex4 = lru_cache.get('four')
  ex5 = lru_cache.get('five')
  ex6 = lru_cache.get('six')
  return ex1 == -1 and ex2 == -1 and ex3 == -1 and ex4 == 4 and ex5 == 5 and ex6 == 6
expect(test_count, 'should be able to replace multiple stale items', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
