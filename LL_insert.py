# create Class Node
class Node(object):

    def __init__(self, data):
        self.data = data
        self.NextNode = None

class LinkedList(object):
    def __init__(self):
        self.head =None # accessing a first Node
        self.size = 0

    def insertStart(self, data):
        self.size = self.size+1
        newNode = Node(data)


# if no Nodes, then newNode is a head
        if not self.head:
            self.head = newNode
        else:
            # inserting a Node at the beginning of the LL
            newNode.next = self.head
            #update the references 
            self.head = newNode

# time compexity is O(1)       

    def size(self): # time complexity is 0(1), because was store references
        return self.size

    def size2(self):#time complexity 0(n)
        while Node is not None:
            size +=1
            currentlNode = currentNode.nextNode  

        return size    








