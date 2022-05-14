class TreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child: TreeNode = left_child
        self.right_child: TreeNode = right_child


def search(search_value, node: TreeNode):
    # Base case: there is no node, or we found the value
    if node is None or node.value == search_value:
        return node

    if search_value < node.value:
        search(search_value, node.left_child)

    else:
        search(search_value, node.right_child)


def insert(value, node: TreeNode):
    if value < node.value:
        if node.left_child is None:
            node.left_child = TreeNode(value)
        else:
            insert(value, node.left_child)

    elif value > node.value:
        if node.right_child is None:
            node.right_child = TreeNode(value)
        else:
            insert(value, node.right_child)


def delete(value, node: TreeNode):
    # The next node in the tree does not exist
    if node is None:
        return None

    elif value < node.value:
        node.left_child = delete(value, node.leftChild)  # type: ignore
        return node
    elif value > node.value:
        node.rightChild = delete(value, node.rightChild)  # type: ignore
        return node

    elif value == node.value:
        if node.left_child is None:
            return node.right_child
        elif node.right_child is None:
            return node.left_child

    else:
        node.right_child = lift(node.right_child, node)
        return node


def return_greatest_node(node: TreeNode):
    # If there is another right child, traverse that subtree:
    if node.right_child:
        return_greatest_node(node.right_child)
    else:
        return node.value


def lift(node: TreeNode, node_to_del: TreeNode):
    if node.left_child:
        node.lelt_child = lift(node.left_child, node_to_del)  # type: ignore
        return node
    else:
        node_to_del.value = node.value
        return node.right_child


def traverse_and_print(node):
    if node is None:
        return
    traverse_and_print(node.left_child)
    print(node.value)
    traverse_and_print(node.right_child)


node_1 = TreeNode(25)
node_2 = TreeNode(75)
root = TreeNode(50, node_1, node_2)

node_3 = TreeNode(10)
node_4 = TreeNode(33)
node_1.left_child = node_3
node_1.right_child = node_4

node_5 = TreeNode(56)
node_6 = TreeNode(89)
node_2.left_child = node_5
node_2.right_child = node_6

print(root.right_child.right_child.value)
print(return_greatest_node(root))
