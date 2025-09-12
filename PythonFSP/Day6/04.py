class Node:
    def __init__(self, info):
        self.__data = info    # defining private instance variables
        self.__next = None

    def get_data(self):       # getter method for reading
        return self.__data
    
    def set_data(self, info): # setter method for writing
        self.__data = info

    def get_next(self):
        return self.__next
    
    def set_next(self, next_node):
        self.__next = next_node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        
    def get_head(self):
        return self.__head
    

    def set_head(self, node):
        self.__head = node

    def get_tail(self):
        return self.__tail
    
    def set_tail(self, node):
        self.__tail = node

    def append(self, info):
        # create the linked list if it is not pre-existing or append a new node at the end
        new_node = Node(info)
        if (self.get_head() is None):
            self.set_head(new_node)
            self.set_tail(new_node)
            new_node.set_next(None)
            print(f"Creating the Linked List with info = {info}...")
        else:
            print(f"Appending the new node at the end with info = {info}...")
            self.get_tail().set_next(new_node)
            self.set_tail(new_node)

    def display(self):
        ptr = self.get_head()
        if (ptr == None):
            print("Linked List is not pre-existing...")
        else:
            print("Displaying the content of the Linked List: ", end = "")
            while(ptr is not None):
                print(ptr.get_data(), end = ", ")
                ptr = ptr.get_next()
            print()

    def __str__(self):
        ptr = self.get_head()
        if (ptr == None):
            return "Linked List is not pre-existing..."
        msg = []
        while (ptr is not None):
            msg.append(str(ptr.get_data()))
            ptr = ptr.get_next()
        output = " ".join(msg)
        return "Content of the Linked List: " + output
    
    def search(self, info):
        if self.get_head() is None : 
            print("Linked List is empty !!!")
            return
        ptr = self.get_head()
        while ptr is not None:
            if (ptr.get_data() == info):
                print(f"Item {info} has been found successfully...")
                return
            ptr = ptr.get_next()
        print("Item has not been found")
        
    def delete(self, data_old):
        ptr = self.get_head()
        if (ptr == None):
            print("The Linked List is not pre-existing...")
            return
        if (ptr.get_data() == data_old):
            self.set_head(ptr.get_next())
            print("Deleting the first node of the Linked List...")
            del ptr
            return
        ptr_next = ptr.get_next()
        while(ptr_next != None and ptr_next.get_data() != data_old):
            ptr = ptr_next
            ptr_next = ptr_next.get_next()
        if (ptr_next != None and ptr_next.get_data() == data_old):
            ptr.set_next(ptr_next.get_next())
            if (ptr_next == self.get_tail()):
                self.set_tail(ptr)
            del ptr_next
            print("Successful deletion has occurred...")


lnk_list = LinkedList()
lnk_list.display()
print(lnk_list)
lnk_list.delete(100)
lnk_list.search(100)
info_data = [11, 22, 33, 44, 55]
for item in info_data:
    lnk_list.append(item)
lnk_list.display()
print(lnk_list)
lnk_list.search(100)
lnk_list.search(44)
lnk_list.delete(40)
lnk_list.delete(44)
lnk_list.display()