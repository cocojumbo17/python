class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None




class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""




def level_order(root):
    # Write your code here
    if root is None:
        return

    arr1 = []
    arr1.append(root)

    while (len(arr1) > 0):

        print(arr1[0].info, end=' ')
        node = arr1.pop(0)

        if node.left is not None:
            arr1.append(node.left)

        if node.right is not None:
            arr1.append(node.right)

def main():
    tree = BinarySearchTree()
    print("Введіть кількість елементів")
    t = int(input())
    print("Введіть", t, "елементів")
    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    level_order(tree.root)
main()