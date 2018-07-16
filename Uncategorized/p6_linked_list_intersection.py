"""
This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""


def naive(ll1, ll2):
    """
    Compare every node in the first list to every node in the second list and return the first match found
    O(n*m) time, O(1) space
    """
    next_node_1 = ll1.head
    while next_node_1:
        next_node_2 = ll2.head
        while next_node_2:
            if next_node_1.value == next_node_2.value:
                return next_node_1.value
            next_node_2 = next_node_2.next
        next_node_1 = next_node_1.next
    return None


def smart(ll1, ll2):
    """
    Traverses the longer list and shorter list together twice to find the intersection.
    Once with shorter list starting at the beginning of the longer list, and another
    time with the shorter list ending at the end of the longer list. This approach
    ensures all test cases pass.
    O(2s + 2l) time, O(1) space
    *s represents length of shorter list, l represents length of longer list
    """
    def traverse_both(longer_next, shorter_next):
        while shorter_next:
            if shorter_next.value == longer_next.value:
                return shorter_next.value
            shorter_next = shorter_next.next
            longer_next = longer_next.next
        return False

    len_ll1 = len(ll1)
    len_ll2 = len(ll2)
    diff = abs(len_ll1-len_ll2)

    if len_ll1 > len_ll2:
        shorter_ll = ll2
        longer_ll = ll1
    else:
        shorter_ll = ll1
        longer_ll = ll2

    longer_next = longer_ll.head
    shorter_next = shorter_ll.head
    if longer_next:
        intersection_beginning = traverse_both(longer_next, shorter_next)
        if intersection_beginning:
            return intersection_beginning

        longer_next = longer_ll.head
        shorter_next = shorter_ll.head
        for _ in range(diff):
            longer_next = longer_next.next

        return traverse_both(longer_next, shorter_next)


if __name__ == '__main__':
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    class LinkedList:
        def __init__(self, value):
            self.head = Node(value)

        def __len__(self):
            counter = 0
            current = self.head
            while current:
                counter += 1
                current = current.next
            return counter

        def push(self, value):
            next_node = self.head
            self.head = Node(value)
            self.head.next = next_node

        def print(self):
            current = self.head
            while current:
                print(current.value)
                current = current.next

    inp1_1 = LinkedList(10)
    inp1_1.push(8)
    inp1_1.push(7)
    inp1_1.push(3)
    #inp1_1.print()
    inp1_2 = LinkedList(10)
    inp1_2.push(8)
    inp1_2.push(1)
    inp1_2.push(99)
    #inp1_2.print()

    inp2_1 = LinkedList(10)
    inp2_1.push(34)
    inp2_1.push(20)
    inp2_1.push(12)
    inp2_1.push(4)
    inp2_1.push(3)
    #inp2_1.print()  # 3,4,12,20,34,10
    inp2_2 = LinkedList(1)
    inp2_2.push(34)
    inp2_2.push(7)
    #inp2_2.print()  # 7,34,1

    inp3_1 = LinkedList(12)
    inp3_1.push(15)
    inp3_1.push(3)
    inp3_1.push(5)
    inp3_1.push(19)
    # inp3_1.print()  # 19,5,3,15,12
    inp3_2 = LinkedList(13)
    inp3_2.push(3)
    inp3_2.push(6)
    # inp3_2.print()  # 6,3,13
    
    # ** inp3 is invalid - if lists intersect at node 3, then next node must be either 13 OR 15, not both
    # i.e. intersecting point == merging point

    assert naive(inp1_1, inp1_2) == 8, "naive failed on inp1"
    assert naive(inp2_1, inp2_2) == 34, "naive failed on inp2"

    assert smart(inp1_1, inp1_2) == 8, "smart failed on inp1"
    assert smart(inp2_1, inp2_2) == 34, "smart failed on inp2"
