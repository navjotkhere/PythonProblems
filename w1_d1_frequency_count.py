#
# Homework - Frequency Count
#
# Utilize the frequency count pattern to solve these problems.  Use a Hash Set
# or an Array instead of a Hash Table where applicable.


# 1. Unique

# Given an array of integers, return an array with all duplicates removed.*

# Parameters
# Input: arr {Array of Integers}
# Output: {Array of Integers}

# Constraints
# Time: O(N)
# Space: O(N)

# Examples
# [1, 2, 4, 4, 5, 6] --> [1, 2, 4, 5, 6]
# [1, 1, 2, 2, 3, 3] --> [1, 2, 3]
# [1, 2, 3, 1, 2] --> [1, 2, 3]


def unique(arr):
    # YOUR WORK HERE
    pass

# 2. Word Count

# Given an body of text, return a hash table of the frequency of each word.

# Parameters
# Input: text {String}
# Output: {Hash Table}

# Constraints
# Capital and lower case versions of the same word should be counted is the same word.
# Remove punctuations from all words.
# Time: O(N)
# Space: O(N)
# Where N is the number of characters in the string.

# Examples
# 'The cat and the hat.' --> '{ the: 2, cat: 1, and: 1, hat: 1 }'`
# 'As soon as possible.' --> '{ as: 2, soon: 1, possible: 1 }'`
# 'It's a man, it's a plane, it's superman!' --> '{ its: 3, a: 2, man: 1, plane: 1, superman: 1 }'`

def word_count(sentence):
    # YOUR WORK HERE
    pass

# 3. RGB Set

# Given a string of characters where each character is either 'r', 'g', or 'b',
# determine the number of complete sets of 'rgb' that can be made with the
# characters.

# Parameters
# Input: str {String}
# Output: {Integer}

# Constraints
# Time: O(N)
# Space: O(1)

# Examples
#  `'rgbrgb' --> 2`
# `'rbgrbrgrgbgrrggbbbbrgrgrgrg' --> 7`
# `'bbrr' --> 0`


def rgb(string):
    # YOUR WORK HERE
    pass

# 4. Missing Number

# Given range of 1 to N and an array of unique integers that are within that
# range, return the missing integers not found in the array

#  Parameters
#  Input: n {Integer}
#  Input: arr {Array of Integers}
#  Output: {Array of Integers}

#  Constraints
#  Time: O(N)
#  Space: O(N)

#  Examples
#  `4, [1, 4, 2] --> [3]`
#  `8, [4, 7, 1, 6] --> [2, 3, 5, 8]`
#  `6, [6, 4, 2, 1] --> [3, 5]`


def missing_number(n, arr):
    # YOUR WORK HERE
    pass


# 5. Letter Sort

#  Given a string of letters, return the letters in sorted order.

#  Parameters
#  Input: str {String}
#  Output: {String}

#  Constraints
#  Time: O(N)
#  Space: O(N)

#  Examples
#  `hello --> ehllo`
#  `whiteboard --> abdehiortw`
#  `one --> eno`


def letter_sort(string):
    # YOUR WORK HERE
    pass


# 6. Character Mode
# Given a string, find the most frequent occurring letter(s) in the string

# Parameters
# Input: str {String}
# Output: {String}

# Constraints
# If more than one letter is tied for the most frequent, return a string of all
# the letters in one string.

# Upper case characters should count as lower case, and do not include spaces
# ... as characters.

# Time: O(N)
# Space: O(N)

# Examples
# 'hello' --> 'l'
# 'A walk in the park' --> 'a'
# 'noon' --> 'no'

def character_mode(string):
    # YOUR WORK HERE
    pass

# 7. Sort Digits

# Given an integer, soft the digits in ascending order and return the new integer.
# Ignore leading zeros.

# Parameters
# Input: num {Integer}
# Output: {Integer}

# Constraints
# Do not convert the integer into a string or other data type.

