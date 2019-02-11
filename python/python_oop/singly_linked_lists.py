class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = Node(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner != None:
            print(runner.val)
            runner = runner.next
        return self
    
    def add_to_back(self, val):
        new_node = Node(val)

        # check if the list is empty
        if self.head == None:
            self.head = new_node
        else:
            runner = self.head
            # this will break if the list is empty
            while runner.next != None:
                runner = runner.next
            runner.next = new_node
        return self
    
    def remove_from_front(self):
        # expect an error if list is empty, this is intentional
        removed = self.head
        self.head = self.head.next
        removed.next = None
        return removed.val

    def remove_from_back(self):
        # expect an error if list is empty, this is intentional
        # avoid an error if we're removing from a list with < 2 nodes
        if self.head.next == None:
            removed = self.head.next
            self.head = None
            return removed.val

        curr = self.head
        # look 2 ahead
        # when we stop, we'll be at the 2nd to last node
        while curr.next.next != None:
            curr = curr.next
        removed = curr.next
        curr.next = None
        return removed.val

    def remove_val(self, val):
        # expect an error if there are no nodes
        if self.head.val == val:
            removed = self.head
            if self.head.next == None:
                self.head = None
            else:
                self.head = self.head.next
                removed.next = None
            return removed.val
        
        curr = self.head
        while curr.next != None:
            if curr.next.val == val:
                removed = curr.next
                curr.next = curr.next.next
                removed.next = None
                return removed.val
            curr = curr.next
        
        print("Value not found")
        return self
    
    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
        else:
            # expect an error if n is out of bounds
            new_node = Node(val)
            curr = self.head
            prev = None
            while n > 0:
                prev = curr
                curr = curr.next
                n -= 1
            prev.next = new_node
            new_node.next = curr
        return self

my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back('fun!')
my_list.remove_val("are")
# my_list.remove_val("Linked lists")
# my_list.remove_val("fun!")
my_list.insert_at("What", 0)
my_list.print_values()