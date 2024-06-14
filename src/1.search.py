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

search = 20
print(f"Search {search}: {bst.search(search) is not None}")

search = 80
print(f"Search {search}: {bst.search(search) is not None}")

search = 200
print(f"Search {search}: {bst.search(search) is not None}")
