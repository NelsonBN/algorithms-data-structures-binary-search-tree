class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None



class BinarySearchTree:
    def __init__(self):
        self.__root = None


    def insert(self, key): # Big-O: O(n) / Big-Theta: Θ(log n)
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



    def delete(self, key): # Big-O: O(n) / Big-Theta: Θ(log n)
        self.__root = self.__delete(self.__root, key)

    def __delete(self, node, key):
        if node is None:
            return node

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


    def inorder(self):
        return self.__inorder(self.__root)

    def __inorder(self, node):
        keys = []
        if node is not None:
            keys = self.__inorder(node.left)
            keys.append(node.key)
            keys = keys + self.__inorder(node.right)
        return keys


    def preorder(self):
        return self.__preorder(self.__root)

    def __preorder(self, node):
        keys = []
        if node is not None:
            keys.append(node.key)
            keys = keys + self.__preorder(node.left)
            keys = keys + self.__preorder(node.right)
        return keys


    def postorder(self):
        return self.__postorder(self.__root)

    def __postorder(self, node):
        keys = []
        if node is not None:
            keys = self.__postorder(node.left)
            keys = keys + self.__postorder(node.right)
            keys.append(node.key)
        return keys



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
print(f'Inorder  : {bst.inorder()}')
print(f'Preorder : {bst.preorder()}')
print(f'Postorder: {bst.postorder()}')


print("\nDelete 20:")
bst.delete(20)

bst.print_tree()
print(f'Inorder  : {bst.inorder()}')
print(f'Preorder : {bst.preorder()}')
print(f'Postorder: {bst.postorder()}')


print("\nDelete 70:")
bst.delete(70)

bst.print_tree()
print(f'Inorder  : {bst.inorder()}')
print(f'Preorder : {bst.preorder()}')
print(f'Postorder: {bst.postorder()}')


print("\nDelete 50:")
bst.delete(50)

bst.print_tree()
print(f'Inorder  : {bst.inorder()}')
print(f'Preorder : {bst.preorder()}')
print(f'Postorder: {bst.postorder()}')
