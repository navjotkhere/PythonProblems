#
#  Homework - Trie
#
#  Problem 1: TrieNode class
#
#  Prompt:    Create a TrieNode class
#             The TrieNode class should contain the following properties:
#
#                 value:   {Character} - default None
#                  next:   {Dictionary}
#                   end:   {Boolean}
#
#
#               Example:   sample = TrieNode("b")
#                          sample.value     # "b"
#                          sample.end       # False
#
#  Problem 2:  Trie class
#
#  Prompt:     Create a Trie class
#              The Trie class should contain the following properties:
#
#                  root:   {TrieNode}
#
#              The Trie class should also contain the following methods:
#
#                insert:   A method that adds a word.
#
#                          Input:     word {String}
#                          Output:    {None}
#
#                isWord:   A method that checks whether a word is in the trie.
#
#                          Input:     word {String}
#                          Output:    {Boolean}
#
#              isPrefix:   A method that checks whether an input is a prefix of
#                          a word in the string.
#
#                          Input:     prefix {String}
#                          Output:    {Boolean}
#
#            startsWith:   A method that returns all words that starts with an
#                          input prefix.
#
#                          Input:     prefix {String}
#                          Output:    {List of Strings}
#
#          EXTRA CREDIT:
#                remove:   Removes a word from the trie.
#
#                          Input:     word {String}
#                          Output:    {None}
#


class TrieNode:

    def __init__(self, value=None):
        # YOUR WORK HERE
        pass


class Trie:

    def __init__(self):
        # YOUR WORK HERE
        pass

    def insert(self, word):
        # YOUR WORK HERE
        pass

    def is_word(self, word):
        # YOUR WORK HERE
        pass

    def is_prefix(self, prefix):
        # YOUR WORK HERE
        pass

    def starts_with(self, prefix):
        # YOUR WORK HERE
        pass

    def remove(self, word):
        # YOUR WORK HERE
        pass




# ###########################################################
# ##############  DO NOT TOUCH TEST BELOW!!!  ###############
# ###########################################################

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


def lists_matching(lst1, lst2):
    if len(lst1) != len(lst2):
        return False

    cache = {}
    for i in range(0, len(lst1)):
        if lst1[i] in cache:
            cache[lst1[i]] += 1
        else:
            cache[lst1[i]] = 1
    for j in range(0, len(lst2)):
        if lst2[j] not in cache or cache[lst2[j]] == 0:
            return False
        cache[lst2[j]] -= 1
    return True


print('TrieNode Class')
test_count = [0, 0]


def test():
    node = TrieNode()
    return isinstance(node, object)


expect(test_count, 'able to create an instance', test)


def test():
    node = TrieNode()
    return hasattr(node, 'value')


expect(test_count, 'has value property', test)


def test():
    node = TrieNode()
    return hasattr(node, 'value') and node.value is None


expect(test_count, 'has default value set to None', test)


def test():
    node = TrieNode()
    return hasattr(node, 'end')


expect(test_count, 'has a end property', test)


def test():
    node = TrieNode()
    return hasattr(node, 'end') and node.end is False


expect(test_count, 'end property initially instantiated to false', test)


def test():
    node = TrieNode()
    node.end = True
    return node.end is True


