class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next 
        return False
    
    def remove_beginning(self):
        if not self.head:
            return None  # Empty list
        removed_data = self.head.data
        self.head = self.head.next
        if not self.head:  # If list became empty
            self.tail = None
        return removed_data
    
    def remove_at_end(self):
        if not self.head:
            return None
        if self.head == self.tail:
            removed_data = self.head.data
            self.head = None
            self.tail = None
            return removed_data
        
        current = self.head
        while current.next != self.tail:
            current = current.next
        removed_data = self.tail.data
        current.next = None
        self.tail = current
        return removed_data
    
    def remove_at(self, data):
        if not self.head:
            return None  

        
        if self.head.data == data:
            return self.remove_beginning()

        prev = None
        current = self.head
        while current:
            if current.data == data:
                removed_data = current.data
                prev.next = current.next
                if current == self.tail:
                    self.tail = prev
                return removed_data
            prev = current
            current = current.next
        return None  

        
    
sushi_preparation = LinkedList()
sushi_preparation.insert_at_end("Prepare")
sushi_preparation.insert_at_end("Roll")
sushi_preparation.insert_at_beginning("Assemble")

x = sushi_preparation.search("Prepare")

