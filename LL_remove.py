class Node(object):

    def __init__(self,data):
        self.data = data
        self.nextNode = None 

class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.size = 0

    def remove(self):
        if self.head is None:
            return 
        size = self.size -1
        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode=currentNode.nextNode

            
# if no previous node, then the node we are looking for is head, 
# remove it and update references
        if previousNode is None:
            self.head = currentNode.nextNode

        else:
            previousNode.nextNode = currentNode.nextNode


LinkedList = LinkedList() 



                


