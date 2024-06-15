class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



class BinarySearchTree:
    def __init__(self):
        self.__root = None



    def insert(self, value): # Big-O: O(n) / Big-Theta: Θ(log n)
        if self.__root is None:
            self.__root = Node(value)
        else:
            self.__insert(self.__root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.__insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.__insert(node.right, value)



    def balance(self): # O(n)
        nodes = []
        self.__inorder(nodes, self.__root)
        n = len(nodes)
        self.__root = self.__balance(nodes, 0, n - 1)


    def __inorder(self, nodes, curr_node):
        if not curr_node:
            return
        self.__inorder(nodes, curr_node.left)
        nodes.append(curr_node)
        self.__inorder(nodes, curr_node.right)

    def __balance(self, nodes, start, end):
        if start > end:
            return None
        mid = start + (end - start) // 2
        node = nodes[mid]
        node.left = self.__balance(nodes, start, mid - 1)
        node.right = self.__balance(nodes, mid + 1, end)
        return node



    def print_tree(self):
        self.__print_tree(self.__root, "", True)

    def __print_tree(self, node, indent, last):
        if node is not None:
            print(indent, end='')
            if last:
                print("R -> ", end='')
                indent += "     "
            else:
                print("L -> ", end='')
                indent += "|    "

            print(node.value)
            self.__print_tree(node.left, indent, False)
            self.__print_tree(node.right, indent, True)



bst = BinarySearchTree()

bst.insert(12)
bst.insert(24)
bst.insert(29)
bst.insert(33)
bst.insert(45)
bst.insert(61)
bst.insert(70)
bst.insert(80)
bst.insert(92)

# bst.insert(50)
# bst.insert(44)
# bst.insert(55)
# bst.insert(32)
# bst.insert(56)
# bst.insert(29)
# bst.insert(71)
# bst.insert(25)
# bst.insert(82)
# bst.insert(21)
# bst.insert(93)


print("Original BST:")
bst.print_tree()

bst.balance()

print("Balanced BST:")
bst.print_tree()
