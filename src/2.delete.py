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



    def delete(self, target): # Big-O: O(n) / Big-Theta: Θ(log n)
        self.__root = self.__delete(self.__root, target)

    def __delete(self, node, target):
        if node is None:
            return None

        if target < node.value:
            node.left = self.__delete(node.left, target)
        elif target > node.value:
            node.right = self.__delete(node.right, target)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.value = self.__minOfRightSubTree(node.right)
            node.right = self.__delete(node.right, node.value)

        return node

    def __minOfRightSubTree(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value



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
bst.insert(50)
bst.insert(90)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(10)
bst.insert(60)
bst.insert(80)

bst.print_tree()


print("\nDelete 20:")
bst.delete(20)

bst.print_tree()


print("\nDelete 70:")
bst.delete(70)

bst.print_tree()


print("\nDelete 50:")
bst.delete(50)

bst.print_tree()