# Time: O(N) where N is the number of digits.
# Space: O(1)

# Examples
# 8970 --> 789
# 32445 --> 23445
# 10101 --> 111


def sort_digits(n):
    # YOUR WORK HERE
    pass

# 8. Get Duplicates

# Given an array of values, return only the values that have duplicates in the
# array

# Parameters
# Input: arr {Array}
# Output: {Array}

# Constraints
# Time: O(N)
# Space: O(N)

# Examples
# [1, 2, 4, 2] --> [2]
# [3, 2, 3, 2, 3, 3, 4] --> [3, 2]
# [1, 2, 3, 4] --> []


def get_duplicates(arr):
    # YOUR WORK HERE
    pass

# 9. Anagram Pair

# Given two strings, determine if the strings are anagrams of one another.

# Two words are anagrams of one another if they contain the same letters.

# Parameters
# Input: str1 {String}
# Input: str2 {String}
# Output: {Boolean}

# Constraints
# With N as the length of the first string, and M as the length of the second string.
# Time: O(N)
# Space: O(N)

# Examples
# "cat", "act" --> true
# "cat", "dog" --> false
# "racecar", "aaccrres" --> false


def anagram_pair(string1, string2):
    # YOUR WORK HERE
    pass


# 10. Anagram Palindrome

# Given a string, determine if the string can be rearranged to form a palindrome.

# A palindrome is a word that is the same as its reversed. For example: "racecar"
# and "noon" are palindromes because they match their reversed version
# respectively. On the other hand, "cat" is not a palindrome because "cat"
# does not equal "tac".

# Parameters
# Input: str {String}
# Output: {Boolean}

# Constraints
# Assume the string only contains lowercase letters and no spaces.
# Time: O(N)
# Space: O(1)

# Examples
# `"carrace" --> true ("carrace" can be rearranged to "racecar")`
# `"cat" --> false`

def anagram_palindrome(string):
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


print('Unique')
test_count = [0, 0]


def test():
    example = unique([1, 2, 4, 4, 5, 6])
    return example is not None and lists_equal(sorted(example), [1, 2, 4, 5, 6])


expect(test_count, 'should return unique values from sorted list with duplicates', test)


def test():
    example = unique([2, 2, 2, 2, 2, 2, 2])
    return example is not None and lists_equal(example, [2])

expect(test_count, 'should return single value for list with all duplicates', test)


def test():
    example = unique([1, 2, 3, 1, 2])
    return example is not None and lists_equal(sorted(example), [1, 2, 3])

expect(test_count, 'should return unique values from unsorted list with duplicates', test)


def test():
    example = unique([])
    return example is not None and lists_equal(example, [])

expect(test_count, "should return an empty list from empty input", test)


print('\nWord Count')
test_count = [0, 0]


def test():
    example = word_count("The cat and the hat.")
    return example is not None and example == { 'the': 2, 'cat': 1, 'and': 1, 'hat': 1 }

expect(test_count, "should return a dictionary with each word and its frequency", test)


def test():
    example = word_count("It's a man, it's a plane, it's superman!")
    return example is not None and example == {'its': 3, 'a': 2, 'man': 1, 'plane': 1, 'superman': 1}

expect(test_count, "should return dictionary with each word excluding punctuations", test)

def test():
    example = word_count ("")
    return example is not None and example == {}

expect(test_count, "should return empty dictionary for empty string input", test)


print('\nrgb')
test_count = [0, 0]

def test():
    example = rgb('rgbrgb')
    return example is not None and example == 2

expect(test_count, "should return number correct number of rgb from input", test)


def test():
    example = rgb("rbgrbrgrgbgrrggbbbbrgrgrgrg")
    return example is not None and example == 7

expect(test_count, "should return correct number of rgb from input despite characters out of sequence", test)


def test():
    example = rgb("bbrr")
    return example is not None and example == 0

expect(test_count, "should return 0 as output for no number of rgb", test)


