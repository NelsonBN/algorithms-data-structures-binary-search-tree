class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None



class BinarySearchTree:
    def __init__(self):
        self.__root = None


    def insert(self, key): # Big-O: O(n) / Big-Theta: O(log n)
        if self.__root is None:
            self.__root = Node(key)
        else:
            self.__insert(self.__root, key)

    def __insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self.__insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self.__insert(node.right, key)


    def search(self, key): # Big-O: O(n) / Big-Theta: O(log n)
        return self.__search(self.__root, key)

    def __search(self, node, key):
        if node is None:
            return None

        if node.key == key:
            return node

        if node.key < key:
            return self.__search(node.right, key)

        return self.__search(node.left, key)


    def delete(self, key): # Big-O: O(n) / Big-Theta: O(log n)
        self.__root = self.__delete(self.__root, key)

    def __delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self.__delete(node.left, key)
        elif key > node.key:
            node.right = self.__delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.key = self.__minKey(node.right)
            node.right = self.__delete(node.right, node.key)

        return node

    def __minKey(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key



    def print_tree(self):
        self.__print_tree(self.__root, "", True)

    def __print_tree(self, node, indent, last):
        if node is not None:
            print(indent, end='')
            if last:
                print("R----", end='')
                indent += "     "
            else:
                print("L----", end='')
                indent += "|    "

            print(node.key)
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
