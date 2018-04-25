__author__='Sudhanshu Patel'
'''
Binary search tree implementation
it support all basic functionality of BST
'''

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.utility_insert(self.root, key)

    def print(self, type='INORDER'):
        if type == 'INORDER':
            print('Inorder Traversal :>')
            self.inorder(self.root)

    def utility_insert(self, this_node, key):
        if this_node.key > key:
            if this_node.left is None:
                this_node.left = Node(key)
            else:
                self.utility_insert(this_node.left, key)
        else:
            if this_node.right is None:
                this_node.right = Node(key)
            else:
                self.utility_insert(this_node.right, key)

    def inorder(self, this_node):
        if this_node:
            self.inorder(this_node.left)
            print(this_node.key, ', ',end='')
            self.inorder(this_node.right)


if __name__=='__main__':
    print('Binary Search TREE')
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(7)
    bst.insert(3)
    bst.print()