def test():
    example = rgb("")
    return example is not None and example == 0

expect(test_count, "should return 0 for empty input", test)


print("\nMissing Number")
test_count = [0, 0]

def test():
    example = missing_number(4, [1, 4, 2])
    return example is not None and lists_equal(example, [3])

expect(test_count, "should return [3] for input of [1, 4, 2]", test)


def test():
    example = missing_number(8, [4, 7, 1, 6])
    return example is not None and lists_equal(example, [2, 3, 5, 8])

expect(test_count, "should return [2, 3, 5, 8] for input of [4, 7, 1, 6]", test)


def test():
    example = missing_number(6, [6, 4, 2, 1])
    return example is not None and lists_equal(example, [3, 5])

expect(test_count, "should return [3, 5] for input of [6, 4, 2, 1]", test)


print("\nLetter Sort")
test_count = [0, 0]

def test():
    example = letter_sort("hello")
    return example is not None and example == "ehllo"

expect(test_count, "should return 'ehllo' for input 'hello'", test)


def test():
    example = letter_sort("whiteboard")
    return example is not None and example == "abdehiortw"

expect(test_count, "should return 'abdehiortw' for input of 'whiteboard'", test)


def test():
    example = letter_sort("one")
    return example is not None and example == "eno"

expect(test_count, "should return 'eno' for input 'one'", test)


print("\nCharacter Mode")
test_count = [0, 0]

def test():
    example = character_mode("hello")
    return example is not None and example == "l"

expect(test_count, "should return 'l' for input 'hello'", test)

def test():
    example = character_mode("A walk in the park")
    return example is not None and example == "a"

expect(test_count, "should return 'a' when input is 'A walk in the park'", test)

def test():
    example = character_mode("noon")
    return example is not None and example == "no"

expect(test_count, "should return 'no' when input is 'noon'", test)


print("\nSort Digits")
test_count = [0, 0]

def test():
    example = sort_digits(8970)
    return example is not None and example == 789

expect(test_count, "should return '789' when input is '8970'", test)

def test():
    example = sort_digits(32445)
    return example is not None and example == 23445

expect(test_count, "should return '23445' when input is '32445'", test)


def test():
    example = sort_digits(10101)
    return example is not None and example == 111

expect(test_count, "should return '111' when input is '10101'", test)


print("\nGet Duplicates")
test_count = [0, 0]

def test():
    example = get_duplicates([1, 2, 4, 2])
    return example is not None and lists_equal(example, [2])

expect(test_count, "should return '[2]' when input is '[1, 2, 4, 2]'", test)


def test():
    example = get_duplicates([3, 2, 3, 2, 3, 3, 4])
    return example is not None and lists_equal(example, [3, 2]) or lists_equal(example, [2, 3])

expect(test_count, "should return '[3, 2]' or '[2, 3]' when input is '[3, 2, 3, 2, 3, 3, 4]'", test)


def test():
    example = get_duplicates([1, 2, 3, 4])
    return example is not None and lists_equal(example, [])

expect(test_count, "should return '[]' when input is '[1, 2, 3, 4]'", test)


print("\nAnagram Pair")
test_count = [0, 0]

def test():
    example = anagram_pair("cat", "act")
    return example is not None and example is True

expect(test_count, "should return True when input is 'cat, act'", test)


def test():
    example = anagram_pair("cat", "dog")
    return example is not None and example is False

expect(test_count, "should return False when input is 'cat, dog'", test)



def test():
    example = anagram_pair("racecar", "aaccrres")
    return example is not None and example is False

expect(test_count, "should return False when input is 'racecar, aaccrres'", test)


print("\nAnagram Palindrome")
test_count = [0, 0]

def test():
    example = anagram_palindrome("carrace")
    return example is not None and example is True

expect(test_count, "should return True when input is 'carrace'", test)

def test():
    example = anagram_palindrome("cat")
    return example is not None and example is False

expect(test_count, "should return False when input is 'cat'", test)
