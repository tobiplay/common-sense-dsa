class Node:
    def __init__(self, data, previous_node=None, next_node=None):
        self.data = data
        self.previous_node: Node = previous_node
        self.next_node: Node = next_node


class DoublyLinkedList:
    def __init__(self, first_node=None, last_node=None):
        self.first_node: Node = first_node
        self.last_node: Node = last_node

    def insert_at_end(self, value):
        new_node: Node = Node(value, None, None)

        # If there's currently no node in the doubly linked list
        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node

    def remove_from_front(self):
        removed_node = self.first_node
        self.first_node = removed_node.next_node
        return removed_node

    def print_all_reverse(self):
        current_node = self.last_node

        while current_node:
            print(current_node.data)
            current_node = current_node.previous_node


class Queue:
    def __init__(self):
        self.data = DoublyLinkedList()

    def enqueue(self, element: Node):
        self.data.insert_at_end(element)

    def dequeue(self):
        return self.data.remove_from_front()

    def read(self):
        if not self.data.first_node:
            return None

        # We can only read fron the first entry:
        return self.data.first_node


node_1 = Node("hey")
node_2 = Node("from")
node_3 = Node("the")
node_4 = Node("beginning")

node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

node_2.previous_node = node_1
node_3.previous_node = node_2
node_4.previous_node = node_3


doubly_linked_list = DoublyLinkedList(node_1, node_4)
doubly_linked_list.print_all_reverse()
