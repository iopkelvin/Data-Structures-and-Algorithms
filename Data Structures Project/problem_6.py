'''
Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions.
The union of two sets A and B is the set of elements which are in A, in B, or in both A and B.
The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively.
Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

We have provided a code template below, you are not required to use it:
'''

from collections import OrderedDict

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size


def union(llist_1, llist_2):
    record = set()
    union_list = LinkedList()

    node = llist_1.head
    while node:
        if node.value not in record:
            record.add(node.value)
            union_list.append(node.value)
        node = node.next

    node = llist_2.head
    while node:
        if node.value not in record:
            record.add(node.value)
            union_list.append(node.value)
        node = node.next

    if len(record) == 0:
        return 'No items in the lists'
    return union_list


def intersection(llist_1, llist_2):
    record = dict()
    intersection_list = LinkedList()

    # First list fills in the dictionary keys with 0
    node = llist_1.head
    while node:
        if record.get(node.value) is None:
            record[node.value] = 0
        node = node.next

    # Second list adds items to intersection_list if dictionary keys are 0
    node = llist_2.head
    while node:
        if record.get(node.value) == 0:
            record[node.value] += 1
            intersection_list.append(node.value)
        node = node.next

    if intersection_list.head is None:
        return 'There is no intersection'
    return intersection_list


def print_test(list1, list2):
    print('list 1: ', list1)
    print('list 2: ', list2)
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print('Union:')
    print(union(linked_list_1, linked_list_2))
    print('Intersection:')
    print(intersection(linked_list_1, linked_list_2))
    print('\n')
    return


if __name__ == "__main__":

    print('\tTest 1: ')

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]
    print_test(element_1, element_2)

    print('\tTest 2: ')

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]
    print_test(element_1, element_2)

    print('\tTest 3: ')

    element_1 = ['a', 'b']
    element_2 = [1]
    print_test(element_1, element_2)