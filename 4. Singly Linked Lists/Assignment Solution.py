# Q1
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Q2
class SLL:
    def __init__(self, start=None):
        self.start = start

# Q3
    def is_empty(self):
        return self.start == None
    
#  Q4   
    def insert_at_start(self, data):
        newNode = Node(data, self.start)
        self.start = newNode
# Q5
    def insert_at_last(self, data):
        newNode = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
        else:
            self.start = newNode

# Q6
    def search(self, data):
        temp = self.start
        while temp is not None:
            temp=temp.next
            if temp.data == data:
                return True
        return False

# Q7