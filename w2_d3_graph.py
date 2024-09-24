#
#  Homework - Graph
#
#  Problem: Graph
#
#  Prompt: Create a directed graph class using adjacency list edge
#          representation.
#
#            storage: {Hash Table} - the keys represent unique vertex ids and
#                     the values are arrays of Integers representing the vertex
#                     ids of its neighors.
#
#  The Graph will also have the following methods:
#
#           add_vertex: Method that accepts a vertex id {Integer} and adds the
#                      vertex to the graph.  Return true if success and false
#                      if failed.
#
#                       Input:    id {Integer}
#                      Output:    {Boolean}
#
#        remove_vertex: Method that accepts a vertex id and removes the vertex
#                      with the matching id. Return true if success and false
#                      if failed.
#
#                       Input:    id {Integer}
#                      Output:    {Boolean}
#
#             add_edge: Method that accepts two vertex ids and creates a
#                      directed edge from the first vertex to the second.
#                      Returns true if success and false if failed.
#
#                       Input:    id1 {Integer}
#                       Input:    id2 {Integer}
#                      Output:    {Boolean}
#
#          remove_Edge: Method that accepts two vertex id's and removes the
#                      directed edge from the first vertex to the second.
#                      Returns true if success and false if failed.
#
#                       Input:    id1 {Integer}
#                       Input:    id2 {Integer}
#                      Output:    {Boolean}
#
#          is_vertex:  Method that accepts an id, and returns whether the
#                      vertex exists in the graph.
#
#                      Input:    id {Integer}
#                      Output:   {Boolean}
#
#           neighbors: Method that accepts a vertex id, and returns all of the
#                      edges of that vertex.
#
#                      Input:    id {Integer}
#                      Output:   {Boolean}
#
#  Input:  {None}
#  Output: {Graph}
#
#  Notes:  The notation for Time/Auxiliary Space Complexity for graphs is
#          slightly different since certain functions depend on either the
#          either the number of vertices, edges, or both
#
#          O(V) = Linear w/ respect to the number of vertices
#          O(E) = Linear w/ respect to the number of all edges
#          O(V+E) = Linear w/ respect to the number of vertices plus edges
#


class Graph:
    def __init__(self):
        # YOUR WORK HERE
        pass

    # Time Complexity:
    # Auxiliary Space Complexity:
    def add_vertex(self, id):
        # YOUR WORK HERE
        pass

    # Time Complexity:
    # Auxiliary Space Complexity:
    def remove_vertex(self, id):
        # YOUR WORK HERE
        pass

    # Time Complexity:
    # Auxiliary Space Complexity:
    def add_edge(self, id1, id2):
        # YOUR WORK HERE
        pass

    # Time Complexity:
    # Auxiliary Space Complexity:
    def remove_edge(self, id1, id2):
        # YOUR WORK HERE
        pass

    # Time Complexity:
    # Auxiliary Space Complexity:
    def is_vertex(self, id):
        # YOUR WORK HERE
        pass

    # Time Complexity:
    # Auxiliary Space Complexity:
    def neighbors(self, id):
        # YOUR WORK HERE
        pass


# ###########################################################
# ##############  DO NOT TOUCH TEST BELOW!!!  ###############
# ###########################################################


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


