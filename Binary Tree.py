#Binary Tree
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data , end=' ')
        if self.right:
            self.right.printTree()


root = Node('1President')
root.insert('2Minister')
root.insert('3Minister')
root.insert('4Minister')
root.insert('5Minister')
root.insert('F')
root.insert('N')
root.insert('H')
root.insert('I')

root.printTree()