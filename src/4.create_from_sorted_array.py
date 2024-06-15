class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, arr):
        self.__root = self.__balance(arr, 0, len(arr) - 1)


    def __balance(self, nodes, start, end): # O(n)
        if start > end:
            return None
        mid = start + (end - start) // 2
        node = Node(nodes[mid])
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


values = [ -120, 10, 25, 35, 50, 51, 100, 234, 1200, 1300, 1400, 3000]
print(f'Original arr: {values}')

bst = BinarySearchTree(values)
bst.print_tree()
