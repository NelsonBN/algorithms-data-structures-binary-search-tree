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



    def search(self, target): # Big-O: O(n) / Big-Theta: Θ(log n)
        return self.__search(self.__root, target)

    def __search(self, node, target):
        if node is None:
            return None

        if node.value == target:
            return node

        if target < node.value:
            return self.__search(node.left, target)

        return self.__search(node.right, target)



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

search = 20
print(f"Search {search}: {bst.search(search) is not None}")

search = 80
print(f"Search {search}: {bst.search(search) is not None}")

search = 200
print(f"Search {search}: {bst.search(search) is not None}")
