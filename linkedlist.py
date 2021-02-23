#
#  Just a class to store the item and the next pointer
#
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None

    # print a linkedlist
    def listprint(self):
        current = self.head
        while current is not None:
            print (current.item)
            current = current.next
        
    def __str__(self):
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += str(ptr.item) + " "
            ptr = ptr.next
            
        return tmp_str

    # find the length of a linkedlist (non-recursive)
    def length(self):
        count = 0
        ptr = self.head
        while ptr != None:
            count += 1
            ptr = ptr.next
        return count

    # find the maximum element in a linkedlist
    def findmax(self):
        ptr = self.head
        maxi = self.head
        while ptr.next != None:
            if ptr.next.item > maxi.item:
                maxi =  ptr.next
            ptr = ptr.next
        return maxi.item

    # check if a linked list contains an item
    def contains(self, arg):
        current = self.head
        if self.is_empty():
            return False
        
        else:
            while current is not None:
                if current.item == arg:
                    return True
                current = current.next
            return False

    # return the element that comes after a specific item
    def after(self, item):
        current = self.head
        while current is not None:
            if current.item == item and current.next != None:
                return current.next.item
            current = current.next
        return None

    # return the element that comes before a specific item
    def before(self, item):
        current = self.head
        if current is not None:
            while current.next is not None:
                if current.next.item == item and current.next != None:
                    return current.item
                current = current.next
        return None

    # append an element to the end of the linked list
    def append(self, item):
        current = self.head
        if current is not None:
            while current.next is not None:
                current = current.next
        
            current.next = Node(item, current.next)
            
        else:
            self.add(item)
    
    # rotate a linkedlist
    def rotate(self):
        current = self.head

        self.append(current.item)
        self.remove()

#-----------------------------------------------------------------

# check if a linkedlist passed in is a loop
def detect_loop(lst):
    current = lst.head
    if current is not None:
        while current.next is not None:
            current = current.next
        
            if current.next == lst.head:
                return True
        
    else:
        return False

# find the max elem in a linkedlist that has been passed in
def find_max(ll):
        ptr = ll.head
        maxi = ll.head
        while ptr.next != None:
            if ptr.next.item > maxi.item:
                maxi =  ptr.next
            ptr = ptr.next
        return maxi.item

#-----------------------------------------------------------------

import sys

def main():
    # Read each set
    items = [1, 2, 10, 4, 2, 6, 5]
    
    ll = LinkedList()
    
    for item in items:
        ll.add(item)
    
    print(ll.length())
    #print(ll.findmax())
    #print(ll.contains(5))
    #print(ll.contains(10))
    #print(ll.after(1))
    #print(ll.after(5))
    #print(ll.before(5))
    #print(ll.before(1))
    #print("break")
    #ll.listprint()
    #print(ll)
    #ll.rotate()
    #print(ll)
    print(find_max(ll))

if __name__ == "__main__":
    main()