expect(test_count, 'able to assign a end upon instantiation', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Trie Class')
test_count = [0, 0]


def test():
    trie = Trie()
    return isinstance(trie, object)


expect(test_count, 'able to create an instance', test)


def test():
    trie = Trie()
    return hasattr(trie, 'root')


expect(test_count, 'has root property', test)


def test():
    trie = Trie()
    return hasattr(trie, 'root') and isinstance(trie.root, object)


expect(test_count, 'root property is a TrieNode', test)


def test():
    trie = Trie()
    return hasattr(trie, 'root') and trie.root.value == None


expect(test_count, 'root node value is set to None', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Trie Insert Method')
test_count = [0, 0]


def test():
    trie = Trie()
    return hasattr(trie, 'insert') and callable(getattr(trie, 'insert'))


expect(test_count, 'has insert method', test)


def test():
    trie = Trie()
    trie.insert('cat')
    if hasattr(trie, 'root'):
        c = trie.root.next['c']
        a = c.next['a']
        t = a.next['t']
    return hasattr(trie, 'root') and c != None and a != None and t != None and t.end and not a.end and not c.end


expect(test_count, 'able to insert a word into empty trie', test)


def test():
    trie = Trie()
    trie.insert('cat')
    trie.insert('cats')
    if hasattr(trie, 'root'):
        c = trie.root.next['c']
        a = c.next['a']
        t = a.next['t']
        s = t.next['s']
    return hasattr(trie, 'root') and c != None and a != None and t != None and s != None and s.end and t.end and not a.end and not c.end


expect(test_count, 'able to insert words that overlap into trie', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Trie IsWord Method')
test_count = [0, 0]


def test():
    trie = Trie()
    return hasattr(trie, 'is_word') and callable(getattr(trie, 'is_word'))


expect(test_count, 'has is_word method', test)


def test():
    trie = Trie()
    return trie.is_word('') == False


expect(test_count, 'should return false for an empty string as input', test)


def test():
    trie = Trie()
    return trie.is_word('cat') == False


expect(test_count, 'should return false for a word that doesn\'t exist', test)


def test():
    trie = Trie()
    trie.insert('cat')
    return trie.is_word('cat') == True


expect(test_count, 'should return true for a word that exists', test)


def test():
    trie = Trie()
    trie.insert('cat')
    trie.insert('cats')
    return trie.is_word('cat') == True


expect(test_count, 'should return true for a word that exists within larger word', test)


def test():
    trie = Trie()
    trie.insert('cat')
    trie.insert('cats')
    return trie.is_word('cats') == True


expect(test_count, 'should return true for a word that is a larger word', test)


def test():
    trie = Trie()
    trie.insert('cats')
    return trie.is_word('cat') == False


expect(test_count, 'should return false if a smaller word was not added, but exists in a larger word', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')



print('Trie StartsWith Method')
test_count = [0, 0]


def test():
    trie = Trie()
    return hasattr(trie, 'starts_with') and callable(getattr(trie, 'starts_with'))


expect(test_count, 'has starts_with method', test)


def test():
    trie = Trie()
    results = trie.starts_with('cats')
    return results is not None and len(results) == 0


expect(test_count, 'should return an empty array if no words start with input', test)


def test():
    trie = Trie()
    trie.insert('cat')
    trie.insert('cats')
    trie.insert('catnip')
    trie.insert('car')
    trie.insert('cars')
    results = trie.starts_with('car')
    return results is not None and len(results) == 2 and lists_matching(results, ['car', 'cars'])


expect(test_count, 'returns correct prefixes including input that is a word', test)


def test():
    trie = Trie()
    trie.insert('cat')
    trie.insert('cats')
    trie.insert('catnip')
    trie.insert('car')
    trie.insert('cars')
    results = trie.starts_with('ca')
    return results is not None and len(results) == 5 and lists_matching(results, ['car', 'cars', 'catnip', 'cat', 'cats'])


expect(test_count, 'returns correct prefixes', test)


def test():
    trie = Trie()
    trie.insert('cat')
    trie.insert('cats')
    trie.insert('catnip')
    trie.insert('car')
    trie.insert('cars')
    results = trie.starts_with('')
    return results is not None and len(results) == 5 and lists_matching(results, ['cat', 'cats', 'catnip', 'car', 'cars'])


expect(test_count, 'returns all words if input is empty string', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')



print('Trie Remove Method')
test_count = [0, 0]

def test():
    trie = Trie()
    return hasattr(trie, 'remove') and callable(getattr(trie, 'remove'))


expect(test_count, 'has remove method', test)


def test():
    trie = Trie()
    trie.insert('cat')
    trie.remove('cat')
    return trie.is_word('cat') == False and not 'c' in trie.root.next


expect(test_count, 'removes a word that exists', test)


def test():
    trie = Trie()
    trie.insert('cat')
    trie.remove('c')
    return trie.is_word('cat') == True and 'c' in trie.root.next


expect(test_count, 'does not remove a word that does not exist', test)


def test():
    trie = Trie()
    trie.insert('hello')
    trie.insert('hell')
    trie.insert('he')
    trie.remove('hell')
    return trie.is_word('he') and trie.is_word('hello') and not trie.is_word('hell')


expect(test_count, 'does not remove letters that belong to a longer word', test)


def test():
    trie = Trie()
    trie.insert('cat')
    trie.insert('cats')
    trie.insert('catnip')
    trie.remove('catnip')
    return trie.is_word('cat') and trie.is_word('cats') and not trie.is_word('catnip') and not 'n' in trie.root.next['c'].next['a'].next['t'].next


expect(test_count, 'removes letters from longer word and keeps shorter letters', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
