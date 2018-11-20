#binary serach tree implementation

class Node(object):
    def __init__(self, data):
        self.data=data
        self.left_child = None
        self.right_child = None

# binary serach tree can have only 2 children (left and right) 

class Binary_Search_Tree(object):
    def __init__(self):
        self.root = None

# insert method for binary search tree

    def insert(self,data):
        if  not self.root:
            self.root = Node(data)

        else:
            self.insertNode(data, self.root)

    def insertNode(self,data, node):
        if data < node.data:
            if node.left_child:
                self.insertNode(data, node.left_child)
            else:
                node.left_child= Node(data)    

        else:
            if node.right_child:
                self.insertNode(data, node.right_child)
            else:
                node.right_child= Node(data)   


# min value method

    def minValue(self):
        if self.root:
            return self.getMinValue(self.root)
    def getMinValue(self,node):
        if node.left_child:
            return self.getMinValue(node.left_child)
        return node.data
        
    def maxValue(self):
        if self.root:
            return self.getMaxValue(self.root)
    def getMaxValue(self,node):
        if node.right_child:
            return self.getMaxValue(node.right_child)
        return node.data
        
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)
    def traverseInOrder(self, node):
        if node.left_child:
            self.traverseInOrder(node.left_child) 
        if node.right_child:
            self.traverseInOrder(node.right_child)



BST=Binary_Search_Tree()
BST.insert("C")
BST.insert("A")
BST.insert("Z")


print(BST.maxValue())









                


                    
