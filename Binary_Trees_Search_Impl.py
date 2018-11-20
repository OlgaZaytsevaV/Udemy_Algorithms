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

    def removeNode(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.left_child = self.removeNode(data, node.left_child) 
        elif data > node.data:
            node.right_child=self.removeNode(data, node.right_child)

        else:
            # node is a leaf node: no children at all
            if not node.left_child and not node.right_child:
                print("Removing a leaf node")
                del node
                return None

            if not node.left_child:
                print("removing a node with a single right child") 
                temNode = node.left_child
                del node
                return temNode

            elif not node.right_child:
                print("removing a node with a single left child") 
                temNode = node.right_child
                del node
                return temNode

            print("Removing node with two children")  
            temNode = self.getPredecessor(node.left_child) 
            node.data = temNode.data
            node.left_child= self.removeNode(tempNode.data, node.left_child) 
        return node


    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)  

    def getPredecessor(self, node):

        #the predecesor the largest node in the left sudtree
        #successor: the smallest node in the right subtree
        if node.right_child:
            return self.getPredecessor(node.right_child)
        return node    
   
        

                    


            

                




BST=Binary_Search_Tree()
BST.insert(10)
BST.insert(13)
BST.insert(5)
BST.insert(14)
BST.remove(13)


print(BST.maxValue())









                


                    
