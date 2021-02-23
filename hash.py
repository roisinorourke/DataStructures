import sys

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)

#-------------------------------------------------------------------------

    # return the average length of the buckets 
    def average_bucket_length(self):
        total = 0
        index = 0
        count = 0
        for elem in self.table:
            if self.table[index] != None:
                total += len(self.table[index])
                count += 1
            index += 1
        return total / count

    # return the minimum and maximum bucket lengths
    def min_max_bucket_length(self):
        max = 0
        min = 0 
        i = 0
        for items in self.table:
            if self.table[i] != None:
                if min == 0:
                    min = len(self.table[i])
                elif min > len(self.table[i]):
                    min = len(self.table[i])
                
                if max == 0:
                    max = len(self.table[i])
                elif max < len(self.table[i]):
                    max = len(self.table[i])
            i += 1
        
        return (min, max)

    # return the max bucket length
    def longest_bucket_length(self):
        longest = 0
        i = 0
        for items in self.table:
            if self.table[i] != None:
                if longest < len(self.table[i]):
                    longest = len(self.table[i])
            i += 1

        return longest

    # iterate through a hash table
    def __iter__(self):
        index = 0
        for item in self.table:
            if self.table[index] != None:
                ptr = self.table[index].head
                while ptr != None:
                    yield ptr.item
                    ptr = ptr.next
            index += 1

    # Print out the hash table
    def __str__(self):
        s = ""
        for i in range(len(self.table)):
            s += "table[" + str(i) + "]"
            if self.table[i] != None:
                s += " Head " + str(self.table[i])
            s += "\n"

        return s

#-----------------------------------------------------------
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

    def __iter__(self):
        cursor = self.head
        while cursor is not None:
            yield cursor.item
            cursor = cursor.next

    def recursive_len(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.recursive_len(ptr.next)

    def __len__(self):
        return self.recursive_len(self.head)

    def recursive_contains(self, ptr, item):
        if ptr == None:
            return False
        else:
            return item == ptr.item or self.recursive_contains(ptr.next)

    def __in__(self, item):
        return recursive_contains(self.head, item)

    def recursive_str(self, ptr):
        if ptr == None:
            return ""
        else:
            return str(ptr.item) + "->" + self.recursive_str(ptr.next)

    def __str__(self):
        return self.recursive_str(self.head)

#------------------------------------------------------------------

def str_hash(s):
    """ Return a normal hash, unless it is a string. """
    if not isinstance(s, str):
        return hash(s) # not a string => use the normal hash function
    else:
        # Just use the first character of the string. (Not a good hash!)
        h = 0
        s_len = len(s) - 1
        if len(s) > 0:
            for letter in s:
                h += ord(letter) * (31 ** s_len)
                s_len -= 1 # Get the ASCII value of the first char of the string as the hash
        return h

#-----------------------------------------------------------------

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]
    
    # First number is the capacity
    numset = HashSet(nums[0])

    for x in nums[1:]:
        numset.add(x)

    print(numset.min_max_bucket_length())
    print(str_hash(numset))

if __name__ == "__main__":
    main()