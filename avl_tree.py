class TreeNode:
    def __init__(self, key, value = None):
        self.val = value
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return '['+str(self.key)+']='+str(self.val)




class AVLTree:
    def __init__(self, size = 0):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def find(self, key):
        node = self.root
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node
        return None

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)
        return self.root


    def _insert(self, node, key, value):
        if not node:
            self.size += 1
            return TreeNode(key, value)
        elif key < node.key:
            node.left = self._insert(node.left, key, value)

        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.val = value
            return node

        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))

        return self.makeBalance(node)


    def delete(self, key):
        self.root = self._delete(self.root, key)
        return self.root

    def _delete(self, node, key):
        if not node:
            return node
        elif key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.getMinKeyNode(node.right)
            node.key = temp.key
            node.val = temp.val
            node.right = self._delete(node.right,
                                     temp.key)
        if node is None:
            return node
        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))

        return self.makeBalance(node)


    def makeBalance(self, node):
        balance = self.getBalance(node)
        if balance < -1 and self.getBalance(node.left) <= 0:

            return self.rightRotate(node)
        if balance > 1 and self.getBalance(node.right) >= 0:

            return self.leftRotate(node)
        if balance < -1 and self.getBalance(node.left) > 0:

            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance > 1 and self.getBalance(node.right) < 0:

            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        return node


    def leftRotate(self, top_node):
        right_top_node = top_node.right
        temp_node = right_top_node.left
        right_top_node.left = top_node
        top_node.right = temp_node
        top_node.height = 1 + max(self.getHeight(top_node.left),
                                  self.getHeight(top_node.right))
        right_top_node.height = 1 + max(self.getHeight(right_top_node.left),
                                        self.getHeight(right_top_node.right))
        return right_top_node

    def rightRotate(self, top_node):
        left_top_node = top_node.left
        temp_node = left_top_node.right
        left_top_node.right = top_node
        top_node.left = temp_node
        top_node.height = 1 + max(self.getHeight(top_node.left),
                                  self.getHeight(top_node.right))
        left_top_node.height = 1 + max(self.getHeight(left_top_node.left),
                                       self.getHeight(left_top_node.right))
        return left_top_node

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.right) - self.getHeight(node.left)

    def getMinKeyNode(self, node):
        if node is None or node.left is None:
            return node
        return self.getMinKeyNode(node.left)

    def printKeys(self, in_order = True):
        if in_order:
            self.inOrder(self.root)
        else:
            self.preOrder(self.root)
        print()

    def inOrder(self, node):
        if not node:
            return
        if node.left:
            self.inOrder(node.left)
        print(node.key, end=' ')
        if node.right:
            self.inOrder(node.right)



    def preOrder(self, node):
        if not node:
            return
        if node.right:
            self.preOrder(node.right)
        print(node.key, end=' ')
        if node.left:
            self.preOrder(node.left)


    def get_keys(self):
        if self.root is not None:
            return self._get_keys(self.root, [])

    def _get_keys(self, node, arr):
        if node is not None:
            self._get_keys(node.left, arr)
            arr.append(node.key)
            self._get_keys(node.right, arr)
        return arr



class TreeSet:
    def __init__(self):
        self.tree = AVLTree()

    def add(self, val):
        self.tree.insert(val, val)

    def __contains__(self, item):
        return self.tree.find(item) is not None

    def __str__(self):
        keys = self.tree.get_keys()
        res = ''
        for k in keys:
            res += str(k) + ' '
        return res

    def __len__(self):
        return len(self.tree)


def main():
    myTree = AVLTree()
    nums = [9, 1, 5, 10, 0, 1, 6, 2,2,11, -1, 1, 2]

    for num in nums:
        root = myTree.insert(num, num*2)

        # Preorder Traversal
    print("Preorder Traversal after insertion -")
    myTree.printKeys()
    myTree.printKeys(False)

    # Delete
    key = 1
    myTree.delete(key)

    # Preorder Traversal
    print("Preorder Traversal after deletion -")
    myTree.printKeys()
    myTree.printKeys(False)

if __name__ == '__main__': main()