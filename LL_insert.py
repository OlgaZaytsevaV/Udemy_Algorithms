# create Class Node
class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None

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
            newNode.nextNode = self.head
            #update the references 
            self.head = newNode

# time compexity is O(1)       

    def size1(self): # time complexity is 0(1), because was store references
        return self.size

    def size2(self):#runtime complexity 0(n)
        while Node is not None:
            size +=1
            currentlNode = currentNode.nextNode  
        return size   

    def insertEnd(self, data):
        self.size +=1
        newNode=Node(data)   
        currentNode = self.head

# looking for the end of the LL
        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode
# when we find a last node(means that currentNode.nextNode =0)
# refer newNode as a new last Node
        currentNode.nextNode = newNode  

# runtime complexity 0(n)

    def traverseList(self):
        currentNode = self.head

        while currentNode is not None:
            print(currentNode.data)
            currentNode=currentNode.nextNode



LinkedList = LinkedList()

LinkedList.insertStart(12) 
LinkedList.insertStart(122)
LinkedList.insertStart(3)
LinkedList.insertEnd(31)

LinkedList.traverseList()
print(LinkedList.size1())