# code for checking if lists contain the same elements
# (do not need to be in the same order)
def lists_matching(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    else:
        lib = {}
        for i in range(0, len(lst1)):
            lib[lst1[i]] = True
        for j in range(0, len(lst2)):
            if lib[lst2[j]] is None:
                return False
        return True


print('Graph Class')
test_count = [0, 0]


def test():
    graph = Graph()
    return isinstance(graph, object)


expect(test_count, 'able to create an instance', test)


def test():
    graph = Graph()
    return hasattr(graph, 'storage')


expect(test_count, 'has storage property', test)


def test():
    graph = Graph()
    return (hasattr(graph, 'storage') and
            type(graph.storage) is dict)


expect(test_count, 'storage property initialized to an empty dictionary', test)


expect(test_count, 'able to create an instance', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Graph add_vertex method')
test_count = [0, 0]


def test():
    graph = Graph()
    return (hasattr(graph, 'add_vertex') and
            callable(getattr(graph, 'add_vertex')))


expect(test_count, 'has add_vertex method', test)


def test():
    graph = Graph()
    graph.add_vertex(5)
    return (hasattr(graph, 'storage') and
            len(graph.storage) == 1)


expect(test_count, 'is able to add a vertex', test)


def test():
    graph = Graph()
    graph.add_vertex(5)
    return (hasattr(graph, 'storage') and
            type(graph.storage[5]) is list)


expect(test_count, 'vertices store a list of connections', test)


def test():
    graph = Graph()
    graph.add_vertex(5)
    graph.add_vertex(10)
    return (hasattr(graph, 'storage') and
            len(graph.storage) == 2 and
            5 in graph.storage and 10 in graph.storage)


expect(test_count, 'is able to add two vertices', test)


def test():
    graph = Graph()
    graph.add_vertex(5)
    graph.add_vertex(5)
    return len(graph.storage) == 1


expect(test_count, 'does not add in duplicate vertex', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Graph add_edge method')
test_count = [0, 0]


def test():
    graph = Graph()
    return hasattr(graph, 'add_edge') and callable(getattr(graph, 'add_edge'))


expect(test_count, 'has add_edge method', test)


def test():
    graph = Graph()
    graph.add_vertex(5)
    graph.add_vertex(10)
    result = graph.add_edge(5, 10)
    return (hasattr(graph, 'storage') and
            len(graph.storage[5]) == 1 and
            len(graph.storage[10]) == 0 and
            result)


expect(test_count, 'able to create an edge between two vertices that exist',
       test)


def test():
    graph = Graph()
    graph.add_vertex(5)
    result = graph.add_edge(5, 10)
    return (hasattr(graph, 'storage') and
            len(graph.storage[5]) == 0 and
            10 not in graph.storage and not
            result)


expect(test_count, 'does not create an edge when one of the vertices does ' +
       'not exist', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Graph remove_edge method')
test_count = [0, 0]


def test():
    graph = Graph()
    return (hasattr(graph, 'remove_edge') and
            callable(getattr(graph, 'remove_edge')))


expect(test_count, 'has remove_edge method', test)


def test():
    graph = Graph()
    graph.add_vertex(5)
    graph.add_vertex(10)
    graph.add_edge(5, 10)
    result = graph.remove_edge(5, 10)
    return (hasattr(graph, 'storage') and
            len(graph.storage[5]) == 0 and
            len(graph.storage[10]) == 0 and
            result)


expect(test_count, 'able to remove an edge between two vertices', test)


def test():
    graph = Graph()
    graph.add_vertex(5)
    graph.add_vertex(10)
    graph.add_edge(5, 10)
    result = graph.remove_edge(6, 10)
    return (hasattr(graph, 'storage') and
            len(graph.storage[5]) == 1 and
            6 not in graph.storage and not result)


expect(test_count, 'does not remove edge when edge does not exist', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Graph remove_vertex method')
test_count = [0, 0]


def test():
    graph = Graph()
    return (hasattr(graph, 'remove_vertex') and
            callable(getattr(graph, 'remove_vertex')))


expect(test_count, 'has remove_vertex method', test)


def test():
    graph = Graph()
    graph.add_vertex(5)
    result = graph.remove_vertex(5)
    return (hasattr(graph, 'storage') and
            len(graph.storage) == 0 and result)


expect(test_count, 'able to remove a vertex within graph', test)


def test():
    graph = Graph()
    graph.add_vertex(5)
    result = graph.remove_vertex(10)
    return (hasattr(graph, 'storage') and
            len(graph.storage) == 1 and not result)


expect(test_count, 'does not remove vertex that does not exist', test)


def test():
    graph = Graph()
    graph.add_vertex(5)
    graph.add_vertex(10)
    graph.add_vertex(15)
    graph.add_edge(5, 10)
    graph.add_edge(5, 15)
    graph.add_edge(10, 5)
    graph.add_edge(15, 10)
    result = graph.remove_vertex(5)
    return (hasattr(graph, 'storage') and
            len(graph.storage) == 2 and
            len(graph.storage[10]) == 0 and
            len(graph.storage[15]) == 1 and
            result)


expect(test_count, 'removes a vertex while safely removing edges connected ' +
       'to node', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print('Graph is_vertex method')
test_count = [0, 0]


def test():
    graph = Graph()
    return hasattr(graph, 'is_vertex') and callable(getattr(graph, 'is_vertex'))


expect(test_count, 'has is_vertex method', test)


def test():
    graph = Graph()
    graph.add_vertex(5)
    return graph.is_vertex(5) is True


expect(test_count, 'returns true when a vertex exists', test)


def test():
    graph = Graph()
    return graph.is_vertex(5) is False


expect(test_count, 'returns false when a vertex doesn\'t exist', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Graph neighbors method')
test_count = [0, 0]


def test():
    graph = Graph()
    return hasattr(graph, 'neighbors') and callable(getattr(graph, 'neighbors'))


expect(test_count, 'has neighbors method', test)


def test():
    graph = Graph()
    return graph.neighbors(5) is None


expect(test_count, 'returns None if the vertex doesn\'t exist', test)


def test():
    graph = Graph()
    graph.add_vertex(5)
    return graph.neighbors(5) is not None and len(graph.neighbors(5)) == 0


expect(test_count, 'returns an empty list if vertex has no edges', test)


def test():
    graph = Graph()
    graph.add_vertex(5)
    graph.add_vertex(10)
    graph.add_vertex(15)
    graph.add_vertex(20)
    graph.add_edge(5, 10)
    graph.add_edge(5, 15)
    graph.add_edge(5, 20)
    result = graph.neighbors(5)
    return (result is not None and len(result) == 3 and
            lists_matching(result, [10, 15, 20]))


expect(test_count, 'returns neighbors if edges exist for a vertex', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
