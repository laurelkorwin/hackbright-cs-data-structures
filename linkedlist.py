"""DISCUSSION QUESTIONS"""

"""
1. Given the linked list below, which are the nodes? What is the data for each 
node? Where is the head? Where is the tail? (Please be as specific as possible —
exactly which parts of the diagram correspond to each part? Arrows? Boxes? Text?)

A: Each node is represented by a pair of boxes. The first box represents the "data" stored
on the node, and the second box representing the "next" reference also stored on each node.

The head is the node w/data "Apple". Specifically, the head is a separate variable that
points to that particular node.

The tail is the node w/data "Cherry". Although it is not specified in this diagram,
in the best case scenario there would be a separate variable called 'tail' that would
point to the node whose 'next' is none.

2. What’s the difference between doubly- and singly-linked lists?

A. Singly linked lists are only linked in one direction (going from head to tail).
Doubly linked lists contain pointers / references between nodes in both directions.

3. Why is it faster to append to a linked list if we keep track of the tail as an attribute?

A. If you did not keep track of the tail, every time you wanted to append you would have to
loop through the entire list to find the node whose next was None. If you keep track of the tail,
you can just access that variable to find the node whose next is None and append to that.

"""

# Linked list with Node/LinkedList classes


class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node %s>" % self.data


class LinkedList(object):
    """Linked List using head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        """Add node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def remove_node_by_index(self, index):
        """Remove node with given index."""

        prev = None
        node = self.head
        i = 0

        while (node is not None) and (i < index):
            prev = node
            node = node.next
            i += 1

        if prev is None:
            self.head = node.next
        else:
            prev.next = node.next

    def find_node(self, data):
        """Is a matching node in the list?"""

        current = self.head

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False

    def print_list(self):
        """Print all items in the list::

            >>> ll = LinkedList()
            >>> ll.add_node('dog')
            >>> ll.add_node('cat')
            >>> ll.add_node('fish')

            >>> ll.print_list()
            dog
            cat
            fish
        """

        current = self.head

        while current is not None:
            print current.data
            current = current.next

    def get_node_by_index(self, idx):
        """Return a node with the given index::

            >>> ll = LinkedList()
            >>> ll.add_node('dog')
            >>> ll.add_node('cat')
            >>> ll.add_node('fish')

            >>> ll.get_node_by_index(0)
            <Node dog>

            >>> ll.get_node_by_index(2)
            <Node fish>
        """

        current = self.head
        counter = 0

        while current is not None:
            if counter == idx:
                return current
            else:
                counter += 1
                current = current.next


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

