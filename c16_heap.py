from math import floor


class Heap:
    def __init__(self, data: list[int]):
        self.data: list[int] = data

    def root_node(self) -> int:
        return self.data[0]

    def last_node(self) -> int:
        return self.data[-1]

    def left_child_index(self, index) -> int:
        return (index * 2) + 1

    def right_child_index(self, index) -> int:
        return (index * 2) + 2

    # We just want to omit everything after the comma
    def parent_index(self, index: int) -> int:
        return floor((index - 1) / 2)

    def insert(self, value) -> None:
        self.data.append(value)
        new_node_index = len(self.data) - 1

        # Perform the trickle-up algorithm, starting with the "last node"
        # in the array -> as long as the val of the new node is bigger than the
        # parent node:
        while new_node_index > 0 and self.data[new_node_index] > self.data[self.parent_index(new_node_index)]:
            # Swap the parent node and the new node.
            self.data[self.parent_index(
                new_node_index)], self.data[new_node_index] = self.data[new_node_index], self.data[self.parent_index(new_node_index)]
            # "Swap" the index of the previous parent and the new node.
            new_node_index = self.parent_index(new_node_index)

    def has_greater_child(self, index):
        # We check whether the node at index has left and right
        # children and if either of those children are greater
        # than the node at index:
        return (self.data[self.left_child_index(index)] and self.data[self.left_child_index(
            index)] > self.data[index] or self.data[self.right_child_index(index)] and self.data[self.right_child_index(index)] > self.data[index])

    def calculate_larger_child_index(self, index) -> int:
        # --- missing ---
        return 1

    def delete(self) -> None:
        # Delete does not need any argument, because we only ever delete
        # the root node.

        # Pop the last node off the array and insert at the very beginning:
        self.data[0] = self.data.pop()

        # Keep track of the index of the trickle node:
        trickle_node_index = 0

        # Trickle down algorithm -> run as long as there is a child greater
        # than the current node:
        while self.has_greater_child(trickle_node_index):
            # Find the index of the larger child and save that in a var:
            larger_child_index = self.calculate_larger_child_index(
                trickle_node_index)

            # Swap the trickle node with its larger child:
            self.data[larger_child_index], self.data[trickle_node_index] = self.data[trickle_node_index], self.data[larger_child_index]

            # Also swap the index of those nodes:
            trickle_node_index = larger_child_index


heap_1 = Heap([100, 88, 25])
print(heap_1.root_node())
