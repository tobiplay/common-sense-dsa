from re import S
from typing import List


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node: Node = next_node


class LinkedList:
    def __init__(self, first_node: Node):
        self.first_node = first_node

    def read(self, index):
        # Read

        # We begin at the first node of the list, which
        # is an attribute of LinkedList:
        current_node: Node = self.first_node
        current_index = 0

        # We keep following the links of each node until
        # we get to the # index we're looking for:
        while current_index < index:
            current_node = current_node.next_node
            current_index += 1

            if not current_node:
                # If we reach a point, where there is no
                # next node, we've moved past the end of
                # the linked list:
                return None

        return current_node.data

    def index_of(self, value):
        # Search
        current_node = self.first_node
        current_index = 0

        while current_node:
            # If the current node has the data
            # we're looking for, return its index
            if current_node.data == value:
                return current_index

        # If we reach the end, the value is
        # not part of the linked list.
        return None

    def insert_at_index(self, index, value):
        # Insertion

        # First, we create a new node with the provided value:
        new_node: Node = Node(value)

        # If we insert at the beginning (index == 0):
        if index == 0:
            # Link the new node to the prev. first node,
            # where the next node of the new node is our
            # prev. first node
            new_node.next_node = self.first_node
            # Our new node is now the first node of the linked list:
            self.first_node = new_node
            return

        # If we insert somewhere but the beginning:
        # start at the first node (current node)
        current_node = self.first_node
        current_index = 0

        while current_index < index:
            # Move throught the linked list
            current_node: Node = current_node.next_node
            current_index += 1

        # Link the current node and next (new) node:
        # the next node of our new node is the node
        # that came after the current node (prev. node)
        new_node.next_node = current_node.next_node

        # Point to the new node from the current node,
        # now that the new node comes after the current node
        current_node.next_node = new_node

    def delete_at_index(self, index):
        # Deletion

        # If we're deleting at the start of the linked list:
        if index == 0:
            self.first_node = self.first_node.next_node
            return

        # If we're inserting somewhere else:
        current_index = 0
        current_node = self.first_node

        # Find the node just before the one
        # we're trying to delete
        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1

        # No we've reached the node with the index
        # just 1 before our target
        node_after_deleted_node = current_node.next_node.next_node

        # Link the node one before the one we're deleting
        # to the one that comes after the deleted one
        current_node.next_node = node_after_deleted_node

    def print_all_nodes(self):
        # Start at the first node:
        current_node: Node = self.first_node

        while current_node:
            print(current_node.data)
            current_node = current_node.next_node

    def return_last_element(self):
        # If there is no first node/node at all:
        if not self.first_node:
            return

        current_node: Node = self.first_node
        while current_node.next_node:
            current_node = current_node.next_node

        # If we got here, there is no next node
        return current_node

    ''' Commented-out due to type errors:
    def reverse_linked_list(self):
        current_node: Node = self.first_node
        # The first previous node points to None
        previous_node = None
        # We have to keep track of the next node in the linked list
        # because we'll override it in the algorithm:

        while current_node:
            next_node = current_node.next_node
            current_node.next_node = previous_node  # type: ignore
            previous_node = current_node
            current_node = next_node

        # Once we reached the end, we have to asign a new first
        # node to the linked list. This must be the previous node,
        # because no new current node exists at this point:
        self.first_node = previous_node
    '''

    def delete_via_pointer(self, node_pointer: Node):
        # We want to effectively remove a node from a linked list
        # without interfering with the rest of the linked list.

        # Our first node is the one we're pointing to:
        current_node = node_pointer

        # Copy the data from the next node to the accessing node
        # that we're pointing to, and therefore overriding its data:
        current_node.data = current_node.next_node.data

        # Now point to one past the next node: 
        current_node.next_node = current_node.next_node.next_node

node_1 = Node("once")
node_2 = Node("upon")
node_3 = Node("a")
node_4 = Node("time")

node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

list = LinkedList(node_1)

list.delete_via_pointer(node_3)

list.print_all_nodes()
