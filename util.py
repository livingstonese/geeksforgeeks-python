class BinaryTree:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None
    def isLeafNode(self):
        return self._left is None and self._right is None

def inorder(node):
    if node is None: return
    inorder(node._left)
    print node._data, ' ',
    inorder(node._right)
