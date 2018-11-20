#AVL tree implementation.
 class Node(object):
    def __init__(self,data):
    self.data = data
    self.right_child=None
    self.left_child = None
    self.height = 0

class AVL(object):
    def __init__(self):
        self.root = None

    def calculate_height(self, node):
        if not node:
            return -1
        return node.height    


# if returns > 1: it is a left heavy tree( will need to do a right rotation)
# if retruns <1 it's right-heavy (need to do a left rotation) 
# if returns 0 - tree is balanced   
    def balance(self, node):
        if not node:
            return 0
        return self.calculate_height(node.left_child)-self.calculate_height(node.right_child)    


    def rotate_right(self, node):
        print(node.data)
        temp_par=node.left_child
        t = temp_par.right_child
        # after the rotation temp is a new root, and t is a left child of temp's right child
        temp_par.right_child= node
        node.left_child= t
    
    node.height = max(self.calculate_height(node.left_child),self.calculate_height(node.right_child))+ 1
    temp_par = max(self.calculate_height(temp_par.left_child), self.calculate_height(temp_par.right_child))+1

    return 

    def rotate_left(self, node):
        print(node.data)
        temp_par=node.right_child
        t = temp_par.left_child
        # after the rotation temp is a new root, and t is a left child of temp's right child
        temp_par.left_child= node
        node.right_child= t
    
    node.height = max(self.calculate_height(node.left_child),self.calculate_height(node.right_child))+ 1
    temp_par = max(self.calculate_height(temp_par.left_child), self.calculate_height(temp_par.right_child))+1

    return temp_par






