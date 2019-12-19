# Implement a queue using a linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.nextn = None

        

class Queue:
    def __init__(self):
        self.front = None
        self.end = None
        self.length = 0
    
    def add(self, value):
        new_node = Node(value)
        
        if self.length:
            self.end.nextn = new_node
            self.end = new_node
        else:
            self.front = new_node
            self.end = self.front
        
        self.length += 1
        
    def remove(self):
        if self.length:
            old_front = self.front 
            self.front = self.front.nextn
            self.length -= 1
            return old_front.value
            
        return None
