# Linked List Operations
class Node:
    def __init__(self, data):
        self.data = data   
        self.next = None    


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
        return current

    def length(self):
        current = self.head
        # traverse and increment the counter
        count = 0
        while current is not None:
            current = current.next
            count += 1
        return count

    def search(self, target):
        current = self.head
        # traverse and find the target
        while current is not None:
            if current.data == target:
                return True            # target found
            current = current.next
        return False

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)  
        new_node.next = self.head          # insert at beggining
        self.head = new_node
        return self.head

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        # if list is empty
        if self.head is None:
            self.head = new_node 
            return new_node
        current = self.head
        # traverse through last node
        while current.next is not None:
            current = current.next
        current.next = new_node       # insert at end
        return self.head

    def insert_at_pos(self, new_data, pos):
        # insert at head
        new_node = Node(new_data)
        if pos < 0 or pos >= self.length():
            raise Exception("invalid input")
        if pos == 1:
            new_node.next = self.head
            return new_node

        current = self.head
        count = 0
        while current is not None:
            if count == pos-1:
                new_node.next = current.next        # make link before
                current.next = new_node             # insert 
                break
            current = current.next
            count += 1
        return self.head

    def del_node(self, target):
        if self.head is None:         # empty
            return False
        if self.head.data == target:  # head node
            self.head = self.head.next  
            return True 
        current = self.head
        while current.next is not None:
            if current.next.data == target:  
                current.next = current.next.next
                return True 
            current = current.next
        return False  
        

if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_at_beginning(3)
    ll.insert_at_beginning(11)
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_pos(22, 3)
    print(ll.traverse())
    ll.del_node(5)
    print(ll.traverse())
    # print(ll.search(2))
    # print(ll.length())



