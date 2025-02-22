class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getData(self):
        return self.data

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def setData(self, data):
        self.data = data